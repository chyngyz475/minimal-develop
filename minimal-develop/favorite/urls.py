from django.urls import path
from . import views

app_name = 'favorite'
urlpatterns = [
    path('add/', views.add_favorite, name='add_favorite'),
    path('remove/', views.remove_favorite, name='remove'),
]
