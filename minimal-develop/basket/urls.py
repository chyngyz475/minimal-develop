from django.urls import path
from . import views

app_name = 'basket'
urlpatterns = [ 
    path('add/', views.add_product, name='add'), 
    path('remove/', views.remove_product, name='remove'), 
]
