from django.urls import path
from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, HomeView, ContactsView

app_name = CatalogConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path('product_detail/', ProductListView.as_view(), name='product_detail'),
    path('one_product/<int:pk>/', ProductDetailView.as_view(), name='one_product'),
]
