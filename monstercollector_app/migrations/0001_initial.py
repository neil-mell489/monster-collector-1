# Generated by Django 4.2.13 on 2024-05-13 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('level', models.IntegerField(max_length=100)),
                ('attribute', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('lore', models.TextField(max_length=400)),
            ],
        ),
    ]
