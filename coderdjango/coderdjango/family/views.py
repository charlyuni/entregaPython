from http.client import ImproperConnectionState
from multiprocessing import context
from re import template
from typing import Any, Dict
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import myFamily


class familyView(TemplateView):
    template_name = 'family/index.html'

    

    def get(self, request, status=None):
        context = {
        'familiaresBBDD' : myFamily.objects.all()
        }
        return render(request, self.template_name, context)

