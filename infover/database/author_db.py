from .connection import get_author_data
from ..helpers.convert_data_to_model import convert_data_to_author_object

def get_author_from_data():
	element = get_author_data()
	author = convert_data_to_author_object(element)
	return author