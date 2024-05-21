from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Duel scheduling breakdown
DUELS = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('N', 'Night'),
)

class Powerup(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('powerups_detail', kwargs={'pk': self.id})

class Monster(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()
    attribute = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    lore = models.TextField(max_length=400)
    # M:M relationship!
    powerups = models.ManyToManyField(Powerup)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'monster_id': self.id})

class Battle(models.Model):
    date = models.DateField()
    time = models.CharField(
        max_length=1,
        choices=DUELS,
        default=DUELS[0][0]
    )
    monster = models.ForeignKey(Monster, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_time_display()} on {self.date}"

    class Meta:
        ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    monster = models.ForeignKey(Monster, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for monster_id: {self.monster_id} @{self.url}"
