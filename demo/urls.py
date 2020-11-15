from django.urls import path
from .views import home, products, customers


app_name = 'demo'

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('customers/', customers, name='customers'),
]


