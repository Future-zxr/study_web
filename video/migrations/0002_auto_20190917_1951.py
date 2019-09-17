# Generated by Django 2.2.5 on 2019-09-17 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190917_1951'),
        ('courseDetails', '0002_auto_20190917_1951'),
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionvideo',
            name='question_video_id',
        ),
        migrations.RemoveField(
            model_name='questionvideo',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='questionvideo',
            name='video_id',
        ),
        migrations.RemoveField(
            model_name='uservideo',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='uservideo',
            name='video_id',
        ),
        migrations.RemoveField(
            model_name='video',
            name='chapter_id',
        ),
        migrations.AddField(
            model_name='questionvideo',
            name='question_video',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='video.QuestionVideo'),
        ),
        migrations.AddField(
            model_name='questionvideo',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
        migrations.AddField(
            model_name='questionvideo',
            name='video',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='video.Video'),
        ),
        migrations.AddField(
            model_name='uservideo',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
        migrations.AddField(
            model_name='uservideo',
            name='video',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='video.Video'),
        ),
        migrations.AddField(
            model_name='video',
            name='chapter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='courseDetails.Chapter'),
        ),
    ]
