from django.db import models

# Create your models here.

class Players(models.Model):
    name = models.CharField(max_length=8)
    nickname = models.CharField(max_length=15, null=True, blank=True)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    birthday = models.DateField()
    line = models.CharField(max_length=100)
    ig = models.CharField(max_length=100, null=True, blank=True)
    fb = models.CharField(max_length=100, null=True, blank=True)
    photo_whole = models.CharField(max_length=150, null=True)
    photo_half = models.CharField(max_length=150, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name