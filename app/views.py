import json
import requests
from django.template.defaulttags import url
from django.utils import translation
from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from store.utils import cartData, translate_the_text
from django.shortcuts import render, redirect
from contact.models import FeedBack
from django.contrib.auth.forms import AuthenticationForm
from .forms import FeedBackForm, NewUserForm
from store.models import Customer, Product, Order, OrderItem, ProductServices
from .models import Dealers, News
from django.http import JsonResponse
from contact.models import FeedBack


def service(request):
    text = translate_the_text(request.LANGUAGE_CODE)
    data = cartData(request)
    cartItems = data['cartItems']
    dealers = Dealers.objects.all()
    all_news = News.objects.all()
    products = Product.objects.all()
    productService = ProductServices.objects.all()
    context = {"dealers":dealers,"text":text,"products": products, "productServices": productService, "all_news": all_news, "cartItems": cartItems}
    return render(request, "new_design/services.html", context)


def warranty(request):
    text = translate_the_text(request.LANGUAGE_CODE)
    data = cartData(request)
    cartItems = data['cartItems']
    all_news = News.objects.all()
    products = Product.objects.all()
    productService = ProductServices.objects.all()
    context = {"text":text,"products": products, "productServices": productService, "all_news": all_news, "cartItems": cartItems}
    return render(request, "new_design/warranty.html", context)

def payment_delivery(request):
    text = translate_the_text(request.LANGUAGE_CODE)
    data = cartData(request)
    cartItems = data['cartItems']
    all_news = News.objects.all()
    products = Product.objects.all()
    productService = ProductServices.objects.all()
    context = {"text":text,"products": products, "productServices": productService, "all_news": all_news, "cartItems": cartItems}
    return render(request, "new_design/payment-delivery.html", context)


@login_required(login_url="/accounts/login")
def messages(request):
    url = "https://kassa-aparat-default-rtdb.firebaseio.com/orders.json"
    payload = json.dumps({
        # 'order': order,
        'id': 1,
        'order_day': "12 decabr",
        "number": 4

    })
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "d40f61e7-bac1-e66b-0415-1169251aa220"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    context = {

    }
    return render(request, "messages.html", context)


@login_required(login_url="/accounts/login")
def message_detail(request, id):
    feedback = FeedBack.objects.get(id=id)
    context = {"feedback": feedback, "check": "only_feedback"}
    return render(request, "messages.html", context)


def about(request):
    text = translate_the_text(request.LANGUAGE_CODE)
    data = cartData(request)
    cartItems = data['cartItems']
    all_news = News.objects.all()
    products = Product.objects.all()
    productService = ProductServices.objects.all()
    context = {"text":text,"products": products, "productServices": productService, "all_news": all_news, "cartItems": cartItems}
    return render(request, "new_design/about.html", context)


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    elif request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login")
    form = NewUserForm()
    return render(request, "registration/register.html", context={"register_form": form})


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    elif request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "registration/login.html", context={"login_form": form})


def logout_user(request):
    logout(request)
    return redirect("home")


def change_lang(request):
    LANGUAGE_SESSION_KEY = '_language'
    if request.user.is_authenticated:
        if request.method == "POST":
            sent_url = request.POST['url']
            old_lang = request.LANGUAGE_CODE
            changed_lang = request.POST['button']
            translation.activate(changed_lang)
            request.session[LANGUAGE_SESSION_KEY] = changed_lang
            print(request.session[LANGUAGE_SESSION_KEY])
            # I use HTTP_REFERER to direct them back to previous path 
            if "en" in sent_url:
                if changed_lang != 'uz':
                    new_url = sent_url.replace('en', changed_lang)
                    return HttpResponseRedirect(new_url)
                elif changed_lang == 'uz':
                    new_url1 = sent_url.replace('en', '')
                    new_url = new_url1[1:]
                    return HttpResponseRedirect(new_url)
            elif "ru" in sent_url:
                if changed_lang != 'uz':
                    new_url = sent_url.replace('ru', changed_lang)
                    return HttpResponseRedirect(new_url)
                elif changed_lang == 'uz':
                    new_url1 = sent_url.replace('ru', '')
                    new_url = new_url1[1:]
                    return HttpResponseRedirect(new_url)
            elif old_lang == "uz" and changed_lang != 'uz':
                new_url = f"/{changed_lang}" + sent_url

                return HttpResponseRedirect(new_url)
            
            return HttpResponseRedirect(sent_url)


def all_news(request):
    text = translate_the_text(request.LANGUAGE_CODE)
    data = cartData(request)
    cartItems = data['cartItems']
    all_news = News.objects.all()
    products = Product.objects.all()
    productService = ProductServices.objects.all()
    context = {"text":text,"products": products, "productServices": productService, "all_news": all_news, "cartItems": cartItems}
    return render(request, "new_design/all-news.html", context)


def news_detail(request, id):
    text = translate_the_text(request.LANGUAGE_CODE)
    data = cartData(request)
    cartItems = data['cartItems']
    products = data['products']
    news = data['all_news']
    news_detail = News.objects.get(id=id)
    productService = ProductServices.objects.all()
    context = {"text":text,"products": products, "productServices": productService, "news_detail": news_detail,
               "cartItems": cartItems, "all_news": news}
    return render(request, "new_design/news-data.html", context)


def contact(request):
    text = translate_the_text(request.LANGUAGE_CODE)
    data = cartData(request)
    cartItems = data['cartItems']
    products = Product.objects.all()
    news = data['all_news']
    productService = ProductServices.objects.all()

    if request.method == 'POST':
        form = FeedBackForm(request.POST or None)
        if len(form.data['city']) > 0:
            city = form.data['city']
            feedback = FeedBack.objects.create(city=city)
            feedback.user_name = form.data['username']
            feedback.phone_number = form.data['phone']
            feedback.email = form.data['email']
            feedback.text = form.data['text']
            feedback.save()
    form = FeedBackForm()
    
    context = {"form":form,"text":text,"products": products, "productServices": productService, "news_detail": news_detail,
               "cartItems": cartItems, "all_news": news}
    return render(request, "new_design/contact.html", context)
