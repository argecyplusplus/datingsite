from django.shortcuts import render
from django.views.generic.base import View
from .models import Form

# Create your views here.

class FormView(View):
    '''вывод анкет'''
    def get(self, request):
        forms = Form.objects.all()
        return render(request, 'searching/searching.html', {'form_list': forms})
    