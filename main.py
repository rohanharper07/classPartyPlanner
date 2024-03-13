# import my input and file module module from modules folder
from modules import input

# options for the user upon starting the program
operations = ["New Planner", "Load Backup", "Save Backup", "Quit"]

while True:
    command = input.listInput("What would you like to do?", operations)

    if command == "New Planner":
        print("Making a new class party planner")

    elif command == "Load Backup":
        print("You can load these backups:")
        print("Loading party planner backup")

    elif command == "Save Backup":
        print("Saving a new backup")

    else:
        print("See ya later buster!")
        quit()