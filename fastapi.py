
from fastapi import FastAPI
import uvicorn
import json
from math import radians, cos, sin, asin, sqrt

#Init
app = FastAPI(debug = True)

with open("coordinates.json") as c:
    coordinates = json.load(c)
    long1 = coordinates["long1"]
    long2 = coordinates["long2"]
    lat1 = coordinates["lat1"]
    lat2 = coordinates["lat2"]

@app.get('/api/v2/coordinates')
# Calculate haversine 
def haversine(lat1, long1, lat2, long2):

    R = 6372.8 # this is in miles.  For Earth radius in kilometers use 6372.8 km

    dLat = radians(lat2 - lat1)
    dLon = radians(long2 - long1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
    c = 2*asin(sqrt(a))

    # Returns distance in meters
    return R * c * 1000 


if __name__ == '__main__':
    uvicorn.run(app, host = "127.0.0.1", port = "80")