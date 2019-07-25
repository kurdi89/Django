from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

from .models import Product, Category
from .forms import Product_Create_Form

# error handling 
from django.shortcuts import get_list_or_404, get_object_or_404

# Create your views here.
def home(request):
    context = {
        "title" : "First Django app",
        "msg" : "Enjoy coding with Django",
    }
    return render(request, "index.html", context)

def shop(request):
    context = {
        "products_list": Product.objects.all(),
        "featured_list": Product.objects.filter(featured=True),
        "categories": Category.objects.all(),
        "title" : "Shop Page",
        "content" : "Welcome to the Store",
    }
    return render(request, 'shop.html', context)

def single_view(request, product_id):
    context = {
        "product": Product.objects.get(id=product_id),
        "title" : "Product Page Title",
        "content" : "this should be a body for a single page to view a singular book",
    }
    return render(request, 'single_product.html', context)

def create_product(request):
    form = Product_Create_Form() # form as an object
    if request.method == "POST":
        form = Product_Create_Form(request.POST, request.FILES)
        if form.is_valid():
            new = form.save()
            return redirect('single_view', product_id = new.id)
    context = {
        "create_form": form,
    }
    return render(request, 'create-product.html', context)

# Category function 
def show_category(request,hierarchy= None):
    category_slug = hierarchy.split('/')
    category_queryset = list(Category.objects.all())
    all_slugs = [ x.slug for x in category_queryset ]
    parent = None
    for slug in category_slug:
        if slug in all_slugs:
            parent = get_object_or_404(Category,slug=slug,parent=parent)
        else:
            instance = get_object_or_404(Product, slug=slug)
            print(instance)
            breadcrumbs_link = instance.get_cat_list()
            print(breadcrumbs_link)
            category_name = [' '.join(i.split('/')[-1].split('-')) for i in breadcrumbs_link]
            print(category_name)
            breadcrumbs = zip(breadcrumbs_link, category_name)
            print(breadcrumbs)
            
            context = {
                'instance':instance,'breadcrumbs':breadcrumbs, 'product' : Product.objects.get(title=instance)
            }
            return render(request, "single_product.html", context)

    return render(request,"categories.html",{'product_set':parent.product_set.all(),'sub_categories':parent.children.all()})