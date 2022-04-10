from multiprocessing import context
from urllib import response
from django import template
from django.views.generic import TemplateView
from django.shortcuts import render
from flask import request
from .models import formulario
from .form import ContactoForm



class FormularioView(TemplateView):
    template_name = 'template_ecommerce/form.html'

    def post(self, request):
        name = request.POST['name'] 
        lasname = request.POST['lasname'] 
        email = request.POST['email'] 
        phone = request.POST['phone'] 
        messege = request.POST['messege'] 


      

        obj_curso = formulario(name=name, lasname=lasname, email_client=email, phone=phone, messege=messege)
        obj_curso.save() 

        return render(request, self.template_name)

















""" 

    template_name = 'template_ecommerce/form.html'
   
   
    def get(self,request):
        context = {
            'form': ContactoForm()
        }

        return render(request, self.template_name, context)

    def post(self, request):
        print(request.POST)
        response = ContactoForm(request.POST) 
        if response.is_valid:
            obj_response = response.cleaned_data
            obj_curso = formulario( name = obj_response.get('name'),
                                    lasname = obj_response.get('lasname'),
                                    email_client = obj_response.get('email_client'),
                                    phone = obj_response.get('phone'),
                                    messege = obj_response.get('messege'))
            obj_curso.save()

        context = {
            'form': ContactoForm()
        }

        return render(request, self.template_name, context)


 """

        

"""      Curso.objects.create(
            name=name, camada=camada
        ) """

        