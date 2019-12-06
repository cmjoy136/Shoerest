from django.db import models

class Manufacturer(models.Model):
    name =  models.CharField(max_length=50)
    website = models.URLField()

class ShoeType(models.Model):
    style = models.CharField(max_length=6)

class ShoeColor(models.Model):
    color_name = models.CharField(max_length=6)

class Shoe(models.Model):
    size = models.IntegerField()
    brand_name = models.CharField(max_length=50, )
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=50)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=50)