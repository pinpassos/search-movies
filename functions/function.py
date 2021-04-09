# Import modules
from time import sleep
import requests
import json
import dotenv
import os

# Dotenv config
dotenv.load_dotenv(dotenv.find_dotenv()) 
API_KEY = os.getenv('API_KEY')

# HTTP Requisition
def requisition(movie_title):
    try:
        req = requests.get('http://www.omdbapi.com/?t={}&r&apikey={}'.format(movie_title, API_KEY))
        content_dict = json.loads(req.text)
        return content_dict
    except ConnectionError():
        print('Error connection.')
        exit()
    else:
        print('Connection estabelished.') #status 200

# Result of searched movie
def movie_details(movie):
    print('=*=' * 20)
    print('Movie name: '+ movie['Title'])
    print('Released: '+ movie['Released'])
    print('Director: '+ movie['Director'])
    print('Poster: '+ movie['Poster'])
    print('Production: '+ movie['Production'])
    print('imdbRating: '+ movie['imdbRating'])
    print('=*=' * 20)