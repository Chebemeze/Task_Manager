from rest_framework import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register("tasks", TaskViewSet, basename= "task")

urlpatterns = router.urls