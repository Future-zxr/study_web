from django.db import models
# ****** 引入其他模块的对象 ********
# from course.models import Course
# **********************************

# Create your models here.
class Chapter(models.Model):
    name = models.CharField(max_length=255,null=False)
    introduce = models.TextField(null=True)
    course = models.ForeignKey(to='course.Course',to_field='id',default=1,on_delete=models.CASCADE,null=False)