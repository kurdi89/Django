from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

from .models import Product
from .forms import Product_Create_Form

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
        "featured_list": Product.objects.get(featured=True),
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
