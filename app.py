from flask import Flask
import json


app = Flask(__name__)

@app.route('/')
def hello_world():
    try:
	    return render_template('index.html')
	except Exception as e:
		return str(e)

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
