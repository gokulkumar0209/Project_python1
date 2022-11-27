from django.db import models

# Create your models here.
class Product(models.Model):
	title=models.CharField(max_length=16)
	price=models.DecimalField(decimal_places=2,max_digits=10)
	description=models.TextField()


