from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from task import views

router = routers.DefaultRouter()
router.register(r"tasks", views.TaskViewSet, basename="tasks")

urlpatterns = [
    path("", include(router.urls)),
    path("health/", views.health_check),
    path("admin/", admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]
