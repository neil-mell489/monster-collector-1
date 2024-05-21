# Generated by Django 4.2.13 on 2024-05-21 09:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('monstercollector_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Powerup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='monster',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='monster',
            name='lore',
            field=models.TextField(max_length=400),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('monster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monstercollector_app.monster')),
            ],
        ),
        migrations.CreateModel(
            name='Battle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.CharField(choices=[('M', 'Morning'), ('A', 'Afternoon'), ('N', 'Night')], default='M', max_length=1)),
                ('monster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monstercollector_app.monster')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.AddField(
            model_name='monster',
            name='powerups',
            field=models.ManyToManyField(to='monstercollector_app.powerup'),
        ),
    ]
