from argparse import Namespace
from django.urls import path
from django.views.generic import TemplateView


app_name = 'templete_web'
urlpatterns = [
    path('', TemplateView.as_view(template_name='template_web/index.html'),name='template_web')

]