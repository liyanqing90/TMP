# Generated by Django 3.0.8 on 2020-07-18 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200718_1432'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requirement',
            old_name='user',
            new_name='owner_id',
        ),
    ]
