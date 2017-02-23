#! /usr/bin/python

"""
Author: Luis Manuel Roman Garcia

"""

from lxml import etree
import pandas as pd
import numpy as np
import urllib2
import xmltodict
from datetime import datetime
from sqlalchemy import create_engine

## readXML
def readXML(url):
    """
    This function reads an xml from
    the given url and returns a dictionary
    with the same structure.
    """
    file = urllib2.urlopen(url)
    data = file.read()
    file.close()
    data = xmltodict.parse(data)
    return data

## Read in data
prices = readXML('https://datos.gob.mx/api/gasolina/prices.xml')
places = readXML('https://datos.gob.mx/api/gasolina/places.xml')


## Joint data-set
gasType     = []
gasPrice    = []
gasTime     = []
gasDate     = []
gasCat      = []
gasLon      = []
gasLat      = []
for i in range(len(places['places']['place'])):
    if 'gas_price' in prices['places']['place'][i]:
        price = prices['places']['place'][i]['gas_price']
        place = places['places']['place'][i]
        if isinstance(price, list):
            for j in range(len(price)):
                timeDate = price[j]['@update_time'].split('T')
                gasType.append(price[j]['@type'])
                gasPrice.append(price[j]['#text'])
                gasTime.append(timeDate[1].split('.')[0])
                gasDate.append(timeDate[0])
                gasCat.append(place['category'])
                gasLon.append(place['location']['x'])
                gasLat.append(place['location']['y'])
        else:
            timeDate = price['@update_time'].split('T')
            gasType.append(price['@type'])
            gasPrice.append(price['#text'])
            gasTime.append(timeDate[1].split('.')[0])
            gasDate.append(timeDate[0])
            gasCat.append(place['category'])
            gasLon.append(place['location']['x'])
            gasLat.append(place['location']['y'])

## Unify in dictionary
all_data = {"type":gasType, "price":gasPrice, "date":gasDate, "time":gasTime, "lon":gasLon, "lat":gasLat}
## Get dataset
df = pd.DataFrame.from_dict(all_data)
## Save results
## df.to_csv("../data/price_place.csv")
## engine = create_engine('postgresql://scott:tiger@localhost:5432/mydatabase')
## df.to_sql('table_name', engine)
