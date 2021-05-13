from django.db import models
from django.conf import settings

from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()
# Create your models here.

class Jobs(models.Model):
    
    class JobStatus(models.TextChoices):
        IDLE = 'ID', _('Idle')
        INITIATED = "INIT", _('Initiated')
        PENDING = 'PD', _('Pending')
        STARTED = "ST", _('Started')
        FINISHED = 'FI', _('Finished')
        

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    modelName = models.CharField(max_length=50)
    training_data_path = models.CharField(max_length=200)
    job_status = models.CharField(max_length=4,
                choices=JobStatus.choices,
                default=JobStatus.IDLE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


