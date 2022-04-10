from argparse import Namespace
from django.urls import path
from django.views.generic import TemplateView
from coderdjango.template_ecommerce.views import FormularioView
from coderdjango.template_ecommerce.views import FormularioView


app_name = 'templete_ecommerce'
urlpatterns = [
    path('', TemplateView.as_view(template_name='template_ecommerce/index.html'),name='template_ecommerce'),
    path('about', TemplateView.as_view(template_name='template_ecommerce/about.html'),name='template_ecommerce_about'),
    path('computer', TemplateView.as_view(template_name='template_ecommerce/computer.html'),name='template_ecommerce_computer'),
    path('contact', TemplateView.as_view(template_name='template_ecommerce/contact.html'),name='template_ecommerce_contact'),
    path('laptop', TemplateView.as_view(template_name='template_ecommerce/laptop.html'),name='template_ecommerce_laptop'),
    path('product', TemplateView.as_view(template_name='template_ecommerce/product.html'),name='template_ecommerce_product'),
    path('home', TemplateView.as_view(template_name='template_ecommerce/home.html'),name='template_ecommerce_home'),
    path('formulario', FormularioView.as_view(),name='template_ecommerce_form'),
]