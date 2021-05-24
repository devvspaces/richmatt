from django.db import models
from django.urls import reverse


class Product(models.Model):
	CATEGORY = 	(
		('men', 'Men',),
		('women', 'Ladies',),
		('boys', 'Boys',),
		('girls', 'Girls',),
	)
	name = models.CharField(max_length=40)
	category = models.CharField(choices=CATEGORY, max_length=10)
	picture = models.ImageField(upload_to='products/')
	old_price = models.FloatField()
	new_price = models.FloatField()
	created = models.DateTimeField(auto_now_add=True)

	def get_absolute_url(self):
		return reverse('update_product', kwargs={'id': self.id})