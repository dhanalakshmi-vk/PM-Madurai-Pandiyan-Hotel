from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    CategoryViewSet,
    FoodViewSet,
    ContactViewSet
)

router = DefaultRouter()

router.register('categories', CategoryViewSet)
router.register('foods', FoodViewSet)
router.register('contacts', ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),
]