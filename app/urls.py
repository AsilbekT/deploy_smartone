from django.urls import path
from . import views

urlpatterns = [
    path("service/", views.service, name='service'),
    path("warranty/", views.warranty, name='warranty'),
    path("payment_delivery/", views.payment_delivery, name='payment_delivery'),
    path("about/", views.about, name='about'),
    path("all-news/", views.all_news, name='all_news'),
    path("news_detail/<int:id>", views.news_detail, name='news_detail'),
    path("contact/", views.contact, name='contact'),
    path("messages/", views.messages, name='messages'),

    path('accounts/register/', views.register, name='register'),
    path('accounts/login/', views.login_page, name='login'),
    path("accounts/logout/", views.logout_user, name="logout"),
    path("change_lang/", views.change_lang, name="change_lang"),
    path("messages/<int:id>", views.message_detail, name='message_detail'),
]
