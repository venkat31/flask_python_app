from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/hello')
def hello():
    return " Hello World from flask app"

@app.route('/<name>')
def user(name):
    return f"Hello {name}!"

@app.route('/admin')
def admin():
    return redirect(url_for("home"))

@app.route('/index')
def index():
    items = ['Item 1', 'Item 2', 'Item 3']
    return render_template('index.html', items=items)

if __name__ == "__main__":
    app.run(debug=True)