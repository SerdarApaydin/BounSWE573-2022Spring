from django.db import models

# Create your models here.

class Space(models.Model):
    name = models.CharField(max_length= 32 , null = False, unique=True)
    description = models.CharField(max_length= 280 , null = True)
    date = models.DateTimeField(auto_now_add= True)
    spaceImage = models.ImageField(upload_to = "space/images/learningSpaceThumb")

    def __str__(self):
        return self.name

class Tag(models.Model):
    description = models.CharField(max_length= 32, null=False)
    space = models.ForeignKey(Space, null= False, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

class LearningMaterials(models.Model):
    title = models.CharField(max_length= 128, null=False)
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
    sequence = models.IntegerField(null = False)
    material = models.FileField(upload_to = "space/materials")

    def __str__(self):
        return self.title