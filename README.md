# wb_practice_kafka
1) поднять в docker-compose, из репозитория + sasl. выложить в свой git 
2) создать топик, создаётся автоматически при записи данных 
3) написать python скрипт для заливки данных из небольшой таблицы клика (пегас) в топик кафка в формате json. Всю таблицу не нужно пушить, достаточно limit 100. выложить скрипт в свой git 
4) программа Offset Explorer, просмотреть данные в топике. выложить скрины с результатами в свой git 
5) чтение из топика питоном. выложить в свой git

1.	Создаем папку /docker_with_sasl/
cd docker_with_sasl/
Создаем файлы: файл compose.yml, client.properties, kafka_server_jaas.conf, zookeeper_jaas.conf
Запускаем compose.yml docker compose up -d
 <img width="468" alt="image" src="https://github.com/SirRizzer/wb_practice_kafka/assets/61479067/2bac5c96-67c9-4506-91ed-f196e335657b">

Получаем развернутые контейнеры с конфигами, прописанными в созданных файлах.
Запускаем Offset explorer, создаем кластер ‘name’, прописываем сервер, выбираем версию кластера, в вкладке security выбираем SASL Plaintext, в вкладке Advanced SASL Mechanism прописываем PLAIN. Если ошибка коннекта по подключению jaas – прописываем в вкладке JAAS config org.apache.kafka.common.security.plain.PlainLoginModule required username="admin" password="admin-secret";
<img width="468" alt="image" src="https://github.com/SirRizzer/wb_practice_kafka/assets/61479067/13b50227-55d6-446c-a619-d66fb615a9ec">

2) Создаем топик, Content Type – везде String
 <img width="468" alt="image" src="https://github.com/SirRizzer/wb_practice_kafka/assets/61479067/39230c81-2706-4c94-a471-af3680a916d2">

3) Поднимаем clickhouse + kafka + zookeeper. Создаем новую папку и новый файл yml, указав для kafka свой ip. Подключаемся через offset по адресу localhost:9092. Подключаемся к клику user – default. Создаем встроенный consumer, таблицу для хранения сообщений, мат вью на продюсер. Скрипт по выгрузке с пегаса прилагается.
4) </br>
   <img width="468" alt="image" src="https://github.com/SirRizzer/wb_practice_kafka/assets/61479067/9bd4c9af-fbaf-4303-a7d5-d6081c74dbd2"></br>
 <img width="468" alt="image" src="https://github.com/SirRizzer/wb_practice_kafka/assets/61479067/83a509f3-be74-414f-9d33-25a1b630f2ee"></br>
5)  
 <img width="468" alt="image" src="https://github.com/SirRizzer/wb_practice_kafka/assets/61479067/6c40157a-22f7-41d0-b633-09acd4c51c63"></br>
<img width="1305" alt="image" src="https://github.com/SirRizzer/wb_practice_kafka/assets/61479067/a846147a-c453-4f03-9cb1-060e7cd91993">


