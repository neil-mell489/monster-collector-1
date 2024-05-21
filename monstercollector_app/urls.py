from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('monsters/', views.monster_index, name='index'),
    path('monster/<int:monster_id>/', views.monster_detail, name='detail')
]
