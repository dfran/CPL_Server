#! /usr/bin/python
from flask import Flask, render_template, request
#from Classes import VcsClass

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return "Hello !"

@app.route('/Damien')
def damien():
	return "Damien"

@app.route('/status',methods=['GET'])
def status():
	return "Server is UP!!!"

@app.route ('/allow',methods=['GET','POST'])
def allowframe():
	return render_template('allow_cpl_frame')

@app.route ('/deny',methods=['POST'])
def deny():
	return render_template('reject_cpl')

@app.route ('/partners',methods=['POST'])
def partners():
	
	data = request.get_data(cache=False)
	#app.logger.debug(data)
	split = data.split("&")
	app.logger.debug(split[15])
	return "0"





if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
