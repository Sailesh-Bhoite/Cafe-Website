from django.shortcuts import render, redirect

from Menu.models import MenuItem
from Customers.models import Customer
from Orders.models import Order, OrderItem
from django.db import transaction
from django.db.models import Sum

# For PDF generation
from fpdf import FPDF
from fpdf.enums import XPos, YPos

# For plotting graph
import plotly.graph_objects as go


def homePage(request):
    if request.session.get('customer_id'):
        return redirect('/my-home/')
    return render(request, 'home.html')


def showCart(request):
    total_amt = 0
    cart_details = []
    selected_items = {}
    if request.session.get('customer_id'):
        if request.method == 'POST':
            for key, value in request.POST.items():
                if key.startswith('item_name_'):
                    item_id = key.split('item_name_')[-1]
                    item_name = value
                    item_quantity = int(request.POST.get(f'item_quantity_{item_id}'), 0)

                    if item_quantity > 0:
                        selected_items[item_name] = item_quantity

            print("Selected Items: ", selected_items)

            for item_name, item_quantity in selected_items.items():
                try:
                    item = MenuItem.objects.get(name=item_name)
                    cart_details.append({
                        "name": item.name,
                        "quantity": item_quantity,
                        "price": int(item.price),
                        "total": int(item.price) * item_quantity
                    })
                    total_amt += item_quantity * item.price

                except MenuItem.DoesNotExist:
                    print(f'Item {item_name} does not exist!!!!!!!!!!!!!!!!!!!!')

            request.session["cart_details"] = cart_details
            request.session.modified = True

            print("Cart Details Session:", request.session.get("cart_details"))
        else:
            return redirect('/login/')
    return render(request, 'cart.html', {'cart_items': request.session.get("cart_details"), 'total_amount': total_amt})


