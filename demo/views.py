from django.shortcuts import render



def home(request):
    return render(request, 'demo/home.html')


def products(request):
    return render(request, 'demo/products.html')


def customers(request):
    return render(request, 'demo/customers.html')