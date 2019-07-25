from django import forms
from .models import Product



# Creating a new product : 
class Product_Create_Form(forms.ModelForm):
    class Meta:
        model = Product
        # fields = ['title', 'summary', etc...]
        fields = '__all__'