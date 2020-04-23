from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from WeatherSystem.models import City,CitySort
from django.http import HttpResponseRedirect
from .forms import SearchForm,CITYCATEGORY
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def alogin(request):
    if request.POST:
        username = request.POST['usr']
        password = request.POST['pwd']
        if len(username) == 0 or len(password) == 0:
            return render(request, 'WeatherSystem/alogin.html')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            request.session['username'] = username

            return render(request, 'WeatherSystem/alogged.html')

    return render(request, 'WeatherSystem/alogin.html')

# def post_test(request):
#     city_id = request.POST['usr']
#     print("post test:", city_id)
#     # sort_list = CitySort.objects.order_by('aqi')
#     # city_list = City.objects.order_by('id')
#     # context = {
#     #     # 'sort_list': sort_list,
#     #     'city_list': city_list,
#     #     'form': SearchForm(),
#     #     'img': '../static/img/1.png',
#     # }
#     return render(request, 'WeatherSystem/alogin.html')


def alogged(request):
    if not request.session.get('username'):
        return render(request, 'WeatherSystem/alogin.html')
    return render(request, 'WeatherSystem/alogged.html')

def alogout(request):
    logout(request)
    return render(request, 'WeatherSystem/alogin.html')

def air_quality_chart(request):
    if not request.session.get('username'):
        return render(request, 'WeatherSystem/alogin.html')
    city_id = request.POST['category']
    city_list = City.objects.order_by('id')
    context = {
        'city_list': city_list,
        'form': SearchForm(),
        'img': f'../static/img/{city_id}.png',
    }
    return render(request, 'WeatherSystem/air_quality_chart.html', context)

def air_quality_sort(request):
    if not request.session.get('username'):
        return render(request, 'WeatherSystem/alogin.html')
    return render(request, 'WeatherSystem/air_quality_sort.html')

def air_quality_map(request):
    if not request.session.get('username'):
        return render(request, 'WeatherSystem/alogin.html')
    return render(request, 'WeatherSystem/air_quality_map.html')
