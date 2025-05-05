#Base de datos
import json
import os
from config import Config

#Ubicación de nuestra base de datos NoSQL.
config = Config()
DB_PATH = config.DATABASE_PATH


#Obtenemos todos los datos de nuestra base de datos.
def get_data():
	print("HOlaAAAAAA####", DB_PATH)
	with open(DB_PATH, "r") as json_file:
		return json.load(json_file)


#Obtenemos todos los datos de una tabla (table).
def get_table_named(table):
	all_data = get_data()
	return all_data[table]


#Obtenemos únicamente los datos de un elementos dentro de una tabla "Tags".
def get_element_fromWith(table, name):
	all_data = get_data()
	for i in all_data[table]:
		if i["name"] == name:
			return i


#Obtenemos únicamente los elementos que coincidan con la etiqueta.
def get_themes_by_tag(name):
	all_data = get_data()
	data = []
	for  i in all_data["Theme"]:
		if i["father"] == name:
			data.append(i)

	return data


def get_author_data():
	all_data = get_data()
	return all_data["Author"]