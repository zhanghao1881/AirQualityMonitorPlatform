from django.urls import path

from . import views

app_name = 'WeatherSystem'
urlpatterns = [
    # ex: /WeatherSystem/
    path('', views.login, name='login'),
    path('login', views.login, name='login'),
    path('logged', views.logged, name='logged'),
    path('chart', views.air_quality_chart, name='air_quality_chart'),
    path('map', views.air_quality_map, name='air_quality_map'),
    path('sort', views.air_quality_sort, name='air_quality_sort'),
    path('post_test', views.post_test, name='post_test'),
    # # ex: /WeatherSystem/5/
    # path('<city_name>/', views.detail, name='detail'),
    # # ex: /WeatherSystem/5/results/
    # path('<int:city_name>/results/', views.results, name='results'),
    # # ex: /WeatherSystem/5/vote/
    # path('<int:city_name>/vote/', views.vote, name='vote'),
]