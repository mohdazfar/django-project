from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class vat_info(models.Model):
    country_id = models.CharField(max_length=2)
    country_vat = models.FloatField(validators = [MinValueValidator(0.0), MaxValueValidator(1.0)])

    def __str__(self):
        return self.country_id

class products(models.Model):
    item_id = models.CharField(max_length=20)
    item_name = models.CharField(max_length=255)
    item_price = models.FloatField(validators = [MinValueValidator(0.0)])
    manufacturing_country = models.ForeignKey(vat_info, on_delete=  models.CASCADE, default='')

    def __str__(self):
        return self.item_name





