from django.http import HttpRequest
from django.shortcuts import render
from web.models import Product

# Create your views here.
def index(request: HttpRequest):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "index.html", context=context)

def contacts(request: HttpRequest):
    return render(request, "contacts.html")