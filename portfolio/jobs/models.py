from django.db import models
from urllib.parse import urlparse


# Create your models here.
class Job(models.Model):
	#Two properties : Image and Summary
	image = models.ImageField(upload_to = 'images/')
	info = models.CharField(max_length=100)
	summary = models.CharField(max_length=400)
	link = models.URLField(default='')


	def __str__(self):
		return(self.summary)
	def url_text(self):
		parsed_url = urlparse(self.link)
		return parsed_url.hostname.replace("www.", "") + "/..."
