#! /usr/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return "Hello !"

@app.route('/Damien')
def damien():
	return "Damien"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
