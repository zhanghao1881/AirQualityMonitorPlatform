from django.urls import path

from . import views

app_name = 'WeatherSystem'
urlpatterns = [
    # ex: /WeatherSystem/
    path('', views.alogin, name='alogin'),
    path('alogin', views.alogin, name='alogin'),
    path('alogged', views.alogged, name='alogged'),
    path('alogout', views.alogout, name='alogout'),
    path('chart', views.air_quality_chart, name='air_quality_chart'),
    path('map', views.air_quality_map, name='air_quality_map'),
    path('sort', views.air_quality_sort, name='air_quality_sort'),
]