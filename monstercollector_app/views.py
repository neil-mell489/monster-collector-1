import uuid
import os
import boto3
from django.shortcuts import render, redirect
from .models import Monster, Powerup, Photo
from .forms import BattleForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    return render(request, 'monsters/home.html')

def about(request):
    return render(request, 'monsters/about.html')

@login_required
def monsters_index(request):
    monsters = Monster.objects.filter(user=request.user)
    return render(request, 'monsters/index.html', {
        'monsters': monsters
    })

# Monster Detail
@login_required
def monsters_detail(request, monster_id):
    monster = Monster.objects.get(id=monster_id)
    powerups = Powerup
    id_list = monster.powerups.all().values_list('id')
    powerups_monster_doesnt_have = Powerup.objects.exclude(id__in=id_list)
    battle_form = BattleForm()
    return render(request, 'monsters/detail.html', {
        'monster': monster,
        'battle_form': battle_form,
        'powerups': powerups_monster_doesnt_have
    })

@login_required
def add_battle(request, pk):
    form = BattleForm(request.POST)
    if form.is_valid():
        new_battle = form.save(commit=False)
        new_battle.monster_id = pk
        new_battle.save()
    return redirect('detail', monster_id=pk)

@login_required
def assoc_powerup(request, pk, powerup_pk):
    Monster.objects.get(id=pk).powerups.add(powerup_pk)
    return redirect('detail', monster_id=pk)

@login_required
def assoc_delete(request, pk, powerup_pk):
    Monster.objects.get(id=pk).powerups.remove(powerup_pk)
    return redirect('detail', monster_id=pk)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

@login_required
def add_photo(request, monster_pk):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, monster_id=monster_pk)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', monster_id=monster_pk)

class MonsterCreate(LoginRequiredMixin, CreateView):
    model = Monster
    fields = ['name', 'level', 'attribute', 'type', 'lore']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MonsterUpdate(LoginRequiredMixin, UpdateView):
    model = Monster
    fields = ['level', 'attribute', 'type', 'lore']

class MonsterDelete(LoginRequiredMixin, DeleteView):
    model = Monster
    success_url = '/monsters/'

class PowerupList(LoginRequiredMixin, ListView):
    model = Powerup

class PowerupDetail(LoginRequiredMixin, DetailView):
    model = Powerup

class PowerupCreate(LoginRequiredMixin, CreateView):
    model = Powerup
    fields = '__all__'

class PowerupUpdate(LoginRequiredMixin, UpdateView):
    model = Powerup
    fields = ['name', 'color']

class PowerupDelete(LoginRequiredMixin, DeleteView):
    model = Powerup
    success_url = '/powerups'
