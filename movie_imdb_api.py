import requests

import json

import psycopg2





#API key


api_key = '92484e8d8282fd869b379bdddb0c5eb6'


tmdb_key = 'https://api.themoviedb.org/3/search/movie?query=Inception&api_key=92484e8d8282fd869b379bdddb0c5eb6'


response = requests.get(tmdb_key)

data = response.json()

print(data)