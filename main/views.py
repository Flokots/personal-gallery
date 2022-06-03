from django.shortcuts import render
from .models import Category, Location, Image

# Create your views here.
def home(request):
    title = 'Home'
    categories = Category.objects.all()
    locations = Location.objects.all()
    images = Image.objects.all()

    return render(request, 'base-templates/index.html', {"title":title, "categories": categories, "locations": locations, "images": images})


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


def category_image_detail(request, slug1, slug2):
    
    category = Category.objects.get(slug=slug1)
    image = Image.objects.get(slug=slug2)
    title = f'{Image.name} Details Page'
    return render(request, 'base-templates/image.html', {"category": category, "image": image, "title":title})


def location_image_detail(request, slug1, slug2):
    location = Location.objects.get(slug=slug1)
    image = Image.objects.get(slug=slug2)
    title = f'{Image.name} Details Page'
    return render(request, 'base-templates/image.html', {"location": location, "image": image, "title":title})


def search_results(request):
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get("category")
        searched_categories = Category.search_by_category(search_term)
        category=searched_categories[:1]
        images = Image.objects.filter(category=category).order_by('-date_created')

        message = f"{search_term}"

        return render(request, "base-templates/search.html", {"message":message, "images": images, "categories": searched_categories,})
    else:
        message = "You haven't searched for any term"
        return render(request, 'base-templates/search.html', {"message": message})
