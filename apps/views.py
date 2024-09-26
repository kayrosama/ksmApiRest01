from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

class HelloWorld(View):
    def get(self, request):
        #return HttpResponse(content='Hola Mundo, soy kBoot')
        data = {
            'nombre':'kBoot',
            'anios':'2',
            'codes':['python','html','css','javascript','java']

        }
        return render(request, 'hello.html', context=data)
        