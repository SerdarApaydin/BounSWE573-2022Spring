from django.db import models
from django.conf import settings
from django.forms import modelformset_factory
from django.utils import timezone
from space.models import Space


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateField(default=timezone.now)
    published_date = models.DateField(blank=True,null=True)
    space = models.ForeignKey(Space, on_delete=models.CASCADE)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self) :
        return self.title


class Answer(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    published_date = models.DateField(default=timezone.now)
