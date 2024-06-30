from confluent_kafka import Producer
import json
import pandas as pd

config = {
    'bootstrap.servers': 'localhost:29092',  # адрес Kafka сервера
    'client.id': 'simple-producer'
}

producer = Producer(**config)

def data():
    from clickhouse_driver import Client

    dbname = 'default'

    with open(f"/Users/evgenijkolosov/PycharmProjects/pythonProject/keys/wb_key_ch_pegas.json") as json_file:
        data = json.load(json_file)

    client = Client(data['server'][0]['host'],
                    user=data['server'][0]['user'],
                    password=data['server'][0]['password'],
                    verify=False,
                    database=dbname,
                    settings={"numpy_columns": True, 'use_numpy': True},
                    compression=True)

    deps = client.execute(f"""
                select department_id, parent_department_id, department_name
                from dict_Department
                limit 100
                """)
    return deps
def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")

def send_message(data):
    try:
        # Асинхронная отправка сообщения
        producer.produce('click', data.encode('utf-8'), callback=delivery_report)
        producer.poll(0)  # Поллинг для обработки обратных вызовов
    except BufferError:
        print(f"Local producer queue is full ({len(producer)} messages awaiting delivery): try again")

if __name__ == '__main__':
    res = data()
    list_to_json = [{"department_id": x[0], "parent_department_id": x[1], "department_name": x[2]} for x in res]
    for i in list_to_json:
        send_message(json.dumps(i, ensure_ascii=False))

    producer.flush()