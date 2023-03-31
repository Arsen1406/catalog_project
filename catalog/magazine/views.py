import requests
from django.shortcuts import render

from .form import ArticleForm

API_SERVICE = (
    'https://api.forum-auto.ru/v2/listGoods?'
    'login=493358_stroyzar&pass=sAVDkrEbqd&art={}'
)


def index(request):
    form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'index.html', context)


def detail_product(request):
    article = request.GET
    product_data = requests.get(
        API_SERVICE.format(article.get('article'))).json()
    context = {
        'product_data': product_data
    }
    template = 'product_detail.html'
    return render(request, template, context)


def demo_page(request):
    return render(request, 'demo.html')
