from django.urls import path
from .views import detail_product, index, demo_page

app_name = 'magazine'

urlpatterns = [
    path('', index, name='index'),
    path('demo-page/', demo_page, name='demo'),
    path('detail-info/', detail_product, name='data_product'),
]
