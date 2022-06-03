from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('category/<slug:slug>', views.category_page, name='image-category'),
    path('location/<slug:slug>', views.location_page, name='image-location'),
    path('search/', views.search_results, name='search_results'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
