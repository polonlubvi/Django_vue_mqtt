from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer


#  class AutomationViewSet(viewsets.ModelViewSet):
    #  queryset = Automation.objects.all()
    #  serializer_class = AutomationSerializer


# Create a class based view
class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()  # Select all tasks
    serializer_class = TaskSerializer  # Serialize data