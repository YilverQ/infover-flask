from peewee import Model
from infover import db

class BaseModel(Model):
	class Meta:
		database = db