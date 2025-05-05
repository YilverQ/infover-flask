from infover import db
from database import BaseModel

class Author(BaseModel):
	name 			 = CharField(null=False)
	title 			 = CharField(null=False)
	image_profile 	 = BlobField() #Guardamos la imagen en binario
	image_background = BlobField()
	description 	 = TextField()
	nacionality 	 = CharField()
	institute 		 = CharField()
	created_at 		 = TimestampField(default=datetime.datetime.now)
	updated_at 		 = TimestampField(default=datetime.datetime.now)
	email 			 = CharField(unique=True, null=False)


	def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()  # Actualiza timestamp antes de guardar
        return super().save(*args, **kwargs)