from django.shortcuts import render

from django.views.generic import TemplateView, ListView

from .models import City


class homepage(TemplateView):
    template_name = 'home.html'

class searchresult(ListView):
    model = City
    template_name = 'search_result.html'
