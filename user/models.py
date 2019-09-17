from django.db import models
# ****** 引入其他模块的对象 ********
# from home.models import Sex
# from home.models import Icon
# from course.models import Course
# **********************************

# Create your models here.

class User(models.Model):
    tel = models.CharField(max_length=11,unique=True,null=False)
    email = models.CharField(max_length=255,null=True)
    psw = models.CharField(max_length=255,null=False)
    register_time = models.DateTimeField(auto_now_add=True)


class UserInfo(models.Model):
    user_name = models.CharField(max_length=255,unique=True)
    user_icon = models.ForeignKey(to='home.Icon',to_field='id',default=1,on_delete=models.CASCADE,null=True)
    user_sex = models.ForeignKey(to='home.Sex',to_field='id',default=1,on_delete=models.CASCADE,null=True)
    identity = models.CharField(max_length=255,null=True)
    address = models.CharField(max_length=255,null=True)
    introduce = models.CharField(max_length=255,null=True)
    user = models.ForeignKey(to='User',to_field='id',default=1,on_delete=models.CASCADE,null=False)

class UserIntegral(models.Model):
    integral = models.IntegerField(null=False)
    user = models.ForeignKey(to='User', to_field='id', default=1, on_delete=models.CASCADE, null=False)
    get_date = models.DateTimeField(auto_now_add=True,null=False)

class CheckIn(models.Model):
    check_date = models.DateTimeField(auto_now_add=True,null=False)
    user = models.ForeignKey(to='User',to_field='id',default=1,on_delete=models.CASCADE,null=False)

class Collection(models.Model):
    user = models.ForeignKey(to='User',to_field='id',default=1,on_delete=models.CASCADE,null=False)
    course = models.ForeignKey(to='course.Course',to_field='id',default=1,on_delete=models.CASCADE,null=False)
    col_date = models.DateTimeField(auto_now_add=True)

class SelectCourse(models.Model):
    user = models.ForeignKey(to='User', to_field='id', default=1, on_delete=models.CASCADE, null=False)
    course = models.ForeignKey(to='course.Course', to_field='id', default=1, on_delete=models.CASCADE, null=False)
    sc_date = models.DateTimeField(auto_now_add=True)
    iscomplete = models.IntegerField(null=False,default=0)

class CourseEvaluation(models.Model):
    content = models.TextField(null=False)
    course = models.ForeignKey(to='course.Course', to_field='id', default=1, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(to='User', to_field='id', default=1, on_delete=models.CASCADE, null=False)
    eva_date = models.DateTimeField(auto_now_add=True)

