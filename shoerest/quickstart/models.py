from django.db import models

class Manufacturer(models.Model):
    name =  models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name

class ShoeType(models.Model):
    style = models.CharField(max_length=6)

    def __str__(self):
        return self.style

class ShoeColor(models.Model):
    color_name = models.CharField(max_length=6)

    def __str__(self):
        return self.color_name

class Shoe(models.Model):
    size = models.IntegerField()
    brand_name = models.CharField(max_length=50, )
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=50)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=50)

    def __str__(self):
        return self.brand_name - self.size - self.manufacturer - self.color

    # Joe Kaufeld was born in the African Savannah and spent most of his childhood learning to ride on the backs of the local fauna.