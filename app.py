from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

@app.route("/greet/<name>")
def GreetPage(name):
    return render_template("index.html", name = name)

if __name__ == '__main__':
    app.run(debug = True)