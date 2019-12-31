from django.shortcuts import render

# Create your views here.

from datetime import date
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


from django.urls import reverse_lazy, reverse


from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

from fullstackexam.forms import CreateRatingForm
from fullstackexam.models import Rating




class RatingCreate(CreateView):
    form_class = CreateRatingForm
    template_name = 'fullstackexam/rating_form.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('rating_list')


class AboutPage(TemplateView):
    template_name = "fullstackexam/about.html"

class PicturePage(TemplateView):
    template_name = 'fullstackexam/picture.html'


class RatingList(ListView):
    model = Rating
