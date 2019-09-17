from django.db import models
# ****** 引入其他模块的对象 ********
from home.models import Sex
from home.models import Icon
from course.models import Course
# **********************************

# Create your models here.


class UserIdentity(models.Model):
    pass

class User(models.Model):
    pass

class UserInfo(models.Model):
    pass

class UserIntegral(models.Model):
    pass

class CheckIn(models.Model):
    pass

class Collection(models.Model):
    pass

class SelectCourse(models.Model):
    pass

class CourseEvaluation(models.Model):
    pass

