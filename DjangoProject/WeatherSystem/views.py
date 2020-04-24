from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from WeatherSystem.models import City,CitySort
from django.http import HttpResponseRedirect
from .forms import SearchForm,CITYCATEGORY
from django.contrib.auth import authenticate,login,logout
from PlotUtils.plot import Plot
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
    img_list = []
    city_img = None
    if not request.session.get('username'):
        return render(request, 'WeatherSystem/alogin.html')
    if request.POST:
        ret_id = request.POST.getlist('category')
        if len(ret_id) == 1:
            city_img = f'../static/img/{ret_id[0]}.png'
            img_list = []
        else:
            city_img = None
            img_list = list(map(lambda name: f'../static/img/{name}.png',
                                ['aqi', 'pm25', 'pm10', 'co', 'so2', 'no2', 'o3']))
            Plot().plot_single(ret_id)
    context = {
        'form': SearchForm(),
        'img': city_img,
        'img_list': img_list,
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
