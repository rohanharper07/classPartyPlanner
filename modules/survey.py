# this  surveys each student
from . import easyInput

def classSurvey(snacks, allergens):
    preferences = ["the best", "a good", "a good", "a bad", "the worst"]
    surveyResults = []

    # formats the string to be easily readable with it's indexes.
    # starting the formatting with a string that already contains a value means we can avoid a leading comma or unnecessary if statement inside the loop
    formattedSnacks = f"0: {snacks[0]}"
    for snackIndex in range(1, len(snacks)):
        formattedSnacks = formattedSnacks + f", {snackIndex}: {snacks[snackIndex]}"

    # python version of a post-test loop
    while True:
        # entering a name is unnecessary in most cases but is important for checking food allergies
        name = input("Enter your name or exit if there are no more students: ")

        if name.lower() == "exit": break

        print(f"Welcome, {name}\nYou will now pick some snacks\nEach snack is assigned to a number. Refer to it by this number")
        currentResults = []
        
        print(formattedSnacks)

        for pref in preferences:
            while True:
                response = int(input(f"Pick {pref} snack: "))
                if 0 <= response < len(snacks):
                    currentResults.append(snacks[response])
                    break

        allergies = easyInput.multiInput("Do you have any allergies?", allergens, ",")
        
        surveyResults.append({"name": name, "picks": currentResults, "allergens": allergies})

    return(surveyResults)
                