from flask import Flask
import json


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Strat thinking!'

@app.route('/events')
def events():
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    
    
    return json.dumps(x)

if __name__ == '__main__':
    app.run()
