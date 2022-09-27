from ..database import tag_db


class Tag_Controller:
	def __init__(self):
		pass


	def read(self):
		return tag_db.get_tags()


	def read_only(self, tag):
		return tag_db.get_tag_named(tag)