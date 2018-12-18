from flask import Flask, request, redirect
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environement(loader = jinja2.FileSystemLoader(template_dir))

