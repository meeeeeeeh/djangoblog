from django.core.mail import send_mail
from django.template.loader import render_to_string

from .models import Product, Review, Basket, ProductInBasket, Order, Favorites
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.conf import settings


def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})


def product_detail(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    reviews = Review.objects.filter(product=product_pk)
    return render(request, 'shop/product_detail.html', {'product': product,
                                                        'reviews': reviews})


def product_basket(request):
    basket = get_object_or_404(Basket, user=request.user)
    products = ProductInBasket.objects.filter(basket=basket)
    # total_cost = 0
    # for product in products:
    #     total_cost += product.products.cost * product.product_count
    return render(request, 'shop/product_basket.html', {'products': products, 'basket': basket})


def add_to_basket(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    basket = get_object_or_404(Basket, user=request.user)
    products = ProductInBasket.objects.filter(basket=basket)

    if ProductInBasket.objects.filter(products=product, basket=basket):
        product_in_basket = ProductInBasket.objects.get(products=product, basket=basket)
        product_in_basket.product_count += 1
        product_in_basket.save()
    else:
        ProductInBasket.objects.create(products=product, basket=basket)
    return render(request, 'shop/product_basket.html', {'products': products})


def remove_from_basket(request, product_pk):
    product = get_object_or_404(ProductInBasket, pk=product_pk)
    basket = get_object_or_404(Basket, user=request.user)
    product.product_count -= 1
    product.save()
    if product.product_count == 0:
        product.delete()
    return redirect('product_basket')


def remove_all_products(request, product_pk):
    product = get_object_or_404(ProductInBasket, pk=product_pk)
    basket = get_object_or_404(Basket, user=request.user)
    product.delete()
    return redirect('product_basket')


def delete_all(request):
    basket = get_object_or_404(Basket, user=request.user)
    products = ProductInBasket.objects.filter(basket=basket)
    products.delete()
    return redirect('product_basket')


def order(request):

    basket = get_object_or_404(Basket, user=request.user)
    products_ids = [product.products for product in basket.productinbasket_set.all()]
    order = Order.objects.create(user=request.user)
    for product_id in products_ids:
        order.products.add(product_id)
    ordered_products = order.products.all()
    msg = render_to_string('shop/order.html', {'ordered_products': ordered_products,
                                               'basket': basket})
    send_mail('Заказ', msg, settings.EMAIL_HOST_USER, ['alexanderkarpovich78@gmail.com'])
    # ordered_products.products = [product.products for product in products]
    order_total_cost = basket.total_cost
    order.save()
    products = ProductInBasket.objects.filter(basket=basket)
    products.delete()

    return render(request, 'shop/order.html', {'ordered_products': ordered_products,
                                               'order_total_cost': order_total_cost})


def orders_history(request):
    user = request.user
    orders = Order.objects.filter(user=user)

    return render(request, 'shop/history.html', {'orders': orders})


def add_to_favorites(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    favorite = Favorites.objects.create(user=request.user)
    favorite.products.add(product)
    favorites = Favorites.objects.filter(user=request.user)
    return render(request, 'shop/favorites.html', {'favorites': favorites})




