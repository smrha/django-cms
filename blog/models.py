from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=256)
	content = models.TextField()
	slug = models.SlugField(unique=True, allow_unicode=True)
	# add status field
	# add publish field
	# add update field
	# add auther field

	class Meta:
		unique_together = ('title', 'slug')

	def __str__(self):
		return self.title 
