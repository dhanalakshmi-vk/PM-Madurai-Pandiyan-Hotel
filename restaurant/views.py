from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Category, Food, Contact
from .serializers import (
    CategorySerializer,
    FoodSerializer,
    ContactSerializer
)


# API ViewSets

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


# Website Pages

def home(request):
    return render(request, 'restaurant/home.html')


def about(request):
    return render(request, 'restaurant/about.html')


def menu(request):
    categories = Category.objects.all()
    foods = Food.objects.all()

    context = {
        'categories': categories,
        'foods': foods,
    }

    return render(request, 'restaurant/menu.html', context)


def gallery(request):
    categories = Category.objects.all()
    foods = Food.objects.all()

    context = {
        'categories': categories,
        'foods': foods,
    }

    return render(request, 'restaurant/gallery.html', context)

def food_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    foods = Food.objects.filter(category=category)

    context = {
        'category': category,
        'foods': foods,
    }

    return render(request, 'restaurant/food_category.html', context)