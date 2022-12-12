import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def apod():
    # Retrieve the Astronomy Picture of the Day
    url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
    response = requests.get(url)
    return response.json()


def earth_natural_imagery():
    # Retrieve metadata on the most recent date of natural color imagery
    url = f"https://api.nasa.gov/EPIC/api/natural/images?api_key={API_KEY}"
    response = requests.get(url)
    return response.json()


def nasa_library(query):
    # Perform a search of the Nasa Image and Video library
    url = f"https://images-api.nasa.gov/search?q={query}"
    response = requests.get(url)
    return response.json()


def asteroid_info(start_date, end_date):
    # Retrieve a list of Asteroids on thier closest approach date to Earth
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={API_KEY}"
    response = requests.get(url)
    return response.json()
