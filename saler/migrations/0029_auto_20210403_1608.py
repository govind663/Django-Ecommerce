# Generated by Django 3.0.7 on 2021-04-03 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0028_auto_20210403_1605'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='slug',
            new_name='sub_Categories',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='slug',
            new_name='subcategory',
        ),
        migrations.RemoveField(
            model_name='category',
            name='is_featured',
        ),
        migrations.RemoveField(
            model_name='category',
            name='parent',
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
        migrations.RemoveField(
            model_name='product',
            name='parent',
        ),
    ]
