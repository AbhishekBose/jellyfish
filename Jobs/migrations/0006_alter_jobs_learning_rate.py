# Generated by Django 3.2 on 2021-05-22 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0005_auto_20210522_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='learning_rate',
            field=models.DecimalField(decimal_places=5, default=0.0, max_digits=10),
        ),
    ]