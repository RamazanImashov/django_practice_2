from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import TaskView, CommentView, ProjectView

router = DefaultRouter()
router.register('comments', CommentView)
router.register('tasks', TaskView)
router.register('projects', ProjectView)


urlpatterns = [
    path('main/', include(router.urls)),
]

