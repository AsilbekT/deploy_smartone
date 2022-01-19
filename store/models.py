from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


# Create your models here.
from tinymce.models import HTMLField


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(_('Name'), max_length=200, null=True)
    email = models.CharField(_('Email'), max_length=200, null=True)
    lang = models.CharField(_('Language'), default='en', max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    name_uz = models.CharField(max_length=200, null=True)
    name_ru = models.CharField(max_length=200, null=True)

    title = models.CharField(max_length=200, null=True)
    title_ru = models.CharField(max_length=200, null=True)
    title_uz = models.CharField(max_length=200, null=True)

    description_ru = models.TextField(default="description")
    description_uz = models.TextField(default="description")
    description = models.TextField(default="description")
    line_ru = HTMLField(default="line")
    line_uz = HTMLField(default="line")
    line = HTMLField(default="line")
    price = models.DecimalField(max_digits=7, decimal_places=2)
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(default="default.jpg", upload_to='uploads/')
    image2 = models.ImageField(default="default.jpg", upload_to='uploads/')
    image3 = models.ImageField(default="default.jpg", upload_to='uploads/')
    image4 = models.ImageField(default="default.jpg", upload_to='uploads/')
    image5 = models.ImageField(default="default.jpg", upload_to='uploads/')

    def __str__(self):
        return self.name

    @property
    def product_url(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    @property
    def product_url2(self):
        try:
            url = self.image2.url
        except:
            url = ''
        return url

    @property
    def product_url3(self):
        try:
            url = self.image3.url
        except:
            url = ''
        return url

    @property
    def product_url5(self):
        try:
            url = self.image5.url
        except:
            url = ''
        return url

    @property
    def product_url4(self):
        try:
            url = self.image4.url
        except:
            url = ''
        return url


class ProductServices(models.Model):
    name = models.CharField(default='', max_length=200, null=True)
    name_uz = models.CharField(max_length=200, null=True)
    name_ru = models.CharField(max_length=200, null=True)

    title = models.CharField(max_length=200, null=True)
    title_ru = models.CharField(max_length=200, null=True)
    title_uz = models.CharField(max_length=200, null=True)

    description_ru = models.TextField(default="description")
    description_uz = models.TextField(default="description")
    description = models.TextField(default="description")
    line_ru = HTMLField(default="line")
    line_uz = HTMLField(default="line")
    line = HTMLField(default="line")
    price = models.DecimalField(max_digits=7, decimal_places=2)
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(default="default.jpg", upload_to='uploads/')
    image2 = models.ImageField(default="default.jpg", upload_to='uploads/')
    image3 = models.ImageField(default="default.jpg", upload_to='uploads/')
    image4 = models.ImageField(default="default.jpg", upload_to='uploads/')
    image5 = models.ImageField(default="default.jpg", upload_to='uploads/')

    def __str__(self):
        return self.name

    @property
    def product_url(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    @property
    def product_url2(self):
        try:
            url = self.image2.url
        except:
            url = ''
        return url

    @property
    def product_url3(self):
        try:
            url = self.image3.url
        except:
            url = ''
        return url

    @property
    def product_url5(self):
        try:
            url = self.image5.url
        except:
            url = ''
        return url

    @property
    def product_url4(self):
        try:
            url = self.image4.url
        except:
            url = ''
        return url


class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=100, default='Tashkent')
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    @property
    def get_cart_total(self):
        order_items = self.orderitem_set.all()
        total = sum([item.get_total for item in order_items])
        return total

    @property
    def get_cart_items(self):
        order_items = self.orderitem_set.all()
        total = sum([item.quantity for item in order_items])
        return total

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    productServices = models.ForeignKey(ProductServices, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_ended = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        if self.product:
            total = self.product.price * self.quantity
        elif self.productServices:
            total = self.productServices.price * self.quantity
        else:
            total = 0
        return total

    def __str__(self):
        if self.product:
            return self.product.name
        return self.productServices


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, null=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
