from django.urls import path

from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.homeView, name='home'),
    path('start/', views.homeView, name='start'),
    path('contact/', views.contactView, name='contact'),
    path('about/', views.aboutView, name='about'),
    path('about-me/', views.aboutView),
    path('genbank/', views.genbankView, name='genbank'),
]
