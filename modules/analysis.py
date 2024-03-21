# this does the data sorting and other cool stuff

# order the data
# exclude unpopular snacks
# warn for allergies

from collections import OrderedDict

def analyse(surveyResults, snacks, allergyFoods):
    # weight of each rank given for snacks
    weight = [2 , 1 , 1 , -1 , -2]
    
    rankings = {}

    # populate ranking list
    for student in surveyResults:
        for preference in range(len(student["picks"])):
            try:
                rankings[student["picks"][preference]] += weight[preference]
            except KeyError:
                rankings[student["picks"][preference]] = weight[preference]

    limitRankings = rankings.copy()
    for rank in rankings:
        if rankings[rank] <= 0:
            del limitRankings[rank]

    # remove unwanted snacks
    sortedFoods = sorted(limitRankings.keys(), key = limitRankings.get, reverse = True)
    sortedVotes = sorted(limitRankings.values(), reverse=True)

    print("Results (sorted by popularity, unwanted snacks removed)\nFood = Votes")
    for food, votes in zip(sortedFoods, sortedVotes):
        print(f"{food} = {votes}")