# Generated by Django 2.2.7 on 2020-01-07 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0003_auto_20200107_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='pub_date',
            field=models.DateTimeField(default='2020-01-01 06:00', verbose_name='Date published'),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='pub_date',
            field=models.DateTimeField(default='2020-01-01 06:00', verbose_name='Date published'),
        ),
    ]
