from django.shortcuts import render
from django.http import HttpRequest



def main(request:HttpRequest):
    tittle = 'главная'
    content = {
        'tittle': tittle
    }
    return render(request, 'mainapp/index.html', content)


def products(request:HttpRequest):
    tittle = 'продукты'

    links_menu = [
        {'href': '#1', 'name': 'все'},
        {'href': '#2', 'name': 'дом'},
        {'href': '#3', 'name': 'офис'},
        {'href': '#4', 'name': 'модерн'},
        {'href': '#5', 'name': 'классика'},
    ]

    content = {
        'tittle': tittle,
        'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', content)


def contact(request:HttpRequest):
    tittle = 'контакты'
    locations = [
        {
            'city': 'Москва',
            'phone': '+7-888-888-8888',
            'email': 'info@geekshop.ru',
            'address': 'В пределах МКАД',
        },
        {
            'city': 'Оренбург',
            'phone': '+7-777-777-7777',
            'email': 'info_oren@geekshop.ru',
            'address': 'Далеко за мкадом',
        },
        {
            'city': 'Бузулук',
            'phone': '+7-999-999-9999',
            'email': 'info_derevenka@geekshop.ru',
            'address': 'Близко к лесу',
        },
    ]
    content = {
        'tittle': tittle,
        'locations': locations
    }
    return render(request, 'mainapp/contact.html', content)
