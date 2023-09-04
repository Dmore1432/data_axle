from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'events', views.EventViewSet)
router.register(r'emaillogs', views.EmailLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

