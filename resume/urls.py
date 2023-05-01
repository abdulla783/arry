from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('download-pdf/', views.download_pdf, name='download_pdf'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('termCon/', views.termCon, name='termCon'),
]

