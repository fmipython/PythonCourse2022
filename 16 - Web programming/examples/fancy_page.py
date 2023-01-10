from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('fancy_index.html', title='Home', user='Lyubo')
