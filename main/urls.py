from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns=[
    re_path(r'^$', views.home, name='home'),
    re_path(r'^/category/<slug:slug>$', views.category_page, name='image-category'),
    re_path(r'^/location/<slug:slug>$', views.location_page, name='image-location'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
