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
    sort_list = []
    count = 1
    sort = CitySort.objects.order_by('aqi')
    for item in sort:
        if item.aqi is None:
            continue
        item.num = count
        sort_list.append(item)
        count += 1

    context = {
        'sort_list': sort_list,
    }
    return render(request, 'WeatherSystem/air_quality_sort.html',context)

def air_quality_map(request):
    if not request.session.get('username'):
        return render(request, 'WeatherSystem/alogin.html')

    map_data = CitySort.objects.order_by('id')
    for data in map_data:
        if data.aqi is None:
            data.aqi = 0
        if data.so2 is None:
            data.so2 = 0
        if data.co is None:
            data.co = 0
        if data.no2 is None:
            data.no2 = 0
        if data.pm10 is None:
            data.pm10 = 0
        if data.pm25 is None:
            data.pm25 = 0
        if data.o3 is None:
            data.o3 = 0
        data.province = city_to_province.get(data.city_name)
    context = {
        'map_data': map_data,
    }
    return render(request, 'WeatherSystem/air_quality_map.html', context)

city_to_province = {
 '北京'  : '北京',
 '上海'  : '上海',
 '深圳'  : '深圳',
 '天津'  : '天津',
 '重庆'  : '重庆',
 '澳门'  : '澳门',
 '香港'  : '香港',
 '海口'  : '海南',
 '台北'  : '台湾',
 '石家庄'  : '河北',
 '太原'  : '山西',
 '济南'  : '山东',
 '南京'  : '江苏',
 '杭州'  : '浙江',
 '合肥'  : '安徽',
 '福州'  : '福建',
 '南昌'  : '江西',
 '郑州'  : '河南',
 '武汉'  : '湖北',
 '长沙'  : '湖南',
 '广州'  : '广东',
 '南宁'  : '广西',
 '成都'  : '四川',
 '贵阳'  : '贵州',
 '昆明'  : '云南',
 '西安'  : '陕西',
 '兰州'  : '甘肃',
 '沈阳'  : '辽宁',
 '长春'  : '吉林',
 '哈尔滨'  : '黑龙江',
 '西宁'  : '青海',
 '银川'  : '宁夏',
 '拉萨'  : '西藏',
 '乌鲁木齐'  : '新疆',
 '呼和浩特'  : '内蒙古',
}
