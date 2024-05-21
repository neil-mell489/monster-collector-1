from django.db import models
from django.urls import reverse


# Duel scheduling breakdown

DUELS = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('N', 'Night'),
)



# Create your models here.
class Monster(models.Model):
    name = models.CharField(max_length=100) 
    level = models.IntegerField()  
    attribute = models.CharField(max_length=100) 
    type = models.CharField(max_length=100)  
    lore = models.TextField(max_length=400) 


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'monster_id': self.id})
    
class Battle(models.Model):
    date = models.DateField()
    time = models.TimeField(
        max_length=1,
        choices=DUELS,
        default=DUELS[0][0]
    )

    monster = models.ForeignKey(Monster, on_delete=models.CASCADE)
   
    def __str__(self):
       
        return f"{self.get_battle_display()} on {self.date}"