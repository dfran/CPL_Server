from flask import Flask, request, redirect
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environement(loader = jinja2.FileSystemLoader(template_dir))

app = Flask(__Policy__)

	@app.route('/', methods=['POST'])
	def post():
		"""calling_party
		Get the calling calling_party
		If the destination is an allowed one in the dictionnary 
		use the allow_cpl templace

		"""
		response = jinja_env.get_template('allow_cpl')

		#if not use the reject_cpl

		response = jinja_env.get_template('reject_cpl')

		return response


