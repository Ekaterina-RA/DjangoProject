from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Удаляет все продукты и категории, затем добавляет тестовые данные"

    def handle(self, *args, **kwargs):
        # Удаление всех данных
        self.stdout.write("Удаление всех продуктов")
        Product.objects.all().delete()
        self.stdout.write("Удаление всех категорий")
        Category.objects.all().delete()

        # Создание категорий
        self.stdout.write("Создание категорий")

        category_books = Category.objects.create(
            name="Книги", description="Литература и учебники"
        )
        category_clothing = Category.objects.create(
            name="Одежда", description="Модная одежда"
        )

        # Создание продуктов
        self.stdout.write("Добавление тестовых продуктов")

        Product.objects.create(
            name="Роман",
            description="Популярный роман",
            image="products/roman.jpg",
            category=category_books,
            price=500.00,
        )
        Product.objects.create(
            name="Футболка",
            description="Мягкая хлопковая футболка",
            image="products/tshirt.jpg",
            category=category_clothing,
            price=1500.00,
        )

        Product.objects.create(
            name="Учебник",
            description="Учебник по математике",
            image="products/textbook.jpg",
            category=category_books,
            price=800.00,
        )

        self.stdout.write(self.style.SUCCESS("Тестовые продукты успешно добавлены!"))
