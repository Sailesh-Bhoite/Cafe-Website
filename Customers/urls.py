from django.urls import path

from Customers.views import homePageLogged

urlpatterns = [
       path('', homePageLogged, name='HomeLogged'),
]
