from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)

from product.models import (
    Category,
    Product,
    ProductImage,
)

# Create your views here.


class HomeView(View):
    template_name = 'index.html'
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['category_list'] = Category.objects.all()
        product_list = Product.objects.all()
        if len(product_list) > 7:
            self.context['recommended_product'] = product_list[:8]
        else:
            self.context['recommended_product'] = product_list

        return render(
            request, 
            self.template_name, 
            self.context
        )

    def post(self, request, *args, **kwargs):
        self.context['category'] = Category.objects.all()
        return render(
            request,
            self.template_name,
            self.context,
        )


class CategoryView(ListView):
    model = Product
    template_name = 'products.html'
    paginate_by = 15

    def get_queryset(self):
        qs = super().get_queryset()

        slug = self.kwargs.get('slug')
        print(slug)
        if slug:
            category=Category.objects.get(slug=slug)
            return qs.filter(category=category)
        else:
            return qs
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['category_list'] = Category.objects.all()
        return context
    

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