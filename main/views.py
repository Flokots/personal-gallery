from django.shortcuts import render
from .models import Category, Location, Image

# Create your views here.
def home(request):
    title = 'Home'
    categories = Category.objects.all()
    locations = Location.objects.all()

    return render(request, 'base-templates/index.html', {"title":title, "categories": categories, "locations": locations})


def category_page(request):
    return render(request, '', {})


def location_page(request):
    return render(request, '', {})