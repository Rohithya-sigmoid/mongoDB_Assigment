# MongoDB-Assignment


### Installation and Usage

1. Clone the repository
2. Download and Install [Python](https://www.python.org/downloads/)
3. Install [Pymongo](https://pypi.org/project/pymongo/)
    ```
    pip install pymongo
    ```
4. Install [MongoDB](https://www.mongodb.com/docs/manual/installation/)
5. Make sure you have mongo, mongod, mongoimport installed
6. Start mongod server
7. Run task files 

Tasks -

1.Create a Python application to connect to MongoDB.

2.Bulk load the JSON files in the individual MongoDB collections using Python. MongoDB collections -comments , movies , theaters , users

3.Create Python methods and MongoDB queries to insert new comments, movies, theatres, and users into respective MongoDB collections.

4.Create Python methods and MongoDB queries to support the below operations

 -comments collection
Find top 10 users who made the maximum number of comments
Find top 10 movies with most comments
Given a year find the total number of comments created each month in that year

-movies collection
a)Find top `N` movies - 
1. with the highest IMDB rating
2.with the highest IMDB rating in a given year
3.with highest IMDB rating with number of votes > 1000
4.with title matching a given pattern sorted by highest tomatoes ratings

b)Find top `N` directors -
1.who created the maximum number of movies
2.who created the maximum number of movies in a given year
3.who created the maximum number of movies for a given genre

c)Find top `N` actors - 
1.who starred in the maximum number of movies
2.who starred in the maximum number of movies in a given year
3.who starred in the maximum number of movies for a given genre

d)Find top `N` movies for each genre with the highest IMDB rating

-theater collection

Top 10 cities with the maximum number of theaters
top 10 theaters nearby given coordinates

