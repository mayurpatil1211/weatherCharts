from django.shortcuts import render
from .models import *
from .serializers import *

from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from annoying.functions import get_object_or_None
from datetime import date

import re
import requests
import urllib.request
import threading
import time
import datetime


names = ['UK', 'England', 'Wales', 'Scotland']

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'octo', 'nov', 'dec']


def maxTemp(contry):
    res = []
    response = urllib.request.Request('https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmax/date/'+contry+'.txt', headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(response) as response_opened:
        data= response_opened.read().decode("utf-8")
        data = data.split("\n")
        country = Countries.objects.filter(country=contry).first()
        for counter, value in enumerate(data):
            if counter>7:
                    year_obj={}
                    splitted_value = value.split()
                    if len(splitted_value)>=18:
                        year_obj['country'] = country.id
                        year_obj['year'] = splitted_value[0]
                        year_obj['win'] = splitted_value[len(splitted_value)-5]
                        year_obj['spr'] = splitted_value[len(splitted_value)-4]
                        year_obj['summ'] = splitted_value[len(splitted_value)-3]
                        year_obj['aut'] = splitted_value[len(splitted_value)-2]
                        year_obj['ann'] = splitted_value[len(splitted_value)-1]
                        for i in range(1, len(splitted_value)-5):
                            year_obj[months[i-1]] = splitted_value[i]
                        res.append(year_obj)
                    elif(len(splitted_value)<18 and len(splitted_value)>0):
                        year_obj['country'] = country.id
                        year_obj['year'] = splitted_value[0]
                        year_obj['win'] = splitted_value[len(splitted_value)-1]
                        for i in range(1, len(splitted_value)-1):
                            year_obj[months[i-1]] = splitted_value[i]
                        res.append(year_obj) 
                    else:
                        pass 
        MaxTemp.objects.filter(country=country.id).all().delete() 
        serializers = MaxTempSerializer(data=res, many=True)
        if serializers.is_valid():
            serializers.save()
            return 1
        return JsonResponse({'message': 'Error Occured while Adding Maximum Temperature. Try again Later'}, status=400)


def minTemp(contry):
    res = []
    response = urllib.request.Request('https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmin/date/'+contry+'.txt', headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(response) as response_opened:
        data= response_opened.read().decode("utf-8")
        data = data.split("\n")
        country = Countries.objects.filter(country=contry).first()
        for counter, value in enumerate(data):
            if counter>7:
                    year_obj={}
                    splitted_value = value.split()
                    if len(splitted_value)>=18:
                        year_obj['country'] = country.id
                        year_obj['year'] = splitted_value[0]
                        year_obj['win'] = splitted_value[len(splitted_value)-5]
                        year_obj['spr'] = splitted_value[len(splitted_value)-4]
                        year_obj['summ'] = splitted_value[len(splitted_value)-3]
                        year_obj['aut'] = splitted_value[len(splitted_value)-2]
                        year_obj['ann'] = splitted_value[len(splitted_value)-1]
                        for i in range(1, len(splitted_value)-5):
                            year_obj[months[i-1]] = splitted_value[i]
                        res.append(year_obj)
                    elif(len(splitted_value)<18 and len(splitted_value)>0):
                        year_obj['country'] = country.id
                        year_obj['year'] = splitted_value[0]
                        year_obj['win'] = splitted_value[len(splitted_value)-1]
                        for i in range(1, len(splitted_value)-1):
                            year_obj[months[i-1]] = splitted_value[i]
                        res.append(year_obj) 
                    else:
                        pass
        MinTemp.objects.filter(country=country.id).all().delete() 
        serializers = MinTempSerializer(data=res, many=True)
        if serializers.is_valid():
            serializers.save()
            return 1
        return JsonResponse({'message': 'Error Occured while Adding Minimum Temperature. Try again Later'}, status=400)

def meanTemp(contry):
    res = []
    response = urllib.request.Request('https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmean/date/'+contry+'.txt', headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(response) as response_opened:
        data= response_opened.read().decode("utf-8")
        data = data.split("\n")
        country = Countries.objects.filter(country=contry).first()
        for counter, value in enumerate(data):
            if counter>7:
                    year_obj={}
                    splitted_value = value.split()
                    if len(splitted_value)>=18:
                        year_obj['country'] = country.id
                        year_obj['year'] = splitted_value[0]
                        year_obj['win'] = splitted_value[len(splitted_value)-5]
                        year_obj['spr'] = splitted_value[len(splitted_value)-4]
                        year_obj['summ'] = splitted_value[len(splitted_value)-3]
                        year_obj['aut'] = splitted_value[len(splitted_value)-2]
                        year_obj['ann'] = splitted_value[len(splitted_value)-1]
                        for i in range(1, len(splitted_value)-5):
                            year_obj[months[i-1]] = splitted_value[i]
                        res.append(year_obj)
                    elif(len(splitted_value)<18 and len(splitted_value)>0):
                        year_obj['country'] = country.id
                        year_obj['year'] = splitted_value[0]
                        year_obj['win'] = splitted_value[len(splitted_value)-1]
                        for i in range(1, len(splitted_value)-1):
                            year_obj[months[i-1]] = splitted_value[i]
                        res.append(year_obj) 
                    else:
                        pass  
        MeanTemp.objects.filter(country=country.id).all().delete() 
        serializers = MeanTempSerializer(data=res, many=True)
        if serializers.is_valid():
            serializers.save()
            return 1
        return JsonResponse({'message': 'Error Occured while Adding Mean Temperature. Try again Later'}, status=400)

def sunshine(contry):
    res = []
    response = urllib.request.Request('https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Sunshine/date/'+contry+'.txt', headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(response) as response_opened:
        data= response_opened.read().decode("utf-8")
        data = data.split("\n")
        country = Countries.objects.filter(country=contry).first()
        for counter, value in enumerate(data):
            if counter>7:
                    year_obj={}
                    splitted_value = value.split()
                    if len(splitted_value)>=18:
                        year_obj['country'] = country.id
                        year_obj['year'] = splitted_value[0]
                        year_obj['win'] = splitted_value[len(splitted_value)-5]
                        year_obj['spr'] = splitted_value[len(splitted_value)-4]
                        year_obj['summ'] = splitted_value[len(splitted_value)-3]
                        year_obj['aut'] = splitted_value[len(splitted_value)-2]
                        year_obj['ann'] = splitted_value[len(splitted_value)-1]
                        for i in range(1, len(splitted_value)-5):
                            year_obj[months[i-1]] = splitted_value[i]
                        res.append(year_obj)
                    elif(len(splitted_value)<18 and len(splitted_value)>0):
                        year_obj['country'] = country.id
                        year_obj['year'] = splitted_value[0]
                        year_obj['win'] = splitted_value[len(splitted_value)-1]
                        for i in range(1, len(splitted_value)-1):
                            year_obj[months[i-1]] = splitted_value[i]
                        res.append(year_obj) 
                    else:
                        pass

        Sunshine.objects.filter(country=country.id).all().delete() 
        serializers = SunshineSerializer(data=res, many=True)
        if serializers.is_valid():
            serializers.save()
            return 1
        return JsonResponse({'message': 'Error Occured while Adding Sunshine Readings. Try again Later'}, status=400)

def rainfall(contry):
    res = []
    response = urllib.request.Request('https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Rainfall/date/'+contry+'.txt', headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(response) as response_opened:
        data= response_opened.read().decode("utf-8")
        data = data.split("\n")
        country = Countries.objects.filter(country=contry).first()
        for counter, value in enumerate(data):
            if counter>7:
                    year_obj={}
                    splitted_value = value.split()
                    if len(splitted_value)>=18:
                        year_obj['country'] = country.id
                        year_obj['year'] = splitted_value[0]
                        year_obj['win'] = splitted_value[len(splitted_value)-5]
                        year_obj['spr'] = splitted_value[len(splitted_value)-4]
                        year_obj['summ'] = splitted_value[len(splitted_value)-3]
                        year_obj['aut'] = splitted_value[len(splitted_value)-2]
                        year_obj['ann'] = splitted_value[len(splitted_value)-1]
                        for i in range(1, len(splitted_value)-5):
                            year_obj[months[i-1]] = splitted_value[i]
                        res.append(year_obj)
                    elif(len(splitted_value)<18 and len(splitted_value)>0):
                        year_obj['country'] = country.id
                        year_obj['year'] = splitted_value[0]
                        year_obj['win'] = splitted_value[len(splitted_value)-1]
                        for i in range(1, len(splitted_value)-1):
                            year_obj[months[i-1]] = splitted_value[i]
                        res.append(year_obj) 
                    else:
                        pass

        Rainfall.objects.filter(country=country.id).all().delete()
        serializers = RainfallSerializer(data=res, many=True)
        if serializers.is_valid():
            serializers.save()
            return 1
        return JsonResponse({'message': 'Error Occured while Adding Rainfall Readings. Try again Later'}, status=400)


############---------------With Thread----------------###################
@api_view(['POST'])
def save_data(request):
	threads_list = []
	start_time = time.time()
	for i in names:
		t = threading.Thread(target=maxTemp, name='thread{}'.format(i), args=(i,))
		threads_list.append(t)
		t.start()
		# time.sleep(5)
		t1 = threading.Thread(target=minTemp, name='thread{}'.format(i), args=(i,))
		threads_list.append(t1)
		t1.start()
		# time.sleep(5)
		t2 = threading.Thread(target=meanTemp, name='thread{}'.format(i), args=(i,))
		threads_list.append(t2)
		t2.start()
		# time.sleep(5)
		t3 = threading.Thread(target=rainfall, name='thread{}'.format(i), args=(i,))
		threads_list.append(t3)
		t3.start()
		# time.sleep(5)
		t4 = threading.Thread(target=sunshine, name='thread{}'.format(i), args=(i,))
		threads_list.append(t4)
		t4.start()

	for t in threads_list:
		t.join()

	end = time.time()-start_time
	print(end)
	return JsonResponse({'message':'Data saved'}, status=200)



#################------Without Threading-----------------##################
# @api_view(['POST'])
# def save_data(request):
# 	start_time = time.time()
# 	for i in names:
# 		maxTemp(i)
# 		minTemp(i)
# 		meanTemp(i)
# 		rainfall(i)
# 		sunshine(i)
# 	end = time.time()-start_time
# 	print(end)
# 	return JsonResponse({'message':'Data saved'}, status=200)


##########################-----------GET ALL DATA--------------#############
def maxTempSearch(country, year):
    maxTemp = MaxTemp.objects.filter(country=country, year=year).first()
    serializers = GetMaxTempSerializer(maxTemp)
    labels = [i for i in serializers.data]
    values = [str(serializers.data.get(i)) for i in serializers.data]
    return labels, values

def minTempSearch(country, year):
    maxTemp = MinTemp.objects.filter(country=country, year=year).first()
    serializers = GetMinTempSerializer(maxTemp)
    labels = [i for i in serializers.data]
    values = [str(serializers.data.get(i)) for i in serializers.data]
    return labels, values

def meanTempSearch(country, year):
    maxTemp = MeanTemp.objects.filter(country=country, year=year).first()
    serializers = GetMeanTempSerializer(maxTemp)
    labels = [i for i in serializers.data]
    values = [str(serializers.data.get(i)) for i in serializers.data]
    return labels, values

def rainFallSearch(country, year):
    maxTemp = Rainfall.objects.filter(country=country, year=year).first()
    serializers = GetRainfallSerializer(maxTemp)
    labels = [i for i in serializers.data]
    values = [str(serializers.data.get(i)) for i in serializers.data]
    return labels, values

def sunshineSearch(country, year):
    maxTemp = Sunshine.objects.filter(country=country, year=year).first()
    serializers = GetSunshineSerializer(maxTemp)
    labels = [i for i in serializers.data]
    values = [str(serializers.data.get(i)) for i in serializers.data]
    return labels, values

@api_view(['GET'])
def get_data(request, country=None, year=None):
    start_time = time.time()
    search_result={}
    search_result['maxTemp'] = {}
    search_result['minTemp'] = {}
    search_result['meanTemp'] = {}
    search_result['rainfall'] = {}
    search_result['sunshine'] = {}
    if country:
        country_obj =Countries.objects.filter(country=country).first()
    else:
        country_obj =Countries.objects.filter(country='UK').first()
    if(year):
        year = year
    else:
        year = datetime.datetime.strftime(datetime.datetime.today(), "%Y")
    search_result['maxTemp']['labels'], search_result['maxTemp']['value'] =maxTempSearch(country_obj.id, year)
    search_result['minTemp']['labels'], search_result['minTemp']['value'],=minTempSearch(country_obj.id, year)
    search_result['meanTemp']['labels'], search_result['meanTemp']['value']=meanTempSearch(country_obj.id, year)
    search_result['rainfall']['labels'], search_result['rainfall']['value']=rainFallSearch(country_obj.id, year)
    search_result['sunshine']['labels'], search_result['sunshine']['value']=sunshineSearch(country_obj.id, year)
    search_result['year'] = year
    search_result['country'] = country_obj.country
    end = time.time()-start_time
    print(end)
    return JsonResponse({'result':search_result}, status=200)


@api_view(['GET'])
def get_year(request):
    years = MaxTemp.objects.values('year').distinct().order_by('year')
    year_list = [i['year'] for i in years]
    return JsonResponse({'years':year_list}, status=200)