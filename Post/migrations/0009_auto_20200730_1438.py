# Generated by Django 3.0.8 on 2020-07-30 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0008_auto_20200729_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='user_id',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
