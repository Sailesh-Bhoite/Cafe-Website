from django.shortcuts import render
from .models import MenuItem


# Create your views here.
def menuPage(request):
    categories = [
        {
            'name': 'Hot Beverages',
            'icon': '/static/images/hot-beverage-icon.png',
            'menu_items': MenuItem.objects.filter(category='Hot Beverage')
        },
        {
            'name': 'Cold Beverages',
            'icon': '/static/images/cold-beverage-icon.png',
            'menu_items': MenuItem.objects.filter(category='Cold Beverage')
        },
        {
            'name': 'Pizzas',
            'icon': '/static/images/pizza-icon.png',
            'menu_items': MenuItem.objects.filter(category='Pizza')
        },
        {
            'name': 'Burgers',
            'icon': '/static/images/burger-icon.png',
            'menu_items': MenuItem.objects.filter(category='Burger')
        },
        {
            'name': 'Sandwiches',
            'icon': '/static/images/sandwich-icon.png',
            'menu_items': MenuItem.objects.filter(category='Sandwich')
        },
        {
            'name': 'Momos',
            'icon': '/static/images/momos-icon.png',
            'menu_items': MenuItem.objects.filter(category='Momos')
        },
        {
            'name': 'Others',
            'icon': '/static/images/others-icon.png',
            'menu_items': MenuItem.objects.filter(category='Others')
        }
    ]

    return render(request, 'menu.html', {'categories': categories, 'log_in': request.session.get('customer_id')})
