from django.urls import path
from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import product_detail, one_product


app_name = CatalogConfig.name
urlpatterns = [
    path("", views.home, name="home"),
    #path("contacts/", views.contacts, name="contacts"),
    path('product_detail/', product_detail, name='product_detail'),
    path('one_product/<int:pk>/', one_product, name='one_product'),
]
