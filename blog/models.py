from django.db import models
from django.utils import timezone

class Post(models.Model):
	STATUS_CHOICES = (
		('d', 'پیش نویس'),
		('p', 'انتشار یافته'),
		)
	title = models.CharField(max_length=256)
	content = models.TextField()
	slug = models.SlugField(unique=True, allow_unicode=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=1, default='d', choices=STATUS_CHOICES)
	thumbnail = models.ImageField(upload_to='images', blank=True, null=True)
	# add auther field

	class Meta:
		unique_together = ('title', 'slug')

	def __str__(self):
		return self.title 
