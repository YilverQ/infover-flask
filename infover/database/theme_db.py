from .connection import get_table_named, get_element_fromWith, get_themes_by_tag
from ..helpers.convert_data_to_model import convert_data_to_theme_object

def get_themes():
	table = get_table_named("Theme")
	themes = []
	for element in table:
		theme = convert_data_to_theme_object(element)
		themes.append(theme)
	return themes


def get_theme_named(name):
	element = get_element_fromWith("Theme", name)
	theme = convert_data_to_theme_object(element)
	#return theme.as_dict()
	return theme


def read_themes_with_father(name):
	table = get_themes_by_tag(name)
	themes = []
	for element in table:
		theme = convert_data_to_theme_object(element)
		themes.append(theme)
	return themes