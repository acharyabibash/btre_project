from django.db import models

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank =True)
    title = models.IntegerField()
    bedrooms = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2,decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IPAddressField()
    lot_size = models.DecimalField(max_digits=5)