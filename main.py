# import the json module to decode backup files if necessarry
# NOT MADE BY ME (included in python standard library)
import json

# import my input module from modules folder
from modules import input
\
# options for the user upon starting the program
operations = ["New Planner", "Load Backup", "New Backup"]

input.listInput("What would you like to do?", operations)

