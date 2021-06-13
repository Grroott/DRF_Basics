from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    ELECTRONICS = 'ELECTRONICS'
    FROZEN_FOOD = 'FROZEN_FOOD'
    MEAT = 'MEAT'
    FRUITS = 'FRUITS'
    VEGETABLE = 'VEGETABLE'
    CANNED_GOODS = 'CANNED_GOODS'
    SNACKS = 'SNACKS'
    CEREAL = 'CEREAL'
    PERSONAL_CARE = 'PERSONAL_CARE'
    HOUSEHOLD_ITEMS = 'HOUSEHOLD_ITEMS'
    OTHERS = 'OTHERS'

    CATEGORY_CHOICES = [
        (ELECTRONICS, 'Electronic goods'),
        (FROZEN_FOOD, 'Frozen items'),
        (MEAT, 'Raw meat'),
        (FRUITS, 'Fruits'),
        (CANNED_GOODS, 'Canned goods'),
        (SNACKS, 'Snacks items'),
        (CEREAL, 'Cereals'),
        (PERSONAL_CARE, 'Personal care items'),
        (HOUSEHOLD_ITEMS, 'Day to day items'),
        (OTHERS, 'Other items')
    ]

    COUNT = 'COUNT'
    GRAM = 'GRAM'
    MILLI_GRAM = 'MILLI_GRAM'
    LITRE = 'LITRE'
    MILLI_LITRE = 'MILLI_LITRE'

    QUANTITY_TYPE_CHOICE = [
        (COUNT, 'Count of item'),
        (GRAM, 'Grams'),
        (MILLI_GRAM, 'Milli grams'),
        (LITRE, 'Litre'),
        (MILLI_LITRE, 'Milli litre')
    ]
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=OTHERS)
    cost_price = models.FloatField(null=False)
    selling_price = models.FloatField(null=False)
    profit = models.FloatField(default=None, null=True, blank=True)
    expiry_date = models.DateField(default=datetime.now() + timedelta(days=10000))
    quantity = models.IntegerField(null=False, default=1)
    quantity_type = models.CharField(max_length=20, choices=QUANTITY_TYPE_CHOICE, default=COUNT)
    created_date = models.DateTimeField(default=timezone.now)
    is_sold = models.BooleanField(default=False)
    brand = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name + str(" - Out of Stock") if self.is_sold else self.name + str(" - In Stock")

    def save(self, *args, **kwargs):
        self.profit = self.selling_price - self.cost_price
        return super(Product, self).save(*args, **kwargs)
