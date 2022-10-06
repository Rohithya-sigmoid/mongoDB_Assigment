from pymongo import MongoClient
# Connecting to MongoDB
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client['sampleData']
except:
    print("Error while connecting")

movies=db['movies']

n = int(input("n : "))
year = int(input("Year: "))

# --------------Top N actors------------
def topNActors():
    print('\n--------------Actors Query---------------')
    # i) Top N actors who starred in the maximum number of movies

    actors1 = db['movies'].aggregate([
        {'$unwind':'$cast'},
        {'$match':{'cast':{'$exists':True,'$ne':''}}},
        {'$group':{'_id':'$cast','totalMovies':{'$sum':1}}},
        {'$sort':{'totalMovies':-1}},
        {'$limit':n}
    ])

    print(f"\nTop {n} actors who starred in the maximum number of movies\n")
    for i in actors1:
        print(i)

    # ii) Top N actors who starred in the maximum number of movies in a given year

    actors2 = db['movies'].aggregate([
        {'$unwind':'$cast'},
        {'$match': {'year': year}},
        {'$group': {'_id': {'year':'$year','cast':'$cast'},'totalMovies':{'$sum':1}}},
        {'$sort': {'totalMovies': -1}},
        {'$limit': n}
    ])
    print(f"\nTop {n} actors who starred in the maximum number of movies in a year {year}\n")
    count=0

    for i in actors2:
        count+=1
        print(i)

    if count<n:
        print(f"\nOnly {count} movies released in that year\n")

    # iii) Top N actors who starred in the maximum number of movies for a given genre
    genre = input("\nEnter the genre you want to query on: ")
    actors3 = db['movies'].aggregate([
        {'$unwind': '$cast'},
        {'$unwind': '$genres'},
        {'$group': {'_id': {'cast': '$cast', 'genres': '$genres'}, 'totalMovies': {'$sum': 1}}},
        {'$match': {'_id.genres': genre}},
        {'$sort': {'totalMovies': -1}},
        {'$limit': n}
    ])
    print(f"\nTop {n} actors who starred in the maximum number of movies for genre {genre}\n")

    for i in actors3:
        print(i)

def topNmoviesGivenGenre(genre):
    # iv) Top movies for each genre with the highest IMDB rating
    moviesN = db['movies'].aggregate([
        {"$unwind": "$genres"},
        {'$group': {'_id': {'genres':'$genres','title': '$title'}}},
        {"$sort": {"_id.genres": 1,'imdb.rating':-1}},
        {"$match": {'_id.genres':genre}},
        {"$limit": n}
    ])
    print(f"\nTop {n} movies for genre {genre} with the highest IMDB rating\n")
    for i in moviesN:
        print(i)



def topNmoviesAllGenres():
    genres = db["movies"].aggregate([
        {"$unwind":"$genres"},
        {"$project":{"genres":1,"_id":0}}
    ])
    genreList = []
    for i in genres:
        genreList.append(i["genres"])
    genreSet = set(genreList)
    for genre in genreSet:
        topNmoviesGivenGenre(genre)

# ------------- Function Calling---------
topNActors()
topNmoviesAllGenres()