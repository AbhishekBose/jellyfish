from django import forms

from .models import Jobs

class JobForm(forms.ModelForm):
    class Meta:
        model = Jobs

        fields = ['modelName','model_type','learning_rate','epoch','classes','model_description']