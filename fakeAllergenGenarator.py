# genarates fake allergens for some foods

import random, json

allergens = ["nuts", "dairy", "gluten", "egg"]

with open("party_foods.json") as file:
    foods = json.load(file)

foodAllergen = {}

for food in foods:
    if random.random() < 0.25:
        foodAllergen[food] = random.choice(allergens)

with open("allergens.json", "w") as file:
    json.dump(foodAllergen, file)