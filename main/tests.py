from unicodedata import category, name
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



class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        # Creating a new Location and saving it
        self.new_location= Location(id=1, name='Nairobi')
        self.new_location.save()

        # Creating a new Category and saving it
        self.gardens = Category(id=1, title='First Garden')
        self.gardens.save()

        # Creating a new image and saving it
        self.new_image = Image(id=1, name="Image", description="Image Description", location=self.new_location, category=self.gardens)
        self.new_image.save()

    
    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()

    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image, Image))
    

    def test_save_method(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
    

    def test_delete_method(self):
        self.new_image.delete()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)
    
    def test_update_method(self):
        self.new_image.name = 'New Image'
        self.new_image.save_image()
        self.assertEqual(self.new_image.name, 'New Image')
        

    def test_filter_by_location(self):
        self.image = Image.objects.get(location=self.new_location)

        self.assertEqual(self.image.name, 'Image')

    
    def test_get_image_by_id(self):
        self.image = Image.objects.get(id=1)

        self.assertEqual(self.image.name, 'Image')


    
    def test_search_image_category(self):
        pass