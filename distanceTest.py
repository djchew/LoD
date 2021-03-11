from fastapi import FastAPI
import uvicorn
import json
import csv
import os
import pandas as pd
from math import radians, cos, sin, asin, sqrt

#Init
app = FastAPI(debug = True)


os.chdir('C:/Users/darre/Desktop/LoD hire test/FASTAPI')

coord = 'coordinates.csv'
df = pd.read_csv(coord, sep = ',', header = 0)
long1 = df['long1']
long2 = df["long2"]
lat1 = df["lat1"]
lat2 = df["lat2"]

@app.get('/api/v2/coordinates')
# Calculate haversine 
def haversine(lat1, long1, lat2, long2):

    radius = 6372.8 

    dLat = radians(lat2 - lat1)
    dLon = radians(long2 - long1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
    c = 2*asin(sqrt(a))

    # Returns distance in meters
    return radius * c * 1000 




if __name__ == '__main__':
    uvicorn.run(app, host = "127.0.0.1", port = "80")