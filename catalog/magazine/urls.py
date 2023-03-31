from django.urls import path
from .views import detail_product, index

app_name = 'magazine'

urlpatterns = [
    path('', index, name='index'),
    path('detail-info/', detail_product, name='data_product'),
]
