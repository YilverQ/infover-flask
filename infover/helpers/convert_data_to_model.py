from ..models.tag import Tag
from ..models.theme import Theme


def convert_data_to_tag_object(element):
	tag = Tag(id_tag = element["id"],
				  name = element["name"],
				  title = element["title"],
				  url_image = element["url_image"],
				  logo_image = element["logo_image"],
				  index = element["index"],
				  introduction = element["introduction"],
				  body = element["body"],
				  finale = element["finale"])
	return tag 


def convert_data_to_theme_object(element):
	theme = Theme(id_theme = element["id"],
				  father = element["father"],
				  id_tag = element["id_tag"],
				  name = element["name"],
				  title = element["title"],
				  url_image = element["url_image"],
				  logo_image = element["logo_image"],
				  index = element["index"],
				  introduction = element["introduction"],
				  body = element["body"],
				  reference = element["reference"],
				  finale = element["finale"])
	return theme 