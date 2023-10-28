from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet
from events.views import EventViewSet
from django.urls import path
from . import views

router = DefaultRouter()
router.register(r'events', EventViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
]
