from django.db import models

# Create your models here.
class userinfo(models.Model):
    name = models.CharField(max_length=50)
    nickName = models.CharField(max_length=50)
    Birthyear = models.CharField(max_length=50)
    Bestfriend = models.CharField(max_length=50)
    Hobby = models.CharField(max_length=50)
    letter = models.CharField(max_length=50)
    goal = models.CharField(max_length=50)
    idx = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    