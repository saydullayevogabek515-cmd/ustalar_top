from django.urls import path, include
from .views import MasterProfileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'masterprofile', MasterProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]