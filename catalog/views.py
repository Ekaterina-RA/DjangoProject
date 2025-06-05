from django.views.generic import ListView, DetailView, TemplateView
from catalog.models import Product


class HomeView(TemplateView):
    template_name = "home.html"


class ContactsView(TemplateView):
    template_name = "contacts.html"


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'one_product.html'


