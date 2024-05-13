from django.db import models

# Create your models here.
class Monster(models.Model):
    name = models.CharField(max_length=100) 
    level = models.IntegerField(max_length=100)  
    attribute = models.CharField(max_length=100) 
    type = models.CharField(max_length=100)  
    lore = models.TextField(max_length=400) 


    def __str__(self):
        return self.name