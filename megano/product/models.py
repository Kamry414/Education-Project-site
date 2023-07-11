from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField()
    date = models.DateField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    fullDescription = models.TextField()
    freeDelivery = models.BooleanField(default=False)
    images = models.TextField()
    tags = models.TextField()
    reviews = models.TextField()
    specifications = models.TextField()
    rating = models.FloatField()

    def __str__(self):
        return self.title




class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_popular = models.BooleanField(default=False)
    is_limited = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    discount = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} ({self.discount}%)"


class Banner(models.Model):
    image_url = models.URLField()
    caption = models.CharField(max_length=100)

    def __str__(self):
        return self.caption



class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
