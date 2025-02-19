import json

def fromJson(path: str):    
    with open("pokemons.txt", "r") as file:
        class_names = [line.strip() for line in file.readlines()]

    with open("pokemons.json", "w") as json_file:
        json.dump(class_names, json_file)
        return class_names