from django.db import models


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    fullName = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    deliveryType = models.CharField(max_length=100)
    paymentType = models.CharField(max_length=100)
    totalCost = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    products = models.TextField()

    def __str__(self):
        return f"Order #{self.id}"


class BasketItem(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.PositiveIntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    freeDelivery = models.BooleanField(default=False)
    images = models.TextField()
    tags = models.TextField()
    reviews = models.PositiveIntegerField(default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.title
