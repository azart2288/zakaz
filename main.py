from flask import Flask, render_template, request, redirect, session
from addpost import Post
import sqlite3
import os
import time

app = Flask(__name__)
# globuser = "Cymbal"
globpas = "Olesya"
Login = False


# passwords = {
# 'Cymbal': 'Azart2008',
# 'user2': 'password2',
# 'user3': 'password3'
# }

app.secret_key = 'zsasxcsdcsdfsdfsvsdgsdgdsg'

@app.route('/')
def home():
    return render_template('main.html')


@app.route('/library')
def index():
    return render_template('index.html')


@app.route('/login-page')
def login_page():
    if 'logged_in' in session and session['logged_in']:
        return redirect('/post')
    else:
        return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    # username = request.form['username']
    password = request.form['password']

    if password == globpas:
        session["password"] = password
        session['logged_in'] = True
        return redirect('/post')
        # Login = True
    else:
        return "Неверные имя пользователя или пароль."


@app.route('/post')
def post():
    if 'logged_in' in session and session['logged_in']:
        return render_template('upload-post.html')
    else:
        return redirect('/')


@app.route('/up_post', methods=['POST'])
def up_post():
    post_text = request.form["text_of_post"]
    new_post = Post()
    name_post = "local_post"
    text = post_text
    name = name_post
    photo = request.files['photo']
    photo_post = photo.filename
    try:
        photo.save(os.path.join('static', photo.filename))
    except:
        pass
    new_post.create_post(post_text, name_post, photo_post)
    return redirect('/posts')

    #return post_text
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
    

@app.route('/posts')
def posts():
    connection = sqlite3.connect('mydatabase.db')
    cursor = connection.cursor()
    select_query = "SELECT texts, photo FROM mytable"
    select_image = "SELECT photo FROM mytable"

    cursor.execute(select_query)
    #cursor.execute(select_image)

    # Получение результатов запроса
    results = cursor.fetchall()
    posts = [(result[0], result[1]) for result in results]
    #imgs = [result[0] for result in results]
    #images = [result[0] for result in results]
    #file = (posts[1])

    #file = os.path.join("static" , posts_str)
    #posts = [result[0] for result in results]
    #posts_str = ' '.join(imgs)
    #fi#le = os.path.join("static" , posts_str)
    cursor.close()
    connection.close()

    return render_template("articles.html", posts=posts)


if __name__ == "__main__":
    app.run(debug=True)