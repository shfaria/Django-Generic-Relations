from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

class Activity(models.Model):
    FAV = 'Favorite'
    LIK = 'Like'
    UP = 'Up Vote'
    DOWN = 'Down Vote'
    ACTIVITY_TYPES = (
        ('Favorite', 'Favorite'),
        ('Like', 'Like'),
        ('Up Vote', 'Up Vote'),
        ('Down Vote', 'Down Vote'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    acttivity_type = models.CharField(max_length=15, choices=ACTIVITY_TYPES)
    date = models.DateTimeField(auto_now_add=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self) -> str:
        return self.user.username + " -- " + self.acttivity_type

class Post(models.Model):
    text = models.CharField(max_length=1000, null=True, blank=True)
    likes = GenericRelation(Activity)

    def __str__(self) -> str:
        return self.text

class Question(models.Model):
    text = models.CharField(max_length=1000, null=True, blank=True)
    activities = GenericRelation(Activity)

    def __str__(self) -> str:
        return self.text

class Answer(models.Model):
    text = models.CharField(max_length=1000, null=True, blank=True)
    vote = GenericRelation(Activity)

    def __str__(self) -> str:
        return self.text

class Comment(models.Model):
    text = models.CharField(max_length=1000, null=True, blank=True)
    likes = GenericRelation(Activity, related_query_name='comments')

    def __str__(self) -> str:
        return self.text
