from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product
from basketapp.models import Basket
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

LINKS_MENU = [
    {'href': 'main', 'name': 'домой'},
    {'href': 'products:index', 'name': 'продукты'},
    {'href': 'contact', 'name': 'контакты'},
]


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.all()

    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]

    return same_products


def main(request):
    products = Product.objects.all()[:4]

    content = {
        'title': 'Магазин',
        'links_menu': LINKS_MENU,
        'products': products,
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/index.html', context=content)


def products(request, pk=None, page=1):
    title = 'продукты'
    links_menu_category = ProductCategory.objects.all()
    basket = get_basket(request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {
                'pk': 0,
                'name': 'все'
            }
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')
        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)


        content = {
            'title': title,
            'links_menu': LINKS_MENU,
            'links_menu_category': links_menu_category,
            'category': category,
            'products': products_paginator,
            'basket': basket,
        }

        return render(request, 'mainapp/products_list.html', content)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    content = {
        'title': title,
        'links_menu': LINKS_MENU,
        'links_menu_category': links_menu_category,
        'same_products': same_products,
        'hot_product': hot_product,
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/products.html', context=content)


def product(request, pk):
    title = 'продукт'

    content = {
        'title': title,
        'links_menu': LINKS_MENU,
        'links_menu_category': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
    }

    return render(request, 'mainapp/product.html', content)


def contact(request):
    content = {
        'title': 'Контакты',
        'links_menu': LINKS_MENU,
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/contact.html', context=content)
