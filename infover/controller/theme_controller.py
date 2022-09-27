from ..database import theme_db


class Theme_Controller:
	def __init__(self):
		pass


	def read(self):
		return theme_db.get_themes()


	def read_only(self, theme):
		return theme_db.get_theme_named(theme)


	def read_themes_by(self, father):
		return theme_db.read_themes_with_father(father)