from flask import Flask, render_template, request, redirect, session
import sqlite3
import os



class Post(object):
	"""docstring for Post"""
	def __init__(self):
		pass
	connection = sqlite3.connect('mydatabase.db')


	def create_post(self,text,name, photo):
		#os.mkdir(name)
		#os.chdir(name)
		connection = sqlite3.connect('mydatabase.db')
		cursor = connection.cursor()
		#connection = sqlite3.connect('mydatabase.db')

		# Создание SQL-запроса для создания таблицы
		create_table_query = '''CREATE TABLE IF NOT EXISTS mytable (
		                        id INTEGER PRIMARY KEY,
		                        name TEXT,
		                        texts TEXT,
		                        photo TEXT
		                    )'''

		insert_query = "INSERT INTO mytable (name, texts , photo) VALUES (?, ?, ?)"

		# Выполнение SQL-запроса
		cursor.execute(create_table_query)
		cursor.execute(insert_query, (name, text, photo))

		# Подтверждение изменений
		connection.commit()

		connection.close()





		