from flask import Flask
from flask import render_template
import json


app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html')

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
