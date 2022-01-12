from django.db import models

# Create your models here.

class Product_Beato(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    cost_per_item = models.IntegerField()
    stock_quantity = models.IntegerField()
    volume = models.IntegerField()


    def quantity(self):
        if(self.cost_per_item != None):
            quan = (self.cost_per_item*self.stock_quantity)
            return quan
