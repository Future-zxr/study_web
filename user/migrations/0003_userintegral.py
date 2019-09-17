# Generated by Django 2.2.5 on 2019-09-17 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190917_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserIntegral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('integral', models.IntegerField()),
                ('get_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
    ]
