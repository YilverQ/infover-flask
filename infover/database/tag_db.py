from .connection import get_table_named, get_element_fromWith, get_themes_by_tag
from ..helpers.convert_data_to_model import convert_data_to_tag_object

def get_tags():
	table = get_table_named("Tag")
	tags = []
	for element in table:
		tag = convert_data_to_tag_object(element)
	return tags


def get_tag_named(name):
	element = get_element_fromWith("Tag", name)
	tag = convert_data_to_tag_object(element)
	return tag.as_dict()