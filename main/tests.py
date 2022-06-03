from unicodedata import name
from django.test import TestCase
from .models import Category, Location, Image

# Create your tests here.

class CategoryTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.gardens = Category(id=1, title='First Garden')

    def tearDown(self):
        Category.objects.all().delete()

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.gardens, Category))

    # Testing save method
    def test_save_method(self):
        self.gardens.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    
    def test_delete_method(self):
        self.gardens.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)
    

    def test_update_category(self):
        self.gardens.title = 'New Garden'
        self.gardens.save_category()
        self.assertEqual(self.gardens.title, 'New Garden')

    
class LocationTestClass(TestCase):
        #Set up method
    def setUp(self):
        # Creating a new Location and saving it
        self.new_location= Location(id=1, name='Nairobi')
        
    def tearDown(self):
        Location.objects.all().delete()

        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_location, Location))

        
    def test_save_location(self):
        self.new_location.save_location()
        locations=Location.objects.all()
        self.assertTrue(len(locations) > 0)
    

    def test_delete_location(self):
        self.new_location.delete_location()
        locations=Location.objects.all()
        self.assertTrue(len(locations) == 0)
    
    def test_update_location(self):
        self.new_location.name = 'Kisumu'
        self.new_location.save_location()
        self.assertEqual(self.new_location.name, 'Kisumu')



