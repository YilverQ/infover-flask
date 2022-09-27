class Tag:
	def __init__(self, id_tag, name, title, url_image, logo_image, index, introduction, body, finale):
		self.id_tag = id_tag
		self.name = name
		self.title = title
		self.url_image = url_image
		self.logo_image = logo_image
		self.index = index
		self.introduction = introduction
		self.body = body
		self.finale = finale


	def as_dict(self):
		return {"id": self.id_tag,
				"name": self.name,
				"title": self.title,
				"url_image": self.url_image,
				"logo_image": self.logo_image,
				"index": self.index,
				"introduction": self.introduction,
				"body": self.body,
				"finale": self.finale}