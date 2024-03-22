# this module is what takes user input


# this function gets the user to input a yes or no answer
def binaryInput(prompt: str):
    # possible responses to a yes or no question
    yesResponses = ["y", "yes", "1"]
    noResponses = ["n", "no", "0"]
    while True:
        # take input and change case to lowercase
        responseRaw = input(prompt, " y/n: ").lower()
        # check against possible responses and if not, get another input
        if responseRaw in yesResponses:
            return True
        elif responseRaw in noResponses:
            return False


# this function gets the user to select a response from
def listInput(prompt: str, list: list):
    # prompt
    printList(list, prompt)

    while True:
        # take input and change case to lowercase
        response = int(input("Pick the number corresponding to your option: "))
        # check against possible responses and if not, get another input
        if 0 <= response < len(list):
            return list[response]


def multiInput(prompt: str, data: list, separator: str):
    # prompt
    printList(data, prompt)

    # take input, strip whitespace, lowercase it
    responses = input(f"Pick the numbers corresponding to your option, separated by '{separator}': ")
    responses = responses.strip(" ").lower().split(separator)

    result = []

    # try to add the result, if it doesn't work, ignore it.
    for response in responses:
        try:
            result.append(data[int(response)])
        except KeyError:
            print(f"Option '{response}' not found")
        except ValueError:
            print("You have selected nothing.")

    return result


def printList(data: list, prompt="Pick one"):
    print(prompt, ", Your options are:")

    for num, item in enumerate(data):
        print(f"{num}: {item}")
