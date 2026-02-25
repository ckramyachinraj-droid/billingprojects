from django.db import models

# Product Table
class Product(models.Model):
    name = models.CharField(max_length=100)
    product_id = models.CharField(max_length=20, unique=True)
    stock = models.IntegerField()
    price = models.FloatField()
    tax = models.FloatField()   # percentage

    def __str__(self):
        return self.name

# Bill Main Table
class Bill(models.Model):
    customer_email = models.EmailField()
    total_amount = models.FloatField(default=0)
    paid_amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)


# Each product inside bill
class BillItem(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    subtotal = models.FloatField()

