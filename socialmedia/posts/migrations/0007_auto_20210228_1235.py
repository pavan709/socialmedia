# Generated by Django 3.1.7 on 2021-02-28 07:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0006_auto_20210227_1326'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='post',
            unique_together={('user', 'message')},
        ),
    ]