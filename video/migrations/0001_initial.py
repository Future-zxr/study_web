# Generated by Django 2.2.5 on 2019-09-17 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courseDetails', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('video_src', models.CharField(max_length=255)),
                ('video_time', models.TimeField()),
                ('chapter_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='courseDetails.Chapter')),
            ],
        ),
        migrations.CreateModel(
            name='UserVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress', models.TextField()),
                ('user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.User')),
                ('video_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='video.Video')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('qv_date', models.DateTimeField(auto_now_add=True)),
                ('question_video_id', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='video.QuestionVideo')),
                ('user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.User')),
                ('video_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='video.Video')),
            ],
        ),
    ]
