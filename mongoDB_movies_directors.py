# --------------------Top N directors ----------------------------
from pymongo import MongoClient
# Connecting to MongoDB
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client['sampleData']
except:
    print("Error while connecting")

movies=db['movies']

n = int(input("n : "))


def topNDirectors():
    print('\n--------------Directors Query---------------')
    # i) Top N directors who created the maximum number of movies
    directors1 = db['movies'].aggregate([
        {'$unwind':'$directors'},
        {'$project': {'directors': '$directors'}},
        {'$match':{'directors':{'$exists':True,'$ne':''}}},
        {'$group': {'_id': '$directors','totalMovies':{'$sum':1}}},
        {'$sort': {'totalMovies': -1}},
        {'$limit': n}
    ])
    print(f"\nTop {n} directors who created the maximum number of movies\n")
    for i in directors1:
        print(i)

    # ii) Top N directors who created the maximum number of movies in a given year
    year = int(input("Year: "))

    directors2 = db['movies'].aggregate([
        {'$unwind':'$directors'},
        {'$project': {'year':{'$year':'$released'},'directors': '$directors'}},
        {'$match': {'year': year,'directors': {'$exists': True,'$ne': ''}}},
        {'$group': {'_id': '$directors','totalMovies':{'$sum':1}}},
        {'$sort': {'totalMovies': -1}},
        {'$limit': n}
    ])
    print(f"\nTop {n} directors who created the maximum number of movies in a year {year}\n")
    count=0

    for i in directors2:
        count+=1
        print(i)

    if count<n:
        print(f"\nOnly {count} movies released in that year\n")

    # iii) Top N directors who created the maximum number of movies for a given genre
    genre = input("\nEnter the genre you want to query on: ")
    directors3 = db['movies'].aggregate([
        {'$unwind': '$directors'},
        {'$unwind': '$genres'},
        {'$group': {'_id': {'directors': '$directors', 'genres': '$genres'}, 'totalMovies': {'$sum': 1}}},
        {'$match': {'_id.genres': genre}},
        {'$sort': {'totalMovies': -1}},
        {'$limit': n}
    ])
    print(f"\nTop {n} directors who created the maximum number of movies for a given genre\n")

    for i in directors3:
        print(i)

topNDirectors()