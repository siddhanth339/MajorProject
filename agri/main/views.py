from django.shortcuts import render
import joblib
import requests
#from django.contrib.gis.utils import GeoIP

def index(request):
   # g = GeoIP()
    ip = request.META.get('REMOTE_ADDR', None)
    result=requests.get('http://ipwhois.app/json/'+str(ip))
    data=result.json()
    print("api response:")
    print(data)
    """
        if ip:
        print("ip: " + str(ip))
        city = g.city(ip)
        print("city: ")
        print(city)
        city = g.city(ip)['city']
        print("city explicitly mentioned: ")
        print(city)
        lon_lat = g.lon_lat(ip)
        print("lon_lat:")
        print(lon_lat)
    else:
        city = 'Rome' # default city
    """
    print("ip: " + str(ip))
    return render(request, "main/index.html")

def result(request):
    model = joblib.load('savedModel.sav')
    l = []
    l.append(request.GET['N'])
    l.append(request.GET['P'])
    l.append(request.GET['K'])
    l.append(request.GET['T'])
    l.append(request.GET['Humidity'])
    l.append(request.GET['pH'])
    l.append(request.GET['Rainfall'])

    ans = model.predict([l])

    return render(request, "main/result.html", {"ans":ans})