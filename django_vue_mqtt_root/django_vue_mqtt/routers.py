from rest_framework import routers
from task.viewsets import TaskViewSet


router = routers.DefaultRouter()

router.register(r'tasks', TaskViewSet)