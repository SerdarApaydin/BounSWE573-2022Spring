from django.db import models

# Create your models here.

class Space(models.Model):
    name = models.CharField(max_length= 32 , null = False)
    description = models.CharField(max_length= 280 , null = True)
    date = models.DateTimeField(auto_now_add= True)
    spaceImage = models.ImageField(upload_to = "LearningSpaceImages")
