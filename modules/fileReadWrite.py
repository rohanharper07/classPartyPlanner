# this opens backup files and words lists.
# the commented block of code is the encoding scheme that I was going to use,
# but in the end, using the json library is just easier and simpler

# def readFile(path):
#     with open(path, "r") as file:
#         rawData = file.read()

#     data = rawData.split("\n")

#     return data

# def writeBackup(backup, path):
#     encoded = ""
#     for student in backup:
#         chunk = ""
#         for item in student:
#             if type(student[item]) is list:
#                 chunk = chunk + f",{item}:{','.join(student[item])}"
#             else:
#                 chunk = chunk + f",{item}:{student[item]}"
#         encoded = encoded + "\n" + chunk

#     with open(path, "w") as destinationFile:
#         destinationFile.write(encoded)

import json


def writeFile(data, path):
    with open(path, "w") as file:
        json.dump(data, file)


def readFile(path):
    with open(path, "r") as file:
        data = json.load(file)

    return data
