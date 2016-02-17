from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=50)
	pub_time = models.DateTimeField(auto_now_add=True)
	category = models.CharField(max_length=50)
	limited_content = models.CharField(max_length=300)
	full_content = models.TextField()
	main_image = models.ImageField(upload_to="images", blank=True,null=True) 
	optional_image = models.ImageField(upload_to="images", blank=True,null=True)

	def __unicode__(self):
		return self.title

