from django.shortcuts import render, redirect
from .models import Order, OrderItem
from products.models import Product
from .forms import OrderForm
from django.contrib.auth.decorators import login_required

@login_required
def create_order(request):
    cart = request.session.get('cart', {})

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()

            for product_id, item in cart.items():
                product = Product.objects.get(id=product_id)
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    price=item['price'],
                    quantity=item['quantity']
                )

            request.session['cart'] = {}
            return render(request, 'orders/order_confirm.html')

    else:
        form = OrderForm(initial={
            'name': request.user.username,
            'email': request.user.email,
        })

    return render(request, 'orders/order_create.html', {'form': form})
