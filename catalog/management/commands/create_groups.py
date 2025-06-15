from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product


class Command(BaseCommand):
    help = 'Создает группу "Модератор продуктов" с необходимыми правами'

    def handle(self, *args, **kwargs):
        content_type = ContentType.objects.get_for_model(Product)

        # Создание или получение разрешения 'can_unpublish_product'
        can_unpublish, created = Permission.objects.get_or_create(
            codename="can_unpublish_product",
            name="Can unpublish product",
            content_type=content_type,
        )

        # Получение разрешения 'delete_product'
        delete_perm = Permission.objects.get(codename="delete_product")

        # Создание или получение группы 'Модератор продуктов'
        group, created = Group.objects.get_or_create(name="Модератор продуктов")

        # Добавление разрешений в группу
        group.permissions.add(can_unpublish, delete_perm)

        self.stdout.write(
            self.style.SUCCESS('Группа "Модератор продуктов" создана и настроена.')
        )
