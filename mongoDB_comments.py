from pymongo import MongoClient

# Connecting to MongoDB
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client['sampleData']
except:
    print("Error while connecting")

# -------------- Defining Functions ---------------

def findTop10Comments(collection):
    # Top 10 users who made the maximum number of comments
    top10Comments = db[collection].aggregate([
        {'$group': {'_id': {'users': '$name'}, 'totalComments': {'$sum': 1}}},
        {'$sort': {'totalComments': -1}},
        {'$limit': 10}
    ])

    print("Top 10 users who made the maximum number of comments\n")
    for users in top10Comments:
        print(users)

def findTop10Movies(collection):
    # Top 10 movies with most comments
    top10Movies = db['comments'].aggregate([
        {'$group': {'_id': {'movies': '$movie_id'}, 'total_comments': {'$sum': 1}}},
        {'$sort': {'total_comments': -1}},
        {'$limit': 10}
    ])

    print("\nTop 10 movies with most comments\n")
    for movies in top10Movies:
        print(movies)

def findCommentsInAYear(collection):
    # Given a year find the total number of comments created each month in that year
    try:
        year = int(input("\nYear : "))
    except:
        print("Please enter correct year")
    finally:
        totalComments =db['comments'].aggregate([
            {'$project':{'Year':{'$year':'$date'},'Month':{'$month':'$date'},'totalComments':'$_id.totalComments'}},
            {'$match': {'Year': year}},
            {'$group': {'_id': '$Month', 'totalComments': {'$sum': 1}}},
            {'$sort': {'_id': 1}},
            {'$project':{'Month':'$_id','totalComments':1,'_id':0}}
            ])

        print(f"Given year {year} the total number of comments created each month in that year")
        count=0
        for totalNoComment in totalComments:
            count+=1
            print(totalNoComment)
        if count<1:
            print(f"No comments received in year:{year}")

# -------- Functions Calling -------------

# collection='comments'
# findTop10Comments(collection)
# findTop10Movies(collection)
# findCommentsInAYear(collection)