# Generated by Django 3.1.5 on 2021-04-13 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_details_logindetails_userdetailsfb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='emailId',
        ),
        migrations.RemoveField(
            model_name='details',
            name='password',
        ),
        migrations.RemoveField(
            model_name='details',
            name='username',
        ),
    ]
