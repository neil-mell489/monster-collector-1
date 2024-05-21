from django.shortcuts import render
from django.http import HttpResponse
from .models import Monster
from django.views.generic.edit import CreateView, UpdateView, DeleteView

monsters = [
    {
     "name": "Blue-Eyes White Dragon", 
     "level": "8", 
     "attribute": "Light", 
     "type": "Dragon", 
     "lore": "This legendary dragon is a powerful engine of destruction. Virtually invincible, very few have faced this awesome creature and lived to tell the tale.", 
},

    {
     "name": "Dark Magician", 
     "level": "7", 
     "attribute": "Dark", 
     "type": "Spellcaster", 
     "lore": "The ultimate wizard in terms of attack and defense.", 
},

    {
     "name": "Kuriboh", 
     "level": "1", 
     "attribute": "Dark", 
     "type": "Fiend/Effect", 
     "lore": "During damage calculation, if your opponent's monster attacks (Quick Effect): You can discard this card; you take no battle damage from that battle.", 
},
]


# Create your views here.
def home(request):
    # return HttpResponse("hello")
    return render(request, 'monsters/home.html')

def about(request):
    return render(request, 'monsters/about.html')

def monsters_index(request):
    monsters = Monster.objects.all()
    return render(request, 'monsters/index.html', {
        'monsters': monsters
        })

def monster_detail(request, monster_id):
    monster = Monster.objects.get(id=monster_id)
    return render(request, 'monsters/detail.html', {'monster': monster})

class MonsterCreate(CreateView):
  model = Monster
  fields = ['name', 'level', 'attribute', 'type', 'lore']


class MonsterUpdate(UpdateView):
  model = Monster
  fields = ['level', 'attribute', 'type', 'lore']

class MonsterDelete(DeleteView):
  model = Monster
  success_url = '/monsters/'