# this opens backup files and words lists.

def readFile(path):
    with open(path, "r") as file:
        data = file.read()

    dataList = data.split("\n")
    
    return dataList

def writeFile(dataList, path):

    encoded = "\n".join(dataList)

    with open(path, "r") as destinationFile:
        destinationFile.write(encoded)

def readBackup(path):
    