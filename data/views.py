from django.shortcuts import render
from django.shortcuts import render
from math import sqrt
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
from sqlalchemy import create_engine
import pandas as pd
import jsonpickle
import numpy as np
from sqlalchemy import create_engine,text
import pandas as pd
from pandas.tseries.frequencies import to_offset
import os
import pymongo

from math import sqrt
import json

# Create your views here.


dataset = pd.read_csv('dataset.csv')
myclient = pymongo.MongoClient("mongodb://50.116.32.224:27017/")

mydb = myclient["stockdataicici"]

mycol = mydb["customers"]

@api_view(['GET'])
def get_data(request,name):
    sam = name
    print(sam)
    #datan = {}
    #datan1 = {}
    try:
        token=dataset[dataset['ShortName']==str(sam)].Token
        token=token.values[0]
        complete_token="4.1!"+token
        print(complete_token)
        m = mycol.find({"symbol":complete_token})
        print(m)
        #datan = {}

        #datan = [x for x in m]
        #datan.pop('_id')
        datan={}
        da=list()

        for x in m :
            datan['symbol'] = x['symbol']
            datan['close']= x['close']
            datan['time'] = str(x['time'])
            da.append(datan)
        print((da))
        return Response((da))
    except:
        return Response("no data")
