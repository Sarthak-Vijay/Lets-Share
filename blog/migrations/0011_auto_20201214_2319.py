# Generated by Django 3.1 on 2020-12-14 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20201214_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='userPerson',
        ),
        migrations.AddField(
            model_name='post',
            name='profile_id',
            field=models.IntegerField(default=0),
        ),
    ]
