from django.db import models


class Category(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255, unique=True)
    parent = models.ForeignKey('self', related_name='sub_categories', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255, unique=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    description = models.CharField(max_length=1024)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name
