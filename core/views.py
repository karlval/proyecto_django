from django.views.generic import View
from django.shortcuts import render

class HomeView(View):
    # *args **kwargs
    # HACE REFERENCIA A CUALQUIER PARAMETRO QUE 'REQUEST' PUEDA RECIBIR
    def get(self, request, *args, **kwargs):
        context = {
            
        }
        return render(request, 'index.html', context)