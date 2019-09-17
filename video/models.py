from django.db import models
# ****** 引入其他模块的对象 ********
# from courseDetails.models import Chapter
# from user.models import User
# **********************************
# Create your models here.

class Video(models.Model):
    name = models.CharField(max_length=255, null=False)
    video_src = models.CharField(max_length=255, null=False)
    video_time = models.TimeField(null=False)
    chapter = models.ForeignKey(to='courseDetails.Chapter', to_field='id', default=1, on_delete=models.CASCADE, null=False)

class QuestionVideo(models.Model):
    content = models.TextField(null=False)
    video = models.ForeignKey(to='Video', to_field='id', default=1, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(to='user.User', to_field='id', default=1, on_delete=models.CASCADE, null=False)
    question_video = models.ForeignKey(to='QuestionVideo', to_field='id', default=1,on_delete=models.CASCADE, null=True)
    qv_date = models.DateTimeField(auto_now_add=True)

class UserVideo(models.Model):
    progress = models.TextField(null=False)
    video = models.ForeignKey(to='Video', to_field='id', default=1, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(to='user.User', to_field='id', default=1, on_delete=models.CASCADE, null=False)