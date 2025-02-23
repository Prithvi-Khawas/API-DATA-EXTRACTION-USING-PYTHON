import requests

import json

import psycopg2





#API key


api_key = '92484e8d8282fd869b379bdddb0c5eb6'


tmdb_key = 'https://api.themoviedb.org/3/search/movie?query=movie&api_key=92484e8d8282fd869b379bdddb0c5eb6'


response = requests.get(tmdb_key)

data = response.json()

print(data)

movie_title = input("Enter movie name: ")

if data['total_results'] > 0:
    # Iterate over the results list
    for movie in data['results']:
        if movie_title.lower() in movie['original_title'].lower():
            # Extract movie details
            adult = movie['adult']
            movie_id = movie['id']
            title = movie['original_title']
            description = movie['overview']
    
            print("------Movie Information")
            print(f"Name of the movie: {title}")
            print(f"Description : {description}")
            print(f"Adult :{adult}")
    
        else:
            print(f"Movie : {movie_title} not found")
else:
    print("No movies found.")