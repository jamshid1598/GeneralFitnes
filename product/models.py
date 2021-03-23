from django.db import models

# Create your models here.


class Category(models.Model):
    image = models.ImageField(upload_to='category-image/', blank=True, null=True)

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

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Maxsulot"
        verbose_name_plural="Maxsulotlar"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_image")

    image = models.ImageField(upload_to="product-image/")
    caption = models.CharField(max_length=300)

    def __str__(self):
        return self.pk
    