import os
from dotenv import load_dotenv

load_dotenv()


class Config:
	#Application.
	SERVER_NAME = "192.168.0.104:5000"
	DEBUG = True

	#Database.
	DATABASE_PATH = "./infover/database/data.json"
	DB_TOKEN = os.environ.get("DB_TOKEN", "")
	ENCRYPT_DB = False

	#Folder Ubications.
	TEMPLATE_FOLDER = "views/templates"
	STATIC_FOLDER = "views/static"