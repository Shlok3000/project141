import csv
from flask import Flask, jsonify, request

all_movies = []

with open("movies.csv", encoding="utf-8") as i:
    r = csv.reader(i)
    data = list(r)
    all_movies = data[1:]

like_movies = []
disliked_movies = []
not_watched = []

app = Flask(__name__)

@app.route("/") 
def movies():
    return "Welcome to the home page"

@app.route("/get-movie")
def get_movies():
    return jsonify({
        "data": all_movies[0],
        "status": "success"
    }),200

@app.route("/like-movies", methods = ["POST"])
def liked_movies():
    global all_movies
    movie = all_movies[0]
    all_movies = all_movies[1:]
    like_movies.append(movie)
    return jsonify({
        "status": "success"
    }),200

@app.route("/disliked-movies", methods = ["POST"])
def dislike_movie():
    global all_movies
    movie = all_movies[0]
    all_movies = all_movies[1:]
    disliked_movies.append(movie)
    return jsonify({
        "status": "success"
    }),200

@app.route("/unwatched-movies", methods = ["POST"])
def unwatched():
    global all_movies
    movie = all_movies[0]
    all_movies = all_movies[1:]
    not_watched.append(movie)
    return jsonify({
        "status": "success"
    }),200

if __name__ == "__main__":
    app.run(debug = True)