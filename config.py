import os
from dotenv import load_dotenv

load_dotenv()


class Config:
	#Application.
	SERVER_NAME = "192.168.116.238:5000"
	DEBUG = True

	#Database.
	DATABASE_PATH = "./infover/database/data.json"
	DATABASE = {
	    'name': 'infover.db',  
	    'engine': 'peewee.SqliteDatabase',
	}

	#Folder Ubications.
	TEMPLATE_FOLDER = "views/templates"
	STATIC_FOLDER = "views/static"
