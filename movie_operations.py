from PyQt4.QtGui import *
from misc import change_image
import tmdbsimple as tmdb

tmdb.API_KEY = "ecad2ffd2f6bc7b8e016fcad0d7bb9fb"
GENRES = {"action":28, "adventure":12, "comedy":35, "romance":10749, "drama":18, "crime":80, "horror":27, "fiction":878}

def list_by_genre(number_movies, id_genre):
    movies_informations = []
    movie = {}
    genre = tmdb.Genres(id_genre)
    movies = genre.movies(page=2)
    result = movies["results"]
    for i in range(number_movies):
        movie = {}
        movie["id_movie"] = result[i]["id"]
        movie["name"] = result[i]["title"]
        movie["overview"] = result[i]["overview"]
        movie["date"] = result[i]["release_date"]
        movie["poster"] = "https://image.tmdb.org/t/p/w500" + result[i]["poster_path"]
        movie["vote"] = str(result[i]["vote_average"])
        movies_informations.append(movie)
    return movies_informations


def add_attributes(widget, genre, start=0):
    counter = 0
    movies = list_by_genre(15, GENRES[genre])
    for i in QApplication.allWidgets():
        if counter == 5:
            break
        if "carac" in i.objectName():
            continue
        if genre in i.objectName() and i.objectName().find("{}_title_".format(genre)) == -1:
            i.id = movies[start]["id_movie"]
            i.name = movies[start]["name"]
            getattr(widget, "{0}_title_{1}".format(genre, i.objectName()[-1])).setText(i.name)
            i.overview = movies[start]["overview"]
            i.date = movies[start]["date"]
            i.poster = movies[start]["poster"]
            i.vote = movies[start]["vote"]
            change_image(i, i.poster, True)
            start += 1
            counter += 1
