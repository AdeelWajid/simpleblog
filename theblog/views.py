from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


# Create your views here.
#
# def home(request):
#     return render(request, 'home.html', {})

def HomeView(ListView):
    model = Post
    template_name = 'home.html'