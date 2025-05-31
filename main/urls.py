from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('blog/', views.blog, name='blog'),
    path('education/', views.education, name='education'),
    path('contact/', views.contact, name='contact'),
    
]
