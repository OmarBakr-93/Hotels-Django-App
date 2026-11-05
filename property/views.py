from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Property

# Create your views here.


class PropertyListView(ListView):
    model = Property
    template_name = 'property/property_list.html'




class PropertyDetailView(DetailView):
    model = Property
    template_name = 'property/property_detail.html'

