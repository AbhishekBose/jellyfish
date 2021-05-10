# Generated by Django 3.2.1 on 2021-05-10 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0002_rename_trainer_jobs_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='job_status',
            field=models.CharField(choices=[('ID', 'Idle'), ('PD', 'Pending'), ('FI', 'Finished')], default='ID', max_length=2),
        ),
    ]