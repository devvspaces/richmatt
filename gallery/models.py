from django.db import models

from django.urls import reverse

# Create your models here.
class Gallery(models.Model):
	CATEGORY = 	(
		('men', 'Men',),
		('women', 'Women',),
		('boys', 'Boys',),
		('girls', 'Girls',),
	)
	picture = models.ImageField(upload_to='gallery/')
	caption = models.TextField(blank=True)
	category = models.CharField(choices=CATEGORY, max_length=10)
	created = models.DateTimeField(auto_now_add=True)

	@property
	def name(self):
		return self.picture.name.split('/')[1]

	@property
	def name_short(self):
		ellipsis = ''
		if len(self.name) > 15:
			ellipsis = '...'
		return self.name[:15]+ellipsis

	def get_absolute_url(self):
		return reverse('update_gallery', kwargs={'id': self.id})
	