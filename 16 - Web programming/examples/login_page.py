from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html', title='Home', user='Guest')


@app.route("/login_action", methods=['POST'])
def login_action():
    if request.method != 'POST':
        return redirect(url_for('/login', message='Invalid method'))

    if request.form['username'] == 'admin' and request.form['password'] == 'admin':
        username = request.form['username']
        return redirect(url_for('user', name=username))
    else:
        return redirect(url_for('login', message='Invalid username or password'))


@app.route("/login")
def login(message=None):
    print(message)
    return render_template('login.html', title='Login', message=message)


@app.route("/user/<name>")
def user_page(name):
    return render_template('user.html', title='User', user=name)
