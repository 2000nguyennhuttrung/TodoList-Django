# Generated by Django 3.1.7 on 2022-05-20 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20220520_2346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='name',
            new_name='content',
        ),
    ]
