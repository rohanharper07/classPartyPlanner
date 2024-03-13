# this module is what takes user input

# this function gets the user to input a yes or no answer
def binaryInput(prompt:str):
    # possible responses to a yes or no question
    yesResponses = ["y", "yes", "1"]
    noResponses = ["n", "no", "0"]
    while True:
        #take input and change case to lowercase
        responseRaw = input(prompt, " y/n: ").lower()
        # check against possible responses and if not, get another input
        if responseRaw in yesResponses:
            return True
        elif responseRaw in noResponses:
            return False
        
# this function gets the user to select a response from 
def listInput(prompt:str, list:list):
    # create a dictionary with numbers corresponding to answers
    responseDict = dict(zip(range(1, len(list)+1), list))

    # print possible responses with numbers once
    print(prompt, ", Your options are:")
    for item in responseDict:
        print(f"{item}: {responseDict[item]}")


    while True:
        #take input and change case to lowercase
        response = int(input("Pick the number corresponding to your option: "))
        # check against possible responses and if not, get another input
        if response in responseDict:
            return responseDict[response]