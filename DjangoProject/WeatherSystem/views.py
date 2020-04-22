from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from WeatherSystem.models import City,CitySort
from django.http import HttpResponseRedirect
from .forms import SearchForm,CITYCATEGORY

# Create your views here.
def login(request):
    if request.POST:
        usr = request.POST['usr']
        pwd = request.POST['pwd']
        print(f"login:{usr}, pwd:{pwd}")
        return render(request, 'WeatherSystem/logged.html')
    else:
        return render(request, 'WeatherSystem/login.html')

def post_test(request):
    city_id = request.POST['usr']
    print("post test:", city_id)
    # sort_list = CitySort.objects.order_by('aqi')
    # city_list = City.objects.order_by('id')
    # context = {
    #     # 'sort_list': sort_list,
    #     'city_list': city_list,
    #     'form': SearchForm(),
    #     'img': '../static/img/1.png',
    # }
    return render(request, 'WeatherSystem/login.html')

def logged(request):
    sort_list = CitySort.objects.order_by('aqi')
    city_list = City.objects.order_by('id')
    context = {
        # 'sort_list': sort_list,
        'city_list': city_list,
        'form': SearchForm(),
        'img': '../static/img/1.png',
    }
    return render(request, 'WeatherSystem/logged.html', context)

def air_quality_chart(request):
    sort_list = CitySort.objects.order_by('aqi')
    city_list = City.objects.order_by('id')
    context = {
        # 'sort_list': sort_list,
        'city_list': city_list,
        'form': SearchForm(),
        'img': '../static/img/1.png',
    }
    return render(request, 'WeatherSystem/air_quality_chart.html', context)


def air_quality_sort(request):
    sort_list = CitySort.objects.order_by('aqi')
    city_list = City.objects.order_by('id')
    context = {
        # 'sort_list': sort_list,
        'city_list': city_list,
        'form': SearchForm(),
        'img': '../static/img/1.png',
    }
    return render(request, 'WeatherSystem/air_quality_sort.html', context)

def air_quality_map(request):
    sort_list = CitySort.objects.order_by('aqi')
    city_list = City.objects.order_by('id')
    context = {
        # 'sort_list': sort_list,
        'city_list': city_list,
        'form': SearchForm(),
        'img': '../static/img/1.png',
    }
    return render(request, 'WeatherSystem/air_quality_map.html', context)
