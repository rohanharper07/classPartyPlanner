# import my input and file module module from modules folder
from modules import easyInput, fileReadWrite, fileFinder, survey, analysis

# options for the user upon starting the program
operations = ["New Planner", "Suggest Snacks!", "Load Backup", "Save Backup", "Quit"]

snacks = fileReadWrite.readFile("party_foods.json")
allergens = fileReadWrite.readFile("allergens.json")
plannerData = []

# using literal strings to avoid calling print lots for multiline text
print("This program collects personal information (names and allergies) Do not share the backup files with unauthorized people")

while True:
    command = easyInput.listInput("What would you like to do", operations)

    # if we want to make a new class party planner
    if command == "New Planner":
        print("Making a new class party planner!")
        plannerData = survey.classSurvey(snacks, allergens)
        print(plannerData)

    # make and save a new list of suggestions
    elif command == "Suggest Snacks!":
        if len(plannerData) == 0:
            print("You need to make a new planner or load a backup first!")
        else:
            print("Analysing data...")
            results = analysis.analyse(plannerData, snacks, fileReadWrite.readFile("allergyFoods.json"))

    # save or overwrite a backup
    elif command == "Save Backup":
        print("Saving a new backup")
        fileName = input("Enter a file name: ")
        fileReadWrite.writeFile(plannerData, fileName + ".json")

    # load an existing backup
    elif command == "Load Backup":
        # find files with the json extension
        backups = fileFinder.findFiles(".json")
        if len(backups) == 0:
            print(f"Oops! No .ppbackup files found in the {__file__.strip('main.py')} directory")
        else:
            selection = easyInput.listInput("Which backup would you like to load?", backups)
            print("Loading party planner backup")
            plannerData = fileReadWrite.readFile(selection)

    # quit the program
    elif command == "quit":
        print("See ya later!")
        quit()
