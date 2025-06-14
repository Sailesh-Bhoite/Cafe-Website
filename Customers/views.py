from django.shortcuts import render
from Customers.models import Customer


# Create your views here.
def homePageLogged(request):
    customer = None
    if request.session.get('customer_id'):
        customer = Customer.objects.get(id=request.session['customer_id'])
    return render(request, 'home_logged.html', {'customer': customer})
