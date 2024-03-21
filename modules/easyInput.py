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
    # print possible responses with numbers once
    print(prompt, ", Your options are:")
    printList(list)

    while True:
        #take input and change case to lowercase
        response = int(input("Pick the number corresponding to your option: "))
        # check against possible responses and if not, get another input
        if 0 <= response < len(list):
            return list[response]
        
def multiInput(prompt:str, list:list, separator:str):
    print(prompt, ", Your options are:")
    printList(list)

    while True:
        #take input and change case to lowercase
        responses = input(f"Pick the numbers corresponding to your option, separated by '{separator}': ")
        responses = responses.strip(" ").split(separator)

        if responses == ['']:
            return []
        # this variable is used to test whether the value is valid or not
        good = True

        result = []
        # check against possible responses and if not, get another input
        for response in responses:
            if not (0 <= int(response) < len(list)):
                good == False
            else:
                result.append(list[int(response)])
        
        if good == True:
            return result

def printList(list:list):
    for itemIndex in range(len(list)):
        print(f"{itemIndex}: {list[itemIndex]}")