# simple hello world flask app

from flask import Flask 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

# run the app
if __name__ == '__main__':
    app.run()
