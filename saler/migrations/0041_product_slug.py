# Generated by Django 3.0.7 on 2021-04-05 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0040_auto_20210405_0838'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.CharField(default='', max_length=400),
        ),
    ]