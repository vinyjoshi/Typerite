# Generated by Django 3.0.7 on 2020-07-14 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='photo',
            new_name='Photo',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='photo1',
            new_name='Photo1',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='photo2',
            new_name='Photo2',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='tag',
            new_name='Tag',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='title',
            new_name='Title',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='video',
            new_name='Video',
        ),
        migrations.AddField(
            model_name='blog',
            name='Thumbnail',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
