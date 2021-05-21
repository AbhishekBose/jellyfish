from django import forms

from .models import Jobs

class JobForm(forms.ModelForm):
    class Meta:
        model = Jobs

        fields = ['modelName','training_data_path']