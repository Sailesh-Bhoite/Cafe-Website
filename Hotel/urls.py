from django.contrib import admin
from django.urls import path, include
from .views import homePage, showCart, loginPage, createAccount, downloadBill, profile, logout, placeOrder, analytics

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage, name='Home'),
    path('menu/', include('Menu.urls')),
    path('login/', loginPage, name="Login"),
    path('my-home/', include('Customers.urls')),
    path('cart/', showCart, name='ShowCart'),
    path("create-account/", createAccount, name="CreateAccount"),
    path("download-bill/", downloadBill, name="DownloadBill"),
    path('customer-profile/', profile, name="CustomerProfile"),
    path('logout/', logout, name='Logout'),
    path('order-placed/', placeOrder, name='PlaceOrder'),
    path('analytics/', analytics, name='Analytics'),
]
