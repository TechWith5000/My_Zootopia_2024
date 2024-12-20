import requests
import os
from dotenv import load_dotenv

def fetch_data(animal_name):
      """
      Fetches the animals data for the animal 'animal_name'.
      Returns: a list of animals, each animal is a dictionary:
      {
        'name': ...,
        'taxonomy': {
          ...
        },
        'locations': [
          ...
        ],
        'characteristics': {
          ...
        }
      },
      """
      load_dotenv()
      API_KEY = os.getenv('API_KEY')
      url = "https://api.api-ninjas.com/v1/animals?name=" + animal_name
      headers = {
          "X-Api-Key": API_KEY
      }
      response = requests.get(url, headers=headers)
      response = response.json()
      return response

