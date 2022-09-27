from flask import Blueprint, render_template

global_scope = Blueprint("view", __name__)


from ..controller import Tag_Controller, Theme_Controller, Author_Controller
tag_controller = Tag_Controller()
theme_controller = Theme_Controller()
author_controller = Author_Controller()


# Página principal
@global_scope.route("/")
def index():
	author = author_controller.get_author()
	parameters 	= {"title": author.name,
				   "description": author.introduction[0:140],
				   "Author": author,
				   "Tag": tag_controller.read(),
				   "Theme": theme_controller.read()
				  }
	return render_template("index.html", **parameters)


# Página de etiqueta.
@global_scope.route("/<string:tag>")
def tag(tag):
	tag = tag.replace("_", " ")
	data = tag_controller.read_only(tag)
	author = author_controller.get_author()
	parameters 	= {"title": data.name,
				   "description": data.introduction[0:140],
				   "Author": author,
				   "Tag": data,
				   "Theme": theme_controller.read_themes_by(tag)
				  }

	return render_template("tag.html", **parameters)


# Página de temas secundarios.
@global_scope.route("/<string:tag>/<string:theme>")
def theme(tag, theme):
	theme = theme.replace("_", " ")
	data = theme_controller.read_only(theme)
	parameters 	= {"title": data.name,
				   "description": data.introduction[0:140],
				   "Theme": data
				  }

	return render_template("theme.html", **parameters, type = type)