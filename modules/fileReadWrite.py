# this opens backup files and words lists.
# it can break up a string into a 2D list
# uses newline character (\n) as delimiter for first dimension
# and , for the second dimension

# could have used JSON, but I wanted to do it myself

def readFile(path, twoDimensional=True):
    with open(path, "r") as file:
        data = file.read()

    dataList = data.split("\n")

    if twoDimensional:
        for subListIndex in range(len(dataList)):
            dataList[subListIndex] = dataList[subListIndex].split(",")
    
    return dataList

def writeFile(dataList, path):
    for subListIndex in range(len(dataList)):
        dataList[subListIndex] = ",".join(dataList[subListIndex])

    encoded = "\n".join(dataList)

    with open(path, "r") as destinationFile:
        destinationFile.write(encoded)