from django.db import models
from django.conf import settings

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Jobs(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    modelName = models.CharField(max_length=50)
    training_data_path = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

