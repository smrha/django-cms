from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=256)
	content = models.TextField()
	# add slug field
	# add status field
	# add publish field
	# add update field
	# add auther field

	def __str__(self):
		return self.title 
