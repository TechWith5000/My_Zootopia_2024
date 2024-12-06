import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

'''
for animal in animals_data:
      print(f"Name: {animal["name"]}\nDiet: {animal["characteristics"]["diet"]}\n"
            f"Location: {animal["locations"][0]}")
      try:
          print(f"Type: {animal["characteristics"]["type"]}\n")
      except KeyError:
        print("")
        continue
'''

with open("animals_template.html", "r") as fileobj:
    text_html = fileobj.read()

output = ''  # define an empty string
for animal in animals_data:
    # append information to each string
    output += '<li class="cards__item">'
    output += f"<div class='card__title'>{animal["name"]}</div><p class='card__text'>\n"
    output += f"<strong>Diet:</strong>{animal["characteristics"]["diet"]}<br/>\n"
    output += f"<strong>Location:</strong>{animal["locations"][0]}<br/>\n"
    try:
        output += f"<strong>Type:</strong>{animal["characteristics"]["type"]}<br/>\n\n</p></li>"
    except KeyError:
        output += f"\n</p></li>"
        continue

#print(output)

new_text = text_html.replace("__REPLACE_ANIMALS_INFO__", output)

print(new_text)

with open("animals.html", "w") as fileobj:
    fileobj.write(new_text)