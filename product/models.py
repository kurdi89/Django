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
    parent = models.ForeignKey('self',blank=True, on_delete=models.PROTECT, null=True ,related_name='children') # when deleting the parent delete children as well

    class Meta:
        unique_together = ('slug', 'parent',)    #enforcing that there can not be two
        verbose_name_plural = "categories"       #categories under a parent with same slug 
    def __str__(self):                           # __str__ method elaborated later in
        full_path = [self.name]                  # post.  use __unicode__ in place of __str__ if you are using python 2
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
    discount_price = models.PositiveIntegerField(blank=True, null=True) #only positive numbers allowed can be null in case there was no discount
    thumbnail = models.ImageField()
    image_link = models.CharField(max_length=120, default=None) #set it to be null by default, unless a link is added
    sku = models.CharField(max_length=120)
    slug = models.SlugField(unique=True) #gives a unique slug for each product
    inventory =  models.PositiveIntegerField(default=5) #only positive numbers allowed
    free_shipping = models.BooleanField(default=False)

    # author = models.CharField(max_length=120) #only users should add a product
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)

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