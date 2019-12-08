from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from animal_shelter.models import Animal

class AnimalList(ListView):
    model = Animal
    template_name = 'animal_list.html'


class AnimalDetail(DetailView):
	model = Animal
	template_name = 'animal_detail.html'


class HomePage(TemplateView):

    template_name = "home.html"


class ContactPage(TemplateView):

    template_name = "contact.html"


class AboutPage(TemplateView):

    template_name = "about.html"