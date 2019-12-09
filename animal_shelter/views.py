from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from animal_shelter.models import Animal
import random

class AnimalList(ListView):
    model = Animal
    template_name = 'animal_list.html'


class AnimalDetail(DetailView):
	model = Animal
	template_name = 'animal_detail.html'


class HomePage(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        col = random.randrange(1, Animal.objects.all().count())
        context['pet'] = Animal.objects.all()[col]
        return context


class ContactPage(TemplateView):

    template_name = "contact.html"


class AboutPage(TemplateView):

    template_name = "about.html"