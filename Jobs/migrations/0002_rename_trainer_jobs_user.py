# Generated by Django 3.2.1 on 2021-05-07 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobs',
            old_name='trainer',
            new_name='user',
        ),
    ]
