from django.db import models

# Create your models here.


class Place(models.Model):
	'''
	 Creating table in database with textfield name and boolean field visited.
	'''
	name = models.CharField(max_length=200)
	visited = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.name}, visited? {self.visited}'
