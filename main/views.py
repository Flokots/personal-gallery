from django.shortcuts import render
from .models import Category, Location, Image

# Create your views here.
def home(request):
    title = 'Home'
    categories = Category.objects.all()
    locations = Location.objects.all()

    return render(request, 'base-templates/index.html', {"title":title, "categories": categories, "locations": locations})


def category_page(request, slug):

    category = Category.objects.get(slug=slug)
    images = Image.objects.filter(category=category)
   
    return render(request, '', {"images": images, "category":category})


def location_page(request, slug):
    location = Location.objects.get(slug=slug)
    images = Image.objects.filter(location=location)

    return render(request, '', {"location": location, "images": images})