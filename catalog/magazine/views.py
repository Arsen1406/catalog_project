import requests as req
from django.shortcuts import render

from .form import ArticleForm

API_SERVISE = 'https://api.forum-auto.ru/v2/listGoods?login=493358_stroyzar&pass=sAVDkrEbqd&art={}'


def index(request):
    form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'index.html', context)


def detail_product(request):
    article = request.GET
    product_data = req.get(API_SERVISE.format(article.get('article'))).json()
    context = {
        'product_data': product_data
    }
    template = 'product_detail.html'
    return render(request, template, context)
