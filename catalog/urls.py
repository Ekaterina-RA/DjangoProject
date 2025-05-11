from django.urls import path, include
from catalog import views, admin
from catalog.apps import CatalogConfig


app_name = CatalogConfig.name
urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('contacts/', views.contacts, name='contacts'),  # Страница контактов
]