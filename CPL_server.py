#! /usr/bin/python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return "Hello !"

@app.route('/Damien')
def damien():
	return "Damien"

@app.route ('/allow')
def allow():
	return render_template('allow_cpl')

@app.route('/allow-frame')
def allowframe():
	return render_template('allow_cpl_frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