def loginPage(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            customer = Customer.objects.get(name=username, password=password)
            request.session['customer_id'] = customer.id
            return redirect(f'/my-home/')  # If a user exists, redirect to Logged Home Page
        except Customer.DoesNotExist:
            # If a user doesn't exist, generate an error message.
            error_message = 'Username or password incorrect!'
    return render(request, 'loginPage.html', {'error_message': error_message})


def createAccount(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = Customer(name=name, email=email, password=password)
        user.save()
        return redirect(f"/login/")
    return render(request, "createAccount.html")


def downloadBill(request):
    cart_items = request.session.get('cart_details')
    print("(Download Bill) cart_details: ", cart_items)
    total_price = 0

    pdf = FPDF()
    pdf.add_page()

    bill_no = request.GET.get('order_id')

    # Setting Café Name font
    pdf.set_font('helvetica', "B", 20)

    # Name of Café
    pdf.cell(190, 20, text="Bhoite's Cafe", border=True, align="c", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Space
    pdf.cell(190, 6, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Setting font to normal
    pdf.set_font('helvetica', "", 12)

    # Bill number and GSTIN
    pdf.cell(80, 10, text=f"Bill No: {bill_no}", border=True, align="l")
    pdf.cell(110, 10, text="GSTIN: 123456", border=True, align="l", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Address
    pdf.cell(190, 10, text="Address: NH 3, Mumbai Nashik Highway Opp.Bhoir Pada Bus Stop, Near Padga Bhiwandi, Pune",
             border=True, align="l", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Contact Number
    pdf.cell(190, 10, text="Contact: 9561191284", border=True, align="l", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Space
    pdf.cell(190, 6, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Table heading
    pdf.set_font('helvetica', "B", 12)
    pdf.cell(20, 10, text="Sr.No.", border=True, align="c")
    pdf.cell(110, 10, text="Item", border=True, align="c")
    pdf.cell(20, 10, text="QTY", border=True, align="c")
    pdf.cell(20, 10, text="Rate", border=True, align="c")
    pdf.cell(20, 10, text="Amt", border=True, align="c", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Content
    pdf.set_font('helvetica', "", 12)
    for i in range(len(cart_items)):
        pdf.cell(20, 10, text=f"{i + 1}", border=True, align="c")
        pdf.cell(110, 10, text=f"{cart_items[i]['name']}", border=True, align="c")
        pdf.cell(20, 10, text=f"{cart_items[i]['quantity']}", border=True, align="c")
        pdf.cell(20, 10, text=f"{cart_items[i]['price']}", border=True, align="c")
        pdf.cell(20, 10, text=f"{cart_items[i]['total']}", border=True, align="c", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        total_price += cart_items[i]['total']

    # Total
    pdf.set_font('helvetica', "B", 12)
    pdf.cell(150, 10, text="Total Amount", border=True, align="r")
    pdf.set_font('helvetica', "", 12)
    pdf.cell(40, 10, text=f"{total_price}", border=True, align="c", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Space
    pdf.cell(190, 6, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Setting Thank You font
    pdf.set_font('helvetica', "BI", 15)

    # Regards
    pdf.cell(190, 6, text="Thank You for your visit.", align="c", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(190, 6, text="Have a nice day!", align="c", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Save the PDF
    pdf.output(f"Bhoite's Cafe Bill No {bill_no}.pdf")
    print("Download Bill Completed")

    # Clear the cart from the session after successful order placement
    if 'cart_details' in request.session:
        del request.session['cart_details']
    request.session.modified = True

    return redirect('Home')


def profile(request):
    customer = Customer.objects.get(id=request.session['customer_id'])
    return render(request, "customer_profile.html", {'customer': customer})


def logout(request):
    request.session.flush()
    return redirect('/')


def placeOrder(request):
    # 1. Manual Login Check: Check for your custom customer_id in session
    customer_id = request.session.get('customer_id')
    if not customer_id:
        # If no customer ID in session, redirect to login page
        return redirect('/login/')

    # Retrieve the Customer object using the ID from the session
    try:
        customer_obj = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        # Handles a case where customer_id in session is invalid or user deleted
        print(f"Error: Customer with ID {customer_id} not found from session.")
        del request.session['customer_id']  # Clear invalid session data
        request.session.modified = True
        return redirect('/login/')  # Redirect to login or error page

    # 2. Retrieve cart data (list of dicts) from the session
    cart_details = request.session.get('cart_details', [])

    # Checking whether the cart is not empty for extra security.
    if not cart_details:
        print("Cart is empty. Cannot place an empty order.")
        return render(request, 'cart.html')

    try:
        with transaction.atomic():
            # 3. Calculate the total price of the order
            calculated_total_price = sum(item['price'] * item['quantity'] for item in cart_details)

            # 4. Create the main Order record
            order = Order.objects.create(
                customer=customer_obj,  # Assign your custom Customer object here
                total_price=calculated_total_price,
                # 'order_date' is set automatically by auto_now_add=True
            )
            print(f"Created new Order with ID: {order.id}")

            # 5. Iterate through cart_details and create OrderItem records
            for item_data in cart_details:
                try:
                    menu_item_obj = MenuItem.objects.get(name=item_data['name'])
                except MenuItem.DoesNotExist:
                    print(
                        f"Error: Menu item '{item_data['name']}' not found in database while placing order. Transaction will rollback.")
                    raise MenuItem.DoesNotExist(f"Menu item '{item_data['name']}' not found.")

                OrderItem.objects.create(
                    order=order,
                    menu_item=menu_item_obj,
                    quantity=item_data['quantity'],
                    price=item_data['price']
                )
                print(f"  Added OrderItem: {item_data['quantity']} x {item_data['name']}")

        print("Order Placed Successfully! Cart cleared.")
        return render(request, 'place_order.html', {
            'order': order,
        })

    except MenuItem.DoesNotExist as e:
        print(f"Failed to place order due to missing menu item: {e}")
        return render(request, 'place_order.html', {
            'message': f'Error placing order: One or more items in your cart are no longer available ({e}). Please review your cart.',
            'error_detail': str(e)
        })
    except Exception as e:
        print(f"An unexpected error occurred while placing the order: {e}")
        return render(request, 'place_order.html', {
            'message': 'An error occurred while processing your order. Please try again.',
            'error_detail': str(e)
        })


def analytics(request):
    bar_colors = [
        '#4285F4',  # Google Blue
        '#34A853',  # Google Green
        '#FBBC05',  # Google Yellow
        '#EA4335',  # Google Red
        '#8E44AD',  # Amethyst Purple
        '#27AE60',  # Emerald Green
        '#E67E22',  # Carrot Orange
        '#3498DB',  # Peter River Blue
        '#C0392B',  # Alizarin Red
        '#7F8C8D'  # Asbestos Grey
    ]

    top_items_data = OrderItem.objects.values(
        'menu_item__name'  # Accesses the 'name' attribute of the related MenuItem
    ).annotate(
        total_quantity=Sum('quantity')  # Sums up the quantities for each item
    ).order_by(
        '-total_quantity'  # Order in descending order (the highest quantity first)
    )[:10]  # Limit to top 10 items (change to [:5] for top 5)

    print(top_items_data)
    # Prepare data for Plotly chart
    item_names = [item['menu_item__name'] for item in top_items_data]
    quantities_sold = [item['total_quantity'] for item in top_items_data]

    # Create the Plotly horizontal bar chart
    # Use go.Bar and set orientation='h' for horizontal bars
    fig = go.Figure(data=[go.Bar(
        x=quantities_sold,      # For horizontal bars, 'x' is the quantity
        y=item_names,     # And 'y' is the category (fruit name)
        orientation='h',   # This makes the bars horizontal
        marker=dict(color=bar_colors)  # A nice color for the bars
    )])

    # Customize the chart layout
    fig.update_layout(
        title_text='BEST Selling Products',  # Chart title
        xaxis_title_text='Quantity',  # X-axis label
        yaxis_title_text='Food Items',    # Y-axis label
        yaxis=dict(categoryorder='total ascending')  # Optional: Reverse y-axis to show the highest bar at the top.
    )

    # Convert the Plotly figure to an HTML div string
    # include_plotlyjs=False assumes you load plotly.js globally in your base template or this specific template
    graph_div = fig.to_html(full_html=False, include_plotlyjs=False)

    context = {
        'chart_div': graph_div
    }

    return render(request, 'analytics.html', context)
