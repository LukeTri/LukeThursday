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

class Homepage(TemplateView):
    template_name = "index.html"