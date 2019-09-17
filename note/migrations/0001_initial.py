# Generated by Django 2.2.5 on 2019-09-17 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('content_html', models.TextField()),
                ('content_editor', models.TextField()),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('classify', models.CharField(max_length=255)),
                ('mold', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
