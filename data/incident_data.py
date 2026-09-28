import json


def load_incidents():
    with open("data/incidents.json", "r") as file:
        return json.load(file)
