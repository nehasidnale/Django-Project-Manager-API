
from rest_framework import viewsets
from api.models import Client, Project, ProjectUsers
from api.serializers import ClientSerializer, ProjectSerializer, ProjectUsersSerializer

# Create your views here.
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
class ProjectUserViewSet(viewsets.ModelViewSet):
    queryset = ProjectUsers.objects.all()
    serializer_class = ProjectUsersSerializer