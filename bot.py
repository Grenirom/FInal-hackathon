# import telebot
# import os
# import django
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mainapp.settings')
# django.setup()
# from django.conf import settings
# from django.core.wsgi import get_wsgi_application
# from category.models import Category
# import django
# import os
# import sys
# from datetime import timedelta
# from pathlib import Path
# from decouple import config
#
# TOKEN = '5716880333:AAFffbdc3qk0vFei3D037eAJwOjNbjYLQVs'
#
# BASE_DIR = Path(__file__).resolve().parent.parent
# # DJANGO_SETTINGS_MODULE
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mainapp.settings')
# os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
#
# django.setup()
#
# bot = telebot.TeleBot(TOKEN)
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     categories = Category.objects.all()
#     category_names = [category.title for category in categories]
#     print(category_names)
#     message_text = '\n'.join(category_names)
#     bot.send_message(message.chat.id, message_text)
#
#
# application = get_wsgi_application()
#
# if __name__ == '__main__':
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mainapp.settings')
#     os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
#     from django.core.management import execute_from_command_line
#     bot.polling()
#
# _____________________________________________________________________________________________-
# import telebot
# import os
# import django
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mainapp.settings')
# django.setup()
# from django.conf import settings
# from django.core.wsgi import get_wsgi_application
# from category.models import Category
# import django
# import os
# import sys
# from datetime import timedelta
# from pathlib import Path
# from decouple import config
#
# TOKEN = '5716880333:AAFffbdc3qk0vFei3D037eAJwOjNbjYLQVs'
#
# BASE_DIR = Path(__file__).resolve().parent.parent
# # DJANGO_SETTINGS_MODULE
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mainapp.settings')
# os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
#
# django.setup()
#
# bot = telebot.TeleBot(TOKEN)
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     categories = Category.objects.all()
#     category_names = [category.slug for category in categories]
#     print(category_names)
#     message_text = '\n'.join(category_names)
#     bot.send_message(message.chat.id, message_text)
#
#
# application = get_wsgi_application()
#
# if __name__ == '__main__':
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mainapp.settings')
#     os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
#     from django.core.management import execute_from_command_line
#     bot.polling()
#

import telebot
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mainapp.settings')
django.setup()
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from category.models import Category
import django
import os
import sys
from datetime import timedelta
from pathlib import Path
from decouple import config
from telebot import types
from comics.models import Comics
from news.models import New
from movies.models import Movie

TOKEN = '5716880333:AAFffbdc3qk0vFei3D037eAJwOjNbjYLQVs'

BASE_DIR = Path(__file__).resolve().parent.parent
# DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mainapp.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

django.setup()

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    categories = Category.objects.all()
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    category_names = [category.slug for category in categories]
    for x in category_names:
        button = types.InlineKeyboardButton(f'{x}', callback_data=f'{x}')
        keyboard.add(button)
    bot.send_message(message.chat.id, 'Выберите категоирию:', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == 'comics':
        list_ = []
        categories_in = Comics.objects.filter(category='comics')[0]
        name = list_.append(categories_in.name.replace('\'', ''))
        desc = list_.append(categories_in.description.replace('\'', ''))
        price = list_.append(str(categories_in.price))
        message_text = '\n'.join(list_)
        bot.send_message(call.message.chat.id,
                         f'{message_text}')

    elif call.data == 'news':
        list_ = []
        categories_in = New.objects.filter(category='news')[0]
        title = list_.append(categories_in.title)
        body = list_.append(categories_in.body)
        message_text = '\n'.join(list_)
        bot.send_message(call.message.chat.id,
                         f'{message_text}')

    elif call.data == 'movie':
        list_ = []
        categories_in = Movie.objects.filter(category='movie')[0]
        title = list_.append(categories_in.title)
        desc = list_.append(categories_in.description)
        price = list_.append(str(categories_in.price))
        release = list_.append(str(categories_in.release_date))
        message_text = '\n'.join(list_)
        bot.send_message(call.message.chat.id,
                         f'{message_text}')


application = get_wsgi_application()

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mainapp.settings')
    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
    from django.core.management import execute_from_command_line

    bot.polling()
