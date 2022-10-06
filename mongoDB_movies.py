from pymongo import MongoClient
import re
# Connecting to MongoDB
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client['sampleData']
except:
    print("Error while connecting")

movies=db['movies']

n = int(input("n : "))

# -------------------------Top N movies------------------------
def topNMovies():
    print('--------------Movies Query---------------')
    # i) Top N movies with highest imdb rating
    movies1= db['movies'].aggregate([
        {'$project': {'title': '$title','rating': '$imdb.rating'}},
        {'$match': {'rating': {'$exists': True,'$ne': ''}}},
        {'$group': {'_id': {'rating': '$rating','title': '$title'}}},
        {'$sort': {'_id.rating': -1}},
        {'$limit': n}
    ])

    print(f"\nTop {n} movies with highest imdb rating\n")
    for movieName in movies1:
        print(movieName)

    # ii) Top N movies with the highest IMDB rating in a given year

    year = int(input("\nYear: "))
    movies2= db['movies'].aggregate([
        {'$project': {"year": {"$year": "$released"}, "rating": "$imdb.rating", "title": "$title"}},
        {'$match': {"year": year,'rating': {'$exists': True,'$ne': ''}}},
        {'$group': {"_id": {"title": "$title", "rating": "$rating"}}},
        {'$sort': {"_id.rating": -1}},
        {'$limit': n}
    ])
    print(f"\nTop {n} movies with the highest IMDB rating in {year}\n")
    count=0
    for i in movies2:
        count+=1
        print(i)
    if count<n:
        print(f"\nOnly {count} movies released in that year\n")

    # iii) Top N movies with highest IMDB rating with number of votes > 1000

    movies3 =db['movies'].aggregate([
        {'$project': {'votes': '$imdb.votes', 'rating': '$imdb.rating', 'title': '$title'}},
        {'$match': {'votes': {'$gt': 1000}}},
        {'$group': {'_id': {'title': '$title', 'rating': '$rating', 'votes': '$votes'}}},
        {'$sort': {'_id.rating': -1, '_id.votes': -1}},
        {'$limit': n}
    ])


    print(f"\nTop {n} movies with highest IMDB rating with number of votes > 1000\n")
    for i in movies3:
        print(i)

    # iv) Top N movies with title matching a given pattern sorted by highest tomatoes ratings
    patternString = input("\nEnter string you want to match: ")
    regxString = re.compile(patternString)
    movies4 = db['movies'].aggregate([
        {'$project': {'title': '$title', 'rating': '$tomatoes.viewer.rating'}},
        {'$match': {'title':regxString }},
        {'$group': {'_id': {'rating': '$rating', 'title': '$title' }}},
        {'$sort': {'_id.rating': -1}},
        {'$limit': n}
    ])

    print(f"\nTop {n} movies with title matching a given pattern sorted by highest tomatoes ratings\n")
    for i in movies4:
        print(i)

topNMovies()




