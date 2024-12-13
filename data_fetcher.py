import requests

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
  url = "https://api.api-ninjas.com/v1/animals?name=" + animal_name
  api_key = "PB3HeskWDOYsKFXahX/0XQ==CKWeyxWZg6YfZN0d"
  headers = {
      "X-Api-Key": api_key
  }
  response = requests.get(url, headers=headers)
  response = response.json()
  return response

