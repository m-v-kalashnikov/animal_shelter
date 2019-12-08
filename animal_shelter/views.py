from django.shortcuts import render
from django.views.generic import ListView, DetailView
from animal_shelter.models import Animal

class AnimalList(ListView):
    model = Animal
    template_name = 'animal_list.html'


class AnimalDetail(DetailView):
	model = Animal
	template_name = 'animal_detail.html'
