# Generated by Django 2.2.5 on 2019-09-17 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classify',
            old_name='direction_id',
            new_name='direction',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='classify_id',
            new_name='classify',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='difficulty_id',
            new_name='difficulty',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='pre_course_id',
            new_name='pre_course',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='teacher_id',
            new_name='teacher',
        ),
    ]