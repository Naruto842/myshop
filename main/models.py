from django.db import models

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(max_length=3000)
	price = models.IntegerField('Цена')
	# img = models.ImageField(upload_to='product')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Продукт'
		verbose_name_plural = 'Продукты'
