from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ProjectViewSet, ProjectUserViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'project-users', ProjectUserViewSet)

urlpatterns = router.urls