from django.db import models

# Create your models here.
class Sex(models.Model):
    sex_name = models.CharField(max_length=255,unique=True,null=False)

class Icon(models.Model):
    icon_img = models.CharField(max_length=255,unique=True,null=False)