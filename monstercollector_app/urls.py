from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('monsters/', views.monsters_index, name='index'),
    
    path('monsters/<int:monster_id>/', views.monsters_detail, name='detail'),
    path('monsters/create/', views.MonsterCreate.as_view(), name='monsters_create'),
    path('monsters/<int:pk>/update/', views.MonsterUpdate.as_view(), name='monsters_update'),
    path('monsters/<int:pk>/delete/', views.MonsterDelete.as_view(), name='monsters_delete'),

    path('monsters/<int:pk>/add_battle', views.add_battle, name='add_battle'),
    path('monsters/<int:pk>/assoc_powerup/<int:powerup_pk>', views.assoc_powerup, name='assoc_powerup'),
    path('monsters/<int:pk>/assoc_delete/<int:powerup_pk>', views.assoc_delete, name='assoc_delete'),

    path('monsters/<int:monster_pk>/add_photo', views.add_photo, name='add_photo'),

    path('powerups/', views.PowerupList.as_view(), name='powerups_index'),
    path('powerups/<int:pk>/', views.PowerupDetail.as_view(), name='powerups_detail'),
    path('powerups/create/', views.PowerupCreate.as_view(), name='powerups_create'),
    path('powerups/<int:pk>/update/', views.PowerupUpdate.as_view(), name='powerups_update'),
    path('powerups/<int:pk>/delete/', views.PowerupDelete.as_view(), name='powerups_delete'),

    path('accounts/signup', views.signup, name='signup'),
]
