from django.http import JsonResponse
from rest_framework.decorators import api_view
import random
import csv
import numpy as np
import pandas as pd
from rest_framework.response import Response
array_length = 1000
random_range = 5000



@api_view(['GET'])
def bubble_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    for i in range(len(li) - 1, 0, -1):
        for j in range(i):
            if li[j] < li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    context = {
      'top': li[0]
    }
    return JsonResponse(context)

@api_view(['GET'])
def normal_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    li.sort(reverse=True)
    context = {
        'top': li[0]
    }
    return JsonResponse(context)

from queue import PriorityQueue

@api_view(['GET'])
def priority_queue(request):
    pq = PriorityQueue()
    for i in range(array_length):
        pq.put(-random.choice(range(1, random_range)))
    context = {
        'top': -pq.get()
    }
    return JsonResponse(context)




def file_open_by_numpy():
    # np.loadtxt(구분자 = ',', 데이터 타입: string)
    np_arr = pd.read_csv('data/test_data.CSV', sep=",", encoding='cp949')
    return np_arr

@api_view(['GET'])
def fileopen(request):
    
    data = file_open_by_numpy()
    df = pd.DataFrame(data)
    
    
    df.replace('', np.nan, inplace=True)
    df = df[df['나이'].notna()] 
    df.fillna('NULL', inplace=True)
   
    # df = df[df['나이'].notna()] 
    tmp = df['나이'].mean()
    
    df['diff'] = abs(df["나이"] - tmp)
    df = df.sort_values(by=['diff', '이름']).head(10)
    
    
    data2 = df.to_dict('records')
    
    
    return JsonResponse({ 'data': data2 })



    
