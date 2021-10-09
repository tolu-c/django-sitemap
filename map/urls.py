from django.urls import path
from . import views

# app_name = 'map'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('support/', views.support, name='support'),
    path('<slug:slug>/', views.snippet_detail, name='detail')
]
