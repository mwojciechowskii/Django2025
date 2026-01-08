from django.urls import path

from . import views

app_name = 'weather'

urlpatterns = [
    path('', views.weatherView, name='weather'),
    path("<str:inputCity>/", views.weatherView, name="cityWeather"),
]

