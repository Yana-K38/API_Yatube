# Generated by Django 4.0.6 on 2022-07-20 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20220720_1148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='folowing',
            new_name='following',
        ),
    ]
