from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=300)

    image = models.ImageField(upload_to='category-image/', blank=True, null=True)
    caption = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name    = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category')

    name = models.CharField(max_length=200,)
    product_model = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=300)
    description = models.TextField()

    guarentee = models.CharField(max_length=200, blank=True, null=True, verbose_name="Kafolat: ")

    delivery_uzb = models.BooleanField(default=False)
    delivery_toshkent = models.BooleanField(default=False)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Maxsulot"
        verbose_name_plural="Maxsulotlar"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_image")

    image = models.ImageField(upload_to="product-image/")
    caption = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return str(self.pk)
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url