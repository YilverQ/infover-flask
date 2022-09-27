class Author:
	def __init__(self, name, title, url_image, logo_image, index, introduction, body, finale):
		self.name = name
		self.title = title
		self.url_image = url_image
		self.logo_image = logo_image
		self.index = index
		self.introduction = introduction
		self.body = body
		self.finale = finale


	def as_dict(self):
		return {"name": self.name,
				"title": self.title,
				"url_image": self.url_image,
				"logo_image": self.logo_image,
				"index": self.index,
				"introduction": self.introduction,
				"body": self.body,
				"finale": self.finale}