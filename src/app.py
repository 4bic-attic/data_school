__author__='4bic'
from flask import Flask
app = Flask(__name__)

@app.route('/')

def hello_method():
    return "Hello World!!"


if __name__ == '__main__':
    app.run(port=4545)