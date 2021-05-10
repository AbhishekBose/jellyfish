from rest_framework import serializers
from .models import Jobs


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = "__all__"


class CreateJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = ('id', 'modelName', 'training_data_path')


class UpdateJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = ('id', 'modelName', 'training_data_path','job_status')