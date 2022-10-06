from pymongo import *


# Connecting to MongoDB
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client['sampleData']
except:
    print("Error while connecting")

theater=db['theaters']
def top10Cities():
    # Top 10 cities with the maximum number of theatres

    theaterName = db['theaters'].aggregate([
        {"$group": {"_id": {"city": "$location.address.city"}, "totalTheaters": {"$sum": 1}}},
        {"$sort": {"totalTheaters": -1}},
        {"$limit": 10},
        {"$project":{"totalTheaters": 1}}
    ])

    print("Top 10 cities with the maximum number of theatres\n")
    for i in theaterName:
        print(i)
def top10Theaters(coordinates):
    # Top 10 theatres nearby given coordinates
    #db.theaters.create_index({'location.geo':'2dsphere'})

    theaterName2= db.theaters.aggregate([
        {"$geoNear":
             {"near":
                    {"type": "Point", "coordinates": coordinates},
                    "maxDistance": 10000000,
                    "distanceField": "distance"
              }
         },
        {"$project": {"location.address.city": 1, "_id": 0, "location.geo.coordinates": 1}},
        {"$limit": 10}])


    print("\nTop 10 theatres nearby given coordinates\n")

    for i in theaterName2:
        print(i)

# -----------------Function Calling-----------------
top10Cities()
coordinates = [-118.11414 , 33.760353]
top10Theaters(coordinates)







