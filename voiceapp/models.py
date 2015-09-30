from django.db import models

# Create your models here.

class Keyword(models.Model):
	keyword = models.CharField(max_length=200)

	def __unicode__(self):
		return self.keyword

class Content(models.Model):
	content = models.TextField()
	keyword = models.ManyToManyField(Keyword)
	def __unicode__(self):
		return self.content