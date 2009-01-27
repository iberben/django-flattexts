from django.db import models

class FlatText(models.Model):
	slug = models.SlugField()
	content = models.TextField()
	
	def __unicode__(self):
		"""A string representation of a Flattext"""
		return self.slug
	
