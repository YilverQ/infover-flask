from ..database import author_db


class Author_Controller:
	def __init__(self):
		pass


	def get_author(self):
		return author_db.get_author_from_data()