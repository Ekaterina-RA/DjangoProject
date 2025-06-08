from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Product
from .forms import ProductForm

class HomeView(TemplateView):
    template_name = "home.html"


class ContactsView(TemplateView):
    template_name = "contacts.html"

class ProductDetailView(DetailView):
    model = Product
    template_name = 'one_product.html'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('product_list')


class ProductListView(ListView):
    model = Product
    form_class = ProductForm
    template_name = 'product_list.html'
    context_object_name = 'products'


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    form_class = ProductForm
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

