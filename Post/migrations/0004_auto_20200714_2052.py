# Generated by Django 3.0.7 on 2020-07-14 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0003_auto_20200714_1956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='content',
            new_name='Content',
        ),
    ]
