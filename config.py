import json

def load_configuration(filename):
    with open(filename) as json_file:
        return json.load(json_file)
        