from argparse import BooleanOptionalAction
from django.db import models
from django.template.defaultfilters import slugify
from django_resized import ResizedImageField
from django.utils import timezone
from uuid import uuid4
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    title = models.CharField(null=True, blank=True, max_length=200)

    #utility variable
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.title, self.uniqueId)
    
    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.title, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(Category, self).save(*args, **kwargs)

class Location(models.Model):
    name = models.CharField(null=True, blank=True, max_length=30)

    def save_location(self):
        self.save()
    
    def delete_location(self):
        self.delete()
    
    
    
