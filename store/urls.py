from django.conf.urls.static import static
from django.urls import path
from SmartOne import settings
from . import views

urlpatterns = [
    path("", views.store, name='home'),
    path("cart/", views.cart, name='cart'),
    path("checkout/", views.checkout, name='checkout'),
    path("products/", views.products, name='products'),

    path("products/<int:id>/", views.product_detail, name='product_detail'),
    path("product_services/<int:id>/", views.product_services_detail, name='product_services_detail'),
    path("update_item/", views.update_item, name='update_item'),    path("process_order/", views.processOrder, name='process_order'),

    # payments api view
    path("paycom_payment/", views.Payment.as_view(), name='paycom_payment'),
    path('click/transaction/', views.TestView.as_view(), name='transaction'),

    # success page
    path("success_payment/<int:status><str:payment_id>", views.success_payment, name='success_payment'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
