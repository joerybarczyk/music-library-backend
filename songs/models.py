from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    release_date = models.DateField()
    genre = models.CharField(max_length=255)
    num_likes = models.PositiveIntegerField(default=0)
    img_link = models.CharField(max_length=255, default="none")

    def __str__(self):
        return f"{self.artist}- {self.title}"