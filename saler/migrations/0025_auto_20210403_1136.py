# Generated by Django 3.0.7 on 2021-04-03 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0024_auto_20210403_1050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='is_featured',
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_featured',
        ),
        migrations.RemoveField(
            model_name='product',
            name='last_visit',
        ),
        migrations.RemoveField(
            model_name='product',
            name='num_visits',
        ),
    ]