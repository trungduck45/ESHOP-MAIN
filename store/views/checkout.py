from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Products
from store.models.orders import Order
from django.core.mail import send_mail

from django.conf import settings
from django.template.loader import render_to_string
class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Products.get_products_by_id(list(cart.keys()))
        email = request.POST.get('email')
        print(address, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}

       # first_name = request.POST.get('first_name')
       # customer_name = Customer.first_name
        customer = Customer.objects.get(id=customer)
        customer_name= customer.first_name

        email_subject = 'Thanks you for purchasing from eCommerce !'
        email_body = render_to_string('email.html',{'name': customer_name})
        send_mail(
            subject = email_subject,
            message = '',
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [email],
            html_message = email_body,
        )
        return redirect('send_mail')

