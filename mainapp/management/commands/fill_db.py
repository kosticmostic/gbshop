from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
from authapp.models import ShopUser

import json, os

JSON_PATH = 'mainapp/json'


def loadFromJSON(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = loadFromJSON('categories')
        print(categories)

        ProductCategory.objects.all().delete()
        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

        products = loadFromJSON('products')

        Product.objects.all().delete()
        for product in products:
            category_name = product["category"]
            # Получаем категорию по имени
            _category = ProductCategory.objects.get(name=category_name)
            # Заменяем название категории объектом
            product['category'] = _category
            new_product = Product(**product)
            new_product.save()
            # super_user = User.objects.create_superuser('admin', 'admin@admin.ru', 'admin')
        ShopUser.objects.all().delete()
        ShopUser.objects.create_superuser('adm', 'adm@adm.ru', 'adm', age=33)
        ShopUser.objects.create_user('test', 'te@te.ru', '12345')

#
# from django.core.management.base import BaseCommand
# # from django.contrib.auth.models import User
#
# from mainapp.models import ProductCategory
# from authapp.models import ShopUser


# class Command(BaseCommand):
#     def handle(self, *args, **options):
#
#         # ProductCategory.objects.all().delete()
#         #
#         # for x in range(5):
#         #     new_cat = ProductCategory()
#         #     new_cat.save()
#
#         # User.objects.create_superuser(
#         #     'manchenkov123', 'test@test.com', 'root'
#         # )
#
#         ShopUser.objects.create_superuser(
#             'kus', 'test@test.com', 'root', age=20
#         )
#         ShopUser.objects.create_user('test', 'te@te.ru', '12345')
