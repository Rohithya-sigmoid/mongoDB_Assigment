# Connecting to MongoDb

# ---------------------Task 1--------------
from pymongo import MongoClient
import json
import os
try:
    client = MongoClient("mongodb://localhost:27017/")       # Creating Connection
    db = client['sampleData']           # Creating database if it doesn't exist and switching to it

except:
    print("Error while connecting")

# Creating collections comments , movies , theaters , users

comments=db['comments']
movies = db['movies']
sessions=db['sessions']
theaters=db['theaters']
users=db['users']

# Loading json files into collections individually
# -------------------Task 2----------------
os.system('mongoimport --db sampleData --collection comments --file comments.json')
# movies
os.system('mongoimport --db sampleData --collection movies --file movies.json')
# theaters
os.system('mongoimport --db sampleData --collection theaters --file theaters.json')
# users
os.system('mongoimport --db sampleData --collection users --file users.json')
# sessions
os.system('mongoimport --db sampleData --collection sessions --file sessions.json')

# Insert data into collections
# -------------- Task 3 -------------------

def insertComments(dic):
    return movies.insert_one(dic)

def insertMovies(dic):
    return movies.insert_one(dic)

def insertSessions(dic):
    return movies.insert_one(dic)

def insertTheaters(dic):
    return movies.insert_one(dic)

def insertUsers(dic):
    return movies.insert_one(dic)



client.close()