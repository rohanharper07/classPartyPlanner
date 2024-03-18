# this  surveys each student
from . import easyInput

def classSurvey(snacks):
    preferences = ["best", "good", "ok", "bad", "no way"]
    surveyResults = []
    # python version of a post-test loop
    while True:
        # exit if anything but enter is pressed
        if input("Press enter to go to next student or type any letter to exit:") != "":
            break

        print(f"Welcome, student\nid: {len(surveyResults)}\nYou will now pick some snacks\nEach snack is assigned to a number. Refer to it by this number")
        currentResults = []

        formattedSnacks = ""
        for snackIndex in range(len(snacks)):
            if formattedSnacks == "":
                formattedSnacks = formattedSnacks + f"{snackIndex}: {snacks[snackIndex]}"
            else:
                formattedSnacks = formattedSnacks + f", {snackIndex}: {snacks[snackIndex]}"
        
        print(formattedSnacks)

        for pref in preferences:
            while True:
                response = int(input(f"Pick your '{pref}' snack: "))
                if 0 <= response < len(snacks):
                    currentResults.append(snacks[response])
                    break
        
        surveyResults.append({"id": len(surveyResults), "picks": currentResults})
    return(surveyResults)
                