# Generated by Django 3.0.8 on 2020-07-29 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0006_auto_20200729_1355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='Photo1',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='Photo2',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='Thumbnail',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='Video',
        ),
    ]
