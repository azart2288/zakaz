import sqlite3

# Установка соединения с базой данных SQLite
connection = sqlite3.connect('mydatabase.db')

# Получение курсора
cursor = connection.cursor()

# SQL-запрос для выборки данных из таблицы
select_query = "SELECT texts, photo FROM mytable"

# Выполнение SQL-запроса
cursor.execute(select_query)

# Получение всех результатов
results = cursor.fetchall()
posts = [(result[0], result[1]) for result in results]

# Вывод результатов
print(posts)

# Закрытие соединения
connection.close()