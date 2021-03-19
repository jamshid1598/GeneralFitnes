from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)
# from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class HomeView(View):
    template_name = 'index.html'
    context = {}

    def get(self, request, *args, **kwargs):
        return render(
            request, 
            self.template_name, 
            self.context
        )

    def post(self, request, *args, **kwargs):
        return render(
            request,
            self.template_name,
            self.context,
        )



class CategoryView(View):
    template_name = 'products.html'
    context = {}

    def get(self, request, *args, **kwargs):
        return render(
            request, 
            self.template_name, 
            self.context
        )

    def post(self, request, *args, **kwargs):
        return render(
            request,
            self.template_name,
            self.context,
        )



class ProductDetailView(View):
    template_name = 'product-detail.html'
    context = {}

    def get(self, request, *args, **kwargs):
        return render(
            request, 
            self.template_name, 
            self.context
        )

    def post(self, request, *args, **kwargs):
        return render(
            request,
            self.template_name,
            self.context,
        )