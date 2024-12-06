import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

for animal in animals_data:
      print(f"Name: {animal["name"]}\nDiet: {animal["characteristics"]["diet"]}\n"
            f"Location: {animal["locations"][0]}")
      try:
          print(f"Type: {animal["characteristics"]["type"]}\n")
      except KeyError:
        print("")
        continue