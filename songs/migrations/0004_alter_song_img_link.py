# Generated by Django 4.0.4 on 2022-04-25 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0003_song_img_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='img_link',
            field=models.CharField(default='none', max_length=255),
        ),
    ]