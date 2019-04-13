from rest_framework import routers
from automation.viewsets import AutomationViewSet


router = routers.DefaultRouter
router.register(r'automation', AutomationViewSet)