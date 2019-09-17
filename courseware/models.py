from django.db import models
# ****** 引入其他模块的对象 ********
# from courseDetails.models import Chapter
# from user.models import User
# **********************************
# Create your models here.
class Courseware(models.Model):
    name = models.CharField(max_length=255,null=False)
    content = models.TextField(null=True)
    courseware_time = models.TimeField(null=False)
    chapter = models.ForeignKey(to='courseDetails.Chapter',to_field='id',default=1,on_delete=models.CASCADE,null=False)


class QuestionCourseware(models.Model):
    content = models.TextField(null=False)
    courseware = models.ForeignKey(to='Courseware',to_field='id',default=1,on_delete=models.CASCADE,null=False)
    user = models.ForeignKey(to='user.User',to_field='id',default=1,on_delete=models.CASCADE,null=False)
    question_courseware = models.ForeignKey(to='QuestionCourseware',to_field='id',default=1,on_delete=models.CASCADE,null=True)
    qc_date = models.DateTimeField(auto_now_add=True)

class UserCourseware(models.Model):
    iswatch = models.IntegerField(null=False,default=0)
    courseware = models.ForeignKey(to='Courseware', to_field='id', default=1, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(to='user.User', to_field='id', default=1, on_delete=models.CASCADE, null=False)