import data_fetcher

'''
 +++ CODE FOR RECEIVING DATA NOT FROM AN API, BUT A JSON FILE: +++
import json
def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)
'''


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



def main():
    # FOR DATA FROM JSON: animals_data = load_data('animals_data.json')
    animal_name = input("Please enter an animal: ")
    animals_data = data_fetcher.fetch_data(animal_name)

    with open("animals_template.html", "r") as fileobj:
        text_html = fileobj.read()

    output = ''
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)

    new_text = text_html.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w") as fileobj:
        fileobj.write(new_text)
        print("The data was successfully added to the template format. See output in the animals.html file")


if __name__ == "__main__":
    main()


