#Modelo
import json

def leer_data():
	#abrir el archivo JSON
	with open("data.json", "r") as json_file:
		return json.load(json_file)



def get_user():
	#Devuelve un diccionario del bloque de Usuarios del archivo JSON
	# En caso de que no se encuentre nada, devuelve 0
	data = leer_data()
	item = "Yilver Quevedo"
	for i in data["Usuarios"]:
		if i["name"] == item:
			return i

	return 0



def get_all_tools(item = "Herramientas"):
	#Obtenemos todas las "Herramientas" del archivo JSON 
	""" 
		cada item de item_list será:
		i["name"] = i["logo_image"]
		{Bases De Datos = herramientas/bases_de_datos.png}
	"""
	data = leer_data()
	item_list = {}
	for i in data[item]:
		item_list[i["name"]] = i["logo_image"] #añadimos las herramientas
	return item_list



def get_technologies(item, bloque = "Tecnologias"):
	#Obtenemos todas las "Tecnologías" del archivo JSON
	"""
		Cuando recorremos el bloque de tecnologías, 
		comprobaremos si i["father"] corresponde a la herramientas que deseamos "father_item". 
			Ejemplo:
			flask["father"] == father_item
			Frameworks == Frameworks
		en caso de ser positivo lo agregamos a la lista de las tecnologías que queremos
	"""
	data = leer_data()
	father_item = item #
	bloque_search = bloque
	item_list = {}
	for i in data[bloque_search]: #Recorremos cada item del bloque "Tecnologías"
		if i["father"] == father_item: 
			item_list[i["name"]] = i["logo_image"]
	return item_list



def get_tecnologia(item, bloque = "Herramientas"):
	#Obtenemos los datos de la tecnología ("Flask", "UML"...) que buscamos, 
	#en caso contrario devolvemos 0
	data = leer_data()
	item_search = item
	for i in data[bloque]:
		if i["name"] == item_search:
			return i

	return 0



#Este codigo es para probar las funciones
if __name__ == "__main__":
	print(get_all_technologies("Arquitectura De Software"))