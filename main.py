# import my input and file module module from modules folder
from modules import analysis, easyInput, fileFinder, fileReadWrite, survey

# options for the user upon starting the program
operations = ["New Planner", "Suggest Snacks!", "Load Backup", "Save Backup", "Quit"]

snacks = fileReadWrite.readFile("party_foods.json")
allergens = fileReadWrite.readFile("allergens.json")
plannerData = []

# using literal strings to avoid calling print lots for multiline text
print(
    "This program collects personal information (names and allergies) Do not share the backup files with unauthorized people"
)

while True:
    command = easyInput.listInput("What would you like to do", operations)

    # if we want to make a new class party planner
    if command == "New Planner":
        print("Making a new class party planner!")
        plannerData = survey.classSurvey(snacks, allergens)
        print(plannerData)
        safeToExit = False
        print("Make sure to save your data!")

    # make and save a new list of suggestions
    elif command == "Suggest Snacks!" and plannerData != []:
        print("Analysing data...")
        results = analysis.analyse(
            plannerData, fileReadWrite.readFile("allergyFoods.json")
        )

    # save or overwrite a backup
    elif command == "Save Backup" and plannerData != []:
        print("Saving a new backup")
        fileName = input("Enter a file name: ")
        fileReadWrite.writeFile(plannerData, fileName + ".json")
        safeToExit = True

    # load an existing backup
    elif command == "Load Backup":
        # find files with the json extension
        backups = fileFinder.findFiles(".json")

        selection = easyInput.listInput(
            "Which backup would you like to load?", backups
        )
        print("Loading party planner backup")
        plannerData = fileReadWrite.readFile(selection)

    # quit the program
    elif command == "Quit":
        print("See ya later!")
        quit()
