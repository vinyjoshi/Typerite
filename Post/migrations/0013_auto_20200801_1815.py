# Generated by Django 3.0.8 on 2020-08-01 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0012_auto_20200801_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='Date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
