from rest_framework import serializers
from .models import Client, Project, ProjectUsers


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        

class ProjectUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectUsers
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'