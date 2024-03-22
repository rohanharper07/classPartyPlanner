# genarates fake allergens for some foods

import json
import random

allergens = ["nuts", "dairy", "gluten", "egg"]

with open("party_foods.json") as file:
    foods = json.load(file)

foodAllergen = {}

for food in foods:
    if random.random() < 0.25:
        a = random.choice(allergens)
        if foodAllergen.get(a, None) is None:
            foodAllergen[a] = [food]
        else:
            foodAllergen[a].append(food)

with open("allergyFoods.json", "w") as file:
    json.dump(foodAllergen, file)
