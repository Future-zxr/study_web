# Generated by Django 2.2.5 on 2019-09-17 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20190917_1951'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkin',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='course_id',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='courseevaluation',
            name='course_id',
        ),
        migrations.RemoveField(
            model_name='courseevaluation',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='selectcourse',
            name='course_id',
        ),
        migrations.RemoveField(
            model_name='selectcourse',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='user_id',
        ),
        migrations.AddField(
            model_name='checkin',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
        migrations.AddField(
            model_name='collection',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='course.Course'),
        ),
        migrations.AddField(
            model_name='collection',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
        migrations.AddField(
            model_name='courseevaluation',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='course.Course'),
        ),
        migrations.AddField(
            model_name='courseevaluation',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
        migrations.AddField(
            model_name='selectcourse',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='course.Course'),
        ),
        migrations.AddField(
            model_name='selectcourse',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
    ]
