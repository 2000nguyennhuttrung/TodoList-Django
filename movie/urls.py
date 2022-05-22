from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("tasks", views.TaskViewSet, "task")
# router.register("movies", views.MovieViewSet, "movie")
# router.register("movie-des", views.MovieDescriptionViewSet, "movie-des")


urlpatterns = [
    path('', include(router.urls)),
    path('tasks/<str:pk>', views.TaskDetailViewSet.as_view(), name='task-detail'),
]
