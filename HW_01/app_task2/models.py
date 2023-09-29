from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'User: {self.name}<br>'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    prod_quant = models.IntegerField()
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Product: {self.name}, price: {self.price}<br>'


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Order # {self.pk}, total price: {self.total_price}<br>'

