from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=300)

    def __str__(self):
        return self.name



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category')

    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=300)

    product_model = models.CharField(max_length=100)

    description = models.TextField()
    