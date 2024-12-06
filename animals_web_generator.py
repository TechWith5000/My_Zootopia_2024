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
    output += f"Name: {animal["name"]}\n"
    output += f"Diet: {animal["characteristics"]["diet"]}\n"
    output += f"Location: {animal["locations"][0]}\n"
    try:
        output += f"Type: {animal["characteristics"]["type"]}\n\n"
    except KeyError:
        output += f"\n"
        continue

#print(output)

new_text = text_html.replace("__REPLACE_ANIMALS_INFO__", output)

print(new_text)