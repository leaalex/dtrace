# Generated by Django 2.0.7 on 2018-07-19 09:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isle', '0021_auto_20180719_0253'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventonlymaterial',
            name='owners',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='eventteammaterial',
            name='owners',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
