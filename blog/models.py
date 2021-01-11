from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import jdatetime

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
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		unique_together = ('title', 'slug')

	def __str__(self):
		return self.title 

	def get_fullname(self):
		return self.author.first_name + " " + self.author.last_name

	def get_status(self):
		if self.status == 'd':
			return "پیش نویس"
		else:
			return "انتشار یافته"

	def get_datetime(self):
		return jdatetime.date(self.publish.year, self.publish.month, self.publish.day)
