# Generated by Django 2.0.7 on 2018-10-08 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isle', '0034_auto_20180928_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventtype',
            name='visible',
            field=models.BooleanField(default=True, verbose_name='Отображать в списке мероприятий'),
        ),
    ]