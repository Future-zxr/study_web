from django.db import models
# ****** 引入其他模块的对象 ********
# from home.models import Sex
# from home.models import Icon
# **********************************

# Create your models here.
class Direction(models.Model):
    name = models.CharField(max_length=255,null=False,unique=True)

class Classify(models.Model):
    name = models.CharField(max_length=255,null=False,unique=True)
    direction = models.ForeignKey(to='Direction',to_field='id',default=1,on_delete=models.CASCADE,null=False)

class Difficulty(models.Model):
    name = models.CharField(max_length=255,null=False,unique=True)

class Course(models.Model):
    name = models.CharField(max_length=255,null=False,unique=True)
    introduce = models.TextField(null=True)
    notice = models.TextField(null=True)
    course_icon = models.CharField(max_length=255,null=False)
    integral = models.IntegerField(default=0,null=True)
    publist_tiem = models.DateTimeField(auto_now_add=True)
    classify = models.ForeignKey(to='Classify',to_field='id',default=1,on_delete=models.CASCADE,null=False)
    difficulty = models.ForeignKey(to='Difficulty',to_field='id',default=1,on_delete=models.CASCADE,null=False)
    teacher = models.ForeignKey(to='Teacher',to_field='id',default=1,on_delete=models.CASCADE,null=False)
    pre_course = models.ForeignKey(to='Course',to_field='id',default=1,on_delete=models.CASCADE,null=False)

class TeacherIdentity(models.Model):
    identity = models.CharField(max_length=255,null=False,unique=True)

class Teacher(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True)
    introduce = models.TextField(null=True)
    teacher_icon = models.ForeignKey(to='home.Icon',to_field='id',default=1,on_delete=models.CASCADE,null=True)
    teacher_sex = models.ForeignKey(to='home.Sex',to_field='id',default=1,on_delete=models.CASCADE,null=True)
    identity = models.ForeignKey(to='TeacherIdentity',to_field='id',default=1,on_delete=models.CASCADE,null=True)

