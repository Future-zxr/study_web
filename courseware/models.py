from django.db import models
# ****** 引入其他模块的对象 ********
from courseDetails.models import Chapter
from user.models import User
# **********************************
# Create your models here.
class Courseware(models.Model):
    pass

class QuestionCourseware(models.Model):
    pass

class UserCourseware(models.Model):
    pass