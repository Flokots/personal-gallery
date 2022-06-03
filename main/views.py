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
    title=f'{Category.title}'
    images = Image.objects.filter(category=category).order_by('-date_created')

    for x in images:
        x.shortDescription = x.description[:130]

   
    return render(request, 'base-templates/category.html', {"images": images, "category":category, "title":title})


def location_page(request, slug):
    location = Location.objects.get(slug=slug)
    title = f'{Location.name}'
    images = Image.objects.filter(location=location).order_by('-date_created')

    for x in images:
        x.shortDescription = x.description[:130]

    
    return render(request, 'base-templates/location.html', {"location": location, "images": images, "title":title})