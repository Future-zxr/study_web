from django.db import models
# ****** 引入其他模块的对象 ********
# from user.models import User
# **********************************
# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=255,null=False,unique=True)
    content_html = models.TextField(null=False)
    content_editor = models.TextField(null=False)
    publish_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to='user.User', to_field='id', default=1, on_delete=models.CASCADE, null=False)
    classify = models.CharField(max_length=255,null=False)
    mold = models.CharField(max_length=255,null=True)
