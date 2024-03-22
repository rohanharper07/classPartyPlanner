# this does the data sorting and other cool stuff

# order the data
# exclude unpopular snacks
# warn for allergies


def analyse(surveyResults, allergyFoods):
    # weight of each rank given for snacks
    weight = [2, 1, 1, -1, -2]

    rankings = {}
    allergies = {}

    for student in surveyResults:
        # add or subtract from score
        for preference in range(len(student["picks"])):
            try:
                rankings[student["picks"][preference]] += weight[preference]
            except KeyError:
                rankings[student["picks"][preference]] = weight[preference]
        
        # take care of allergies
        studentAllergies = student["allergens"]

        for allergy in studentAllergies:
            if allergies.get(allergy, None) is None:
                allergies[allergy] = [student["name"]]
            else:
                allergies[allergy].append(student["name"])


    # remove anything with a score of 0 or less
    limitRankings = rankings.copy()
    for rank in rankings:
        if rankings[rank] <= 0:
            del limitRankings[rank]

    # sort snacks
    sortedFoods = sorted(limitRankings.keys(), key=limitRankings.get, reverse=True)
    sortedVotes = sorted(limitRankings.values(), reverse=True)

    # check for allergies
    unsuitableFoods = {}
    for allergy in allergies:
        for food in allergyFoods.get(allergy, []):
            if food in sortedFoods:
                unsuitableFoods[food] = allergies[allergy]

    # print the results
    print("Results (sorted by popularity, unwanted snacks removed)\nFood = Score - Allergic People")
    for food, votes in zip(sortedFoods, sortedVotes):
        print(f"{food} = {votes}")

    # print allergies
    if len(unsuitableFoods) > 0:
        print("ALLERGIES FOUND")
        for food, students in enumerate(unsuitableFoods):
            print(f'{food} is unsuitable for: {", ".join(students)}')

    return zip(sortedFoods, sortedVotes)
