
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    CategoryViewSet,
    FoodViewSet,
    ContactViewSet,
    home,
    about,
    menu,
    gallery,
    food_category
)

router = DefaultRouter()

router.register('categories', CategoryViewSet)
router.register('foods', FoodViewSet)
router.register('contacts', ContactViewSet)

urlpatterns = [
    # Website Pages
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('menu/', menu, name='menu'),
    path('gallery/', gallery, name='gallery'),
    path('food-category/<int:category_id>/', food_category, name='food_category'),

    # REST API
    path('', include(router.urls)),
]
