from flask import Flask, request, redirect
import os


app = Flask(__name__)

@app.route('/', methods=['POST'])
    return 'Hello, World!'

@app.route('/', methods=['GET'])
    return 'Hello, World!'
    
"""def post():
	calling_party
	Get the calling calling_party
	If the destination is an allowed one in the dictionnary 
	use the allow_cpl templace

	
	response = jinja_env.get_template('allow_cpl')

	#if not use the reject_cpl

	response = jinja_env.get_template('reject_cpl')

	return response

	"""

if __name__ == '__main__':
    app.run(debug=True)




