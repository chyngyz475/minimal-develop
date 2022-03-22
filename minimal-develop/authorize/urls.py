from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contacts, name='contacts'), 
    path('send-app/', views.consultation_handler, name='send_app'),
    path("robots.txt", views.robots),
    path("sitemap.xml", views.sitemap),
]
