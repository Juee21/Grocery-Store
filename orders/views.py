from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.http import HttpResponse
from .models import Order, OrderItem
from .forms import OrderCreateForm
from shop.cart import Cart
from reportlab.pdfgen import canvas


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            # Clear the cart session
            cart.clear()
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})

def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'

    p = canvas.Canvas(response)

    #Header
    p.setFont("Helvetica", 12)
    p.drawString(100, 800, f"Grocery Store Invoice #{order.id}")

    # Customer details
    p.setFont("Helvetica", 12)
    p.drawString(100, 770, f"Bill To: {order.first_name}{order.last_name}")
    p.drawString(100,750, f"Email: {order.email}")
    p.line(100, 725, 500, 725)

    #Table logic
    y=700
    for item in order.items.all():
        p.drawString(100, y, f"{item.product.name} x {item.quantity}")
        p.drawString(400, y, f"${item.price}")

    p.showPage()
    p.save()
    return response


