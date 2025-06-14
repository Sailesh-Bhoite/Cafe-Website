from django.urls import path
from .views import menuPage


urlpatterns = [
    path('', menuPage),
]