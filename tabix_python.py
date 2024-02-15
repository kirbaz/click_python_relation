# pip install clickhouse-driver
# pip install pytabix  - это сложно
from pytabix import Tabix
from clickhouse_driver import Client


# 1.
# Создайте экземпляр класса Client и подключитесь к базе данных ClickHouse:
client = Client(host='localhost', port=9000)
# Замените 'localhost' и 9000 на соответствующие значения для вашей конфигурации ClickHouse.
# Выполните запросы к базе данных:
result_cl = client.execute('SELECT * FROM my_table')
for row in result_cl:
    print(row)

# 2.
# Создайте экземпляр класса Tabix и подключитесь к базе данных ClickHouse:
tab_ex = Tabix('clickhouse://localhost:9000')
# Замените 'localhost' и 9000 на соответствующие значения для вашей конфигурации ClickHouse.
# Выполните запросы к базе данных:
result = tab_ex.query('SELECT * FROM my_table')
# Замените 'my_table' на имя вашей таблицы.
# Обработайте результаты запроса:
for row in result:
    print(row)
