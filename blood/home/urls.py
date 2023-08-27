from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('donor/', views.donor, name="donor"),
    path('search/', views.search, name="search"),
    path('admin/', views.admin, name="admin"),
    path('contact/', views.contact, name="contact"),
]