# import my input and file module module from modules folder
from modules import fileReadWrite, input, fileFinder

# options for the user upon starting the program
operations = ["New Planner", "Load Backup", "Save Backup", "Quit"]

plannerData = []

while True:
    command = input.listInput("What would you like to do?", operations)

    # if we want to make a new class party planner
    if command == "New Planner":
        print("Making a new class party planner!")

    # make and save a new list of suggestions
    elif command == "Suggest Snacks!":
        if len(plannerData) == 0:
            print("You need to make a new planner or load a backup first!")
        else:
            print("Analysing data...")

    # save or overwrite a backup
    elif command == "Save Backup":
        print("Saving a new backup")

        fileName = input("Enter a file name: ")

        fileReadWrite.writeFile(plannerData, fileName)

    # load an existing backup
    elif command == "Load Backup":
        # find files with the .ppbackup extension (which are really just text files)
        backups = fileFinder.findFiles(".ppbackup")

        if len(backups) == 0:
            print(f"Oops! No .ppbackup files found in the {__file__.strip('main.py')} directory")
        else:
            input.listInput("Which backup would you like to load?", backups)
            print("Loading party planner backup")

    # quit the program
    elif command == "quit":
        print("See ya later!")
        
        quit()