from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('monsters/', views.monster_index, name='index'),
    path('monster/<int:monster_id>/', views.monster_detail, name='detail'),
    path('monsters/create/', views.MonsterCreate.as_view(), name='monsters_create'),
    path('monsters/<int:pk>/update/', views.MonsterUpdate.as_view(), name='monsters_update'),
    path('monsters/<int:pk>/delete/', views.MonsterDelete.as_view(), name='monsters_delete'),
]
