from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
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
from .forms import CantactForm
# Create your views here.


class HomeView(View):
	template_name = 'index.html'
	context = {}

	def get(self, request, *args, **kwargs):
		form = CantactForm()

		self.context['form'] = form
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
		form=CantactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data.get('name')
			phone_number = form.cleaned_data.get('phone_number')
			message = form.cleaned_data.get('message')

			try:
				subject = 'General Fitness'
				message = f"Ismi: {name}\ntel: {phone_number}\n"+message
				email_from = settings.EMAIL_HOST_USER
				recipient_list = ['dovurovjamshid95@gmail.com',]    
				send_mail( subject, message, email_from, recipient_list )
				messages.success(request, f"Dear {name}, your message succesfully send to admins")
			except Exception as e:
				message.error(request, f"smth went wrong, please check and try again :)", e)
			form = CantactForm()

			print(name, phone_number, message)
		self.context['form'] = form

		self.context['category'] = Category.objects.all()
		product_list = Product.objects.all()
		if len(product_list) > 7:
			self.context['recommended_product'] = product_list[:8]
		else:
			self.context['recommended_product'] = product_list

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
		if slug:
			category=Category.objects.get(slug=slug)
			return qs.filter(category=category)
		else:
			return qs
	
	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['category_list'] = Category.objects.all()
		return context
	

class ProductDetailView(DetailView):
	model         = Product
	template_name = 'product-detail.html'
	
	slug_url = 'slug'
	slug_field = 'slug'

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		product_list = Product.objects.filter(category=self.object.category)
		if len(product_list) > 7:
			context['recommended_product'] = product_list[:8]
		else:
			context['recommended_product'] = product_list
		return context


