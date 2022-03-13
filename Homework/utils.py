import json


def load_candidates():
    with open("candidates.json") as file:
        candidates = json.load(file)
    return candidates
