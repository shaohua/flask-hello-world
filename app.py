from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/get_page')
def get_page():
    return {
        "page": "<H1>Page</H1>"
    }
