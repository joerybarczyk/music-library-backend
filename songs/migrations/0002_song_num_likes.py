# Generated by Django 4.0.4 on 2022-04-25 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='num_likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
