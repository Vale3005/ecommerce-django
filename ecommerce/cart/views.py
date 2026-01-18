from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .forms import CartUpdateForm 
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
@require_POST
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    product = get_object_or_404(Product, id=product_id)

    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
    else:
        cart[str(product_id)] = {
            'name': product.name,
            'price': str(product.price),
            'quantity': 1
        }

    request.session['cart'] = cart
    request.session.modified = True

    messages.success(request, "Prodotto aggiunto al carrello!")

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        total_items = sum(item['quantity'] for item in cart.values())
        return JsonResponse({
            'message': "Prodotto aggiunto al carrello!",
            'total_items': total_items
        })

    return redirect('/cart/')


@login_required
def cart_detail(request): 
    cart = request.session.get('cart', {})

    items = []
    total = 0

    for product_id, item in cart.items():
        total += float(item['price']) * item['quantity']
        items.append({
            'product_id': product_id,
            'item': item,
            'subtotal': float(item['price']) * item['quantity'],
            'form': CartUpdateForm(initial={'quantity': item['quantity']})
        })

    return render(request, 'cart/cart_detail.html', {
        'items': items,
        'total': total
    })

@login_required
def update_cart(request, product_id): 
    cart = request.session.get('cart', {})

    if request.method == "POST":
        form = CartUpdateForm(request.POST)
        if form.is_valid(): 
            cart[str(product_id)]['quantity'] = form.cleaned_data['quantity']
            request.session['cart'] = cart 
    return redirect('/cart/')

@login_required
def remove_from_cart(request, product_id): 
    cart = request.session.get('cart', {})

    if str(product_id) in cart: 
        del cart[str(product_id)]
        request.session['cart'] = cart 

    return redirect('/cart/') 

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
def increase_quantity(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
        request.session['cart'] = cart

    return redirect('cart_detail')


@login_required
def decrease_quantity(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] -= 1

        if cart[str(product_id)]['quantity'] <= 0:
            del cart[str(product_id)]

        request.session['cart'] = cart

    return redirect('cart_detail')
