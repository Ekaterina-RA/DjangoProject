from config.settings import CACHE_ENABLED
from .models import Product
from django.core.cache import cache


def get_products_by_category(category_id):
    if not CACHE_ENABLED:
        return Product.objects.filter(category_id=category_id)
    key = "category_products"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products
