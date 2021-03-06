from django.db import models
from model_utils import Choices
from django.contrib.auth.models import User




# # for AUTH_USER_MODEL (Use this only if you are using a custome User model) check settings.py as well:
# from django.conf import settings 


# Create your models here.


# Product Categories : 
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    thumbnail = models.ImageField(blank=True, help_text="Optional, upload an image to assign it to the product category") # image galleries can be null
    parent = models.ForeignKey('self',blank=True, on_delete=models.PROTECT, null=True ,related_name='children') # when deleting the parent delete children as well

    class Meta:
        unique_together = ('slug', 'parent',)    #enforcing that there can not be two
        verbose_name_plural = "categories"       #categories under a parent with same 
                                                 #slug 

    def __str__(self):                           # __str__ method elaborated later in
        full_path = [self.name]                  # post.  use __unicode__ in place of
                                                 # __str__ if you are using python 2
        k = self.parent                          

        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])

# Product :
class Product(models.Model):
    title = models.CharField(max_length=120)
    summary = models.TextField()
    # description = HTMLField('Content', blank=True) # description can be null
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True) # when deleting the child protect the parent
    regular_price = models.PositiveIntegerField() #only positive numbers allowed
    discount_price = models.PositiveIntegerField(blank=True, null=True, help_text="Leave blank if there is no discount") #only positive numbers allowed can be null in case there was no discount
    discount_until = models.DateField(blank=True, null=True, help_text="Leave blank if there is no discount") #only positive numbers allowed can be null in case there was no discount
    thumbnail = models.ImageField(blank=True, help_text="This is main thumbnail")
    thumbnail_link = models.CharField(max_length=120, default=None, blank=True,) #set it to be null by default, unless a link is added
    image_1 = models.ImageField(blank=True, help_text="This is optional for more images of the product") # image galleries can be null
    image_1_link = models.CharField(max_length=120, default=None, blank=True,) #set it to be null by default, unless a link is added
    image_2 = models.ImageField(blank=True, help_text="This is optional for more images of the product") # image galleries can be null
    image_2_link = models.CharField(max_length=120, default=None, blank=True,) #set it to be null by default, unless a link is added
    image_3 = models.ImageField(blank=True, help_text="This is optional for more images of the product") # image galleries can be null
    image_3_link = models.CharField(max_length=120, default=None, blank=True,) #set it to be null by default, unless a link is added
    image_4 = models.ImageField(blank=True, help_text="This is optional for more images of the product") # image galleries can be null
    image_4_link = models.CharField(max_length=120, default=None, blank=True,) #set it to be null by default, unless a link is added
    sku = models.CharField(max_length=120)
    slug = models.SlugField(unique=True) #gives a unique slug for each product
    inventory =  models.PositiveIntegerField(default=5, help_text="By default this will be set to 5") #only positive numbers allowed
    free_shipping = models.BooleanField(default=False, help_text="check if you want to assign this product for free shipping")
    featured = models.BooleanField(default=False,  help_text="check if you want to add the product to the featured list")

    RATINGS = Choices(1,2,3,4,5)
    rating = models.PositiveIntegerField(choices=RATINGS, default=5, help_text="this rating should be set by users")

    # author = models.CharField(max_length=120) #only users should add a product
    author = models.ForeignKey(User, on_delete=models.CASCADE,  help_text="Assign this product to a user")

    STATUS = Choices('draft', 'published')
    status = models.CharField(choices=STATUS, default=STATUS.draft, max_length=20)
    created_at = models.DateField(auto_now_add=True) #auto_now_add=True 
    def __str__(self):
        return self.title #defines the title as a value that represetns a singular object of this class
    def get_cat_list(self):           #instance method allows to retrieve parent category
        k = self.category
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent

        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]