from django.db import models

from petstagram.photos.models import Photo


class Comment(models.Model):
    class Meta:
        ordering = ['-comment_date']

    text = models.CharField(max_length=300)
    comment_date = models.DateTimeField(auto_now_add=True)
    commented_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)


class Like(models.Model):
    liked_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
