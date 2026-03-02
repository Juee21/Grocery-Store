from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from .cart import Cart
from .forms import CartAddProductForm

# 1. List of all products
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })

# 2. Individual product page
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {
        'product': product,
        'cart_product_form': cart_product_form
    })
# 3. Logic to add item to cart (The missing piece!)
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
        return redirect('shop:cart_detail') # This takes you to the cart page
    return redirect('shop:product_list') # Fallback if form is invalid

# 4. Show the cart page (The other missing piece!)
def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        # This adds a form to each item to allow updating quantity
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True # This tells the cart to REPLACE the number, not add to it
        })
    return render(request, 'shop/cart/detail.html', {'cart': cart})

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('shop:cart_detail')
