from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length = 200)
    website = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class ShoeType(models.Model):
    style = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ShoeColor(models.Model):
    COLOR_CHOICES = [
        ('Red', 'Red'),
        ('Orange', 'Orange'),
        ('Yellow', 'Yellow'),
        ('Green', 'Green'),
        ('Blue', 'Blue'),
        ('Indigo', 'Indigo'),
        ('Violet', 'Violet'),
        ('White', 'White'),
        ('Black', 'Black')
    ]
    color = models.CharField(
        max_length = 6,
        choices = COLOR_CHOICES,
        default = 'Black'
    )

    def __str__(self):
        return self.name


class Shoe(models.Model):
    size = models.IntegerField()
    brand_name = models.CharField(max_length=200)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=200)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name