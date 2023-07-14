import sqlite3

# Установка соединения с базой данных SQLite
connection = sqlite3.connect('mydatabase.db')

# Получение курсора
cursor = connection.cursor()

# SQL-запрос для выборки данных из таблицы
select_query = "SELECT photo FROM mytable"

# Выполнение SQL-запроса
cursor.execute(select_query)

# Получение всех результатов
results = cursor.fetchall()
posts = [result[0] for result in results]
#posts_str = ' '.join(posts)
file = "{{ url_for('static', filename= " , posts , "}}"

# Вывод результатов
print(posts_str)

# Закрытие соединения
connection.close()