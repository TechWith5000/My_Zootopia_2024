import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')


with open("animals_template.html", "r") as fileobj:
    text_html = fileobj.read()


def serialize_animal(animal_obj):
    output = ''  # define an empty string
    # append information to each string
    output += '<li class="cards__item">'
    output += f"<div class='card__title'>{animal_obj["name"]}</div><p class='card__text'>\n"
    output += f"<strong>Diet:</strong>{animal_obj["characteristics"]["diet"]}<br/>\n"
    output += f"<strong>Location:</strong>{animal_obj["locations"][0]}<br/>\n"
    try:
        output += f"<strong>Type:</strong>{animal_obj["characteristics"]["type"]}<br/>\n\n</p></li>"
    except KeyError:
        output += f"\n</p></li>"
    return output

output = ''
for animal_obj in animals_data:
    output += serialize_animal(animal_obj)

new_text = text_html.replace("__REPLACE_ANIMALS_INFO__", output)


with open("animals.html", "w") as fileobj:
    fileobj.write(new_text)