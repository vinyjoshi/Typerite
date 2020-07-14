# Generated by Django 3.0.7 on 2020-07-14 05:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('tag', models.CharField(max_length=100)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('time', models.TimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('video', models.FileField(blank=True, upload_to='videos/%Y/%m/%d/')),
            ],
        ),
    ]