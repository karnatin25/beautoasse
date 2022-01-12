from django.db import models

# Create your models here.

class Product_Beato(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    cost_per_item = models.IntegerField()
    stock_quantity = models.IntegerField()
    volume = models.IntegerField(blank= True)

    def save(self, *args, **kwargs):
        self.volume = self.cost_per_item * self.stock_quantity
        super(Product_Beato, self).save(*args, **kwargs)
        
    def quantity(self):
        if(self.cost_per_item != None):
            quan = (self.cost_per_item*self.stock_quantity)
            return quan
