from flask import Flask, render_template, request, redirect, session

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


if __name__ == "__main__":
    app.run(debug=True)