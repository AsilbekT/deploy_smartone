import json
from .models import *
from app.models import News, TextsToTranslate


def cartData(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        all_news = News.objects.all()
        products = Product.objects.all()
    else:
        all_news = News.objects.all()
        cookieData = cookieCart(request)
        items = cookieData['items']
        order = cookieData['order']
        cartItems = cookieData['cartItems']
        products = Product.objects.all()

    return {"cartItems": cartItems, 'order': order, 'items': items, "all_news":all_news, "products": products}


def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    items = []
    order = {"get_cart_total": 0, "get_cart_items": 0}
    cartItems = order['get_cart_items']

    for i in cart:
        try:
            cartItems += cart[i]['quantity']
            product = Product.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])

            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']
            item = {
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'product_url': product.product_url,
                },
                'quantity': cart[i]['quantity'],
                'get_total': total,
            }
            items.append(item)
        except:
            pass
    return {"cartItems": cartItems, 'order': order, 'items': items}


def translate_the_text(lang):
    textObject = TextsToTranslate.objects.all()
    text = {}
    for i in textObject:
        if lang == 'uz':
            (text[i.title]) = i.text_uz
        elif lang == 'ru':
            text[i.title] = i.text_ru
        else:
            text[i.title] = i.text_en
    return text