from flask import Blueprint, render_template

global_scope = Blueprint("view", __name__)


from ..database.theme_db import *



@global_scope.route("/")
def index():
	""" Página principal """
	parameters = {"title": "Infover",
				  "description": "Blog informativo sobre tópicos de programación e ingeniería de software."
				 }
	data = None
	return render_template("index.html", data = data, **parameters)


@global_scope.route("/data")
def data():
	return get_theme_named("Api Rest")