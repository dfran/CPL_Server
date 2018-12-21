#! /usr/bin/python
from flask import Flask, render_template, request
#from Classes import VcsClass

trusted_partners = ["dimensiondata.call.ciscospark.com"]
internal_domains = ["labddfr.com"]
callable_domains = ["pmr.labddfr.com"]

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
	#ap.logger.debug(data)
	#split = data.split("&")
	app.logger.debug(data)
	
	my_list = [tuple(i.split('=')) for i in data.split('&')]
	my_dict = dict(my_list)
	
	
	app.logger.debug(my_dict["UNAUTHENTICATED_SOURCE_ALIAS"].split("%40")[1])

	
	return "0"

@app.route('/callpolicy',methods=['POST'])
def callpolicy():

        data = request.get_data(cache=False)
        my_list = [tuple(i.split("=")) for i in data.split('&')]
        my_dict = dict(my_list)
	
	app.logger.debug(data)
		
	if my_dict["AUTHENTICATED"] == "FALSE": 
		if my_dict["UNAUTHENTICATED_SOURCE_ALIAS"].split("%40")[1] in trusted_partners or my_dict["DESTINATION_ALIAS"].split("%40")[1] in callable_domains:
			
			app.logger.debug("Incoming Call Allowed")
			return render_template("allow_cpl_frame")
			

	elif my_dict["AUTHENTICATED_SOURCE_ALIAS"].split("%40")[1] in internal_domains:
		
		app.logger.debug("Call to External Allowed")
		return render_template("allow_cpl_frame")
			
	
	app.logger.debug("Call Refused")
	return render_template("reject_cpl")
		

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
