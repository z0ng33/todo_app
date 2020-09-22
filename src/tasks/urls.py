from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'tasks_lists', views.TasksListsViewSet, 'tasks_lists')

urlpatterns = router.urls
