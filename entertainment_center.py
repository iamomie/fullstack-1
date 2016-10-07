import media
import fresh_tomatoes
import urllib
import json

# a method to get movie metadata from the omdb api.
def get_movie_metadata(movie_title):
    connection = urllib.urlopen("http://www.omdbapi.com/?t=" + movie_title + "&y=&plot=full&r=json")
    json_str = connection.read()
    connection.close()
    return json.loads(json_str)

# get the metadata for each movie, toy story.
movie_metadata = get_movie_metadata("Toy story")

# create the toy story movie object.
toy_story = media.Movie(movie_metadata['Title'],
                        movie_metadata['Plot'],
                        movie_metadata['Poster'],
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# get the metadata for each movie, Avatar.
movie_metadata = get_movie_metadata("Avatar")

# create the avatar movie object.
avatar = media.Movie(movie_metadata['Title'],
                     movie_metadata['Plot'],
                     movie_metadata['Poster'],
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")


# get the metadata for each movie, A Beautiful Mind.
movie_metadata = get_movie_metadata("A Beautiful Mind")

# create the A Beautiful Mind movie object.
a_beautiful_mind = media.Movie(movie_metadata['Title'],
                               movie_metadata['Plot'],
                               movie_metadata['Poster'],
                               "https://www.youtube.com/watch?v=aS_d0Ayjw4o")

# create an array to pss into the python module that will crate the webpage.
movies = [toy_story, avatar, a_beautiful_mind]

# creates a web page with all the movies
fresh_tomatoes.open_movies_page(movies)
