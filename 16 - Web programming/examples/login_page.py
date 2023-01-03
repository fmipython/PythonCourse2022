from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('fancy_index.html', title='Home', user='Guest')


@app.route("/login")
def login(message=None):
    return render_template('login.html', title='Login', message=message)


@app.route("/login_action", methods=['POST'])
def login_action():
    if request.method != 'POST':
        return redirect(url_for('/login', message='Invalid method'))

    if request.form['username'] == 'admin' and request.form['password'] == 'admin':
        return redirect(url_for('user/admin'))
    else:
        return redirect(url_for('login', message='Wrong username or password'))

@app.route("/user/<username>")
def user_page(username):
    return render_template('index.html', title='User', user=username)