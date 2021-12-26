from django.shortcuts import render
import joblib
import requests
from django.http import HttpResponse
import pandas as pd
from .models import Success

# Success model is a model having successful crops of a given state
# load data from csv file and store it in database
model = model = joblib.load('savedModel.sav')
def load(request):
    records = Success.objects.all()
    records.delete()
    tmp_data=pd.read_csv('state_wise_crop_success.csv')
    # create records in database
    records = [
        Success(
            State = tmp_data.iloc[row][1], 
            Crop = tmp_data.iloc[row][2],
            SuccessRate = tmp_data.iloc[row][3],
        )
        for row in range(0, len(tmp_data))
    ]

    Success.objects.bulk_create(records)
    return HttpResponse('<h1> Data loaded successfully </h1>')

# Page where User will enter the values
def index(request):
    return render(request, "main/index.html")

# Crop prediction and sending result to result.html
def result(request):
    l = []
    l.append(request.GET['N'])
    l.append(request.GET['P'])
    l.append(request.GET['K'])
    l.append(request.GET['T'])
    l.append(request.GET['Humidity'])
    l.append(request.GET['pH'])
    l.append(request.GET['Rainfall'])
    state = request.GET['State']

    # predicting the best crop for given conditions
    ans = model.predict([l])

    # get weather details of given state using openweathermap API
    weatherData=requests.get('http://api.openweathermap.org/data/2.5/weather?q='+state+'&appid=72adf46e1fc74893b5312ba1b87fd7c0')
    weatherData=weatherData.json()

    # get top 5 successful crops of given state
    res = Success.objects.filter(State=state).order_by('-SuccessRate')[:5]

    return render(request, "main/result.html", {"ans":ans, "res": res, "weatherData": weatherData})
