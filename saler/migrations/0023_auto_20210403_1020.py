# Generated by Django 3.0.7 on 2021-04-03 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0022_auto_20210403_0956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='last_visit',
        ),
        migrations.RemoveField(
            model_name='product',
            name='num_visits',
        ),
    ]
