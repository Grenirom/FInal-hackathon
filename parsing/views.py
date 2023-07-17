import json
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from django.shortcuts import render
import time
from . import serializers
from bs4 import BeautifulSoup as bs
from json import dumps
import requests
from multiprocessing import Pool

from parsing.models import ParsingModel
from .serializers import ParsingSerializer

link_main = 'https://www.film.ru/compilation/vselennaya-marvel'


def get_html(url):
    response = requests.get(url).text
    soup = bs(response, 'lxml')
    return soup


def get_list_of_urls(link):
    html = get_html(link)
    list_ = html.find_all('a', class_='film_list_link')
    list_of_urls = []
    zero = 0
    for x in list_:
        zero += 1
        df = x['href']
        list_of_urls.append('https://www.film.ru' + df)
    return list_of_urls


def get_title_of_each_page(link_main):
    urls = get_list_of_urls(link_main)
    list_ = []
    for x in urls:
        html = get_html(x)
        title = html.find('div', class_='wrapper_movies_top_main_right').find('h1').text.strip()
        index_of_scobka = title.index('(')
        title = title[:index_of_scobka]
        description = html.find('div', class_='block_info').text.strip()
        dict_ = {"name": title, "description": description.replace('\n', '')}
        list_.append(dict_)
    json_data = dumps(list_, ensure_ascii=False)
    return json_data


# get_title_of_each_page(link_main)
class ParsingListAPIView(APIView):
    def get(self, request):
        start = time.time()
        json_data = get_title_of_each_page(link_main)
        data = json.loads(json_data)
        serializer = ParsingSerializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        end = time.time()
        return Response({'msg':f'Время выполнения {end-start}','data':serializer.data}, status=201)





























