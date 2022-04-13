from flask import Flask, render_template, redirect, url_for
from model import *


app = Flask("__main__")
#app.secret_key = "FlaskAplication"


@app.route("/")
def index():
	datos = get_user()
	tarjetas = get_all_tools()
	tarjetas_technology = get_all_tools("Tecnologias")
	if datos != 0:
		return render_template("index.html", datos = datos, tarjetas = tarjetas, 
								tarjetas_technology =  tarjetas_technology)
	else:
		return redirect(url_for("error"))


@app.route("/tag1")
@app.route("/tag1/")
def tag1():
	return redirect(url_for("error"))


@app.route("/tag1/<string:herramienta>")
def herramienta(herramienta):
	datos = get_tecnologia(herramienta.title().replace("_", " "), "Herramientas")
	if datos != 0:
		tarjetas = get_technologies(datos["name"])
		return render_template("herramienta.html", datos = datos, tarjetas = tarjetas)
	else:
		return redirect(url_for("error"))


@app.route("/tag2")
@app.route("/tag2/")
def tag2():
	return redirect(url_for("error"))


@app.route("/tag2/<string:tecnologia>")
def tecnologia(tecnologia):
	datos = get_tecnologia(tecnologia.replace("_", " "), "Tecnologias")
	if datos != 0:
		return render_template("tecnologia.html", datos = datos)
	else:
		return redirect(url_for("error"))


@app.route("/error404")
def error():
	return render_template("error404.html")


if __name__ == "__main__":
	app.run(debug = True, port = 5000)

#host = "192.168.43.7"
