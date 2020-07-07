from django.db import models

# Create your models here.

class Players(models.Model):
    active = models.BooleanField(default=False)
    name = models.CharField(max_length=8)
    nickname = models.CharField(max_length=15, null=True, blank=True)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    birthday = models.DateField()
    line = models.CharField(max_length=100)
    ig = models.CharField(max_length=100, null=True, blank=True)
    fb = models.CharField(max_length=100, null=True, blank=True)
    youtube = models.CharField(max_length=100, null=True, blank=True)
    photo_whole = models.CharField(max_length=150, null=True)
    photo_half = models.CharField(max_length=150, null=True)
    votes = models.PositiveIntegerField(default=0)
    video = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Voter(models.Model):
    user_id = models.CharField(max_length=30, unique_for_date="date")
    access_toke = models.CharField(max_length=255)
    date = models.DateField()
    vote_1 = models.PositiveSmallIntegerField()
    vote_2 = models.PositiveSmallIntegerField(null=True, blank=True)
    vote_3 = models.PositiveSmallIntegerField(null=True, blank=True)
    vote_4 = models.PositiveSmallIntegerField(null=True, blank=True)
    vote_5 = models.PositiveSmallIntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)