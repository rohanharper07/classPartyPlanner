# this uses the os library (not mine) to find files or directories with a keyword in the name
from os import listdir
# this library has to be used to do more complex operations than reading or writing

# search, with default path as the working directory
def findFiles(keyword, path=None):
    directoryConents = listdir(path)
    output = []
    for fileOrFolder in directoryConents:
        if keyword in fileOrFolder:
            output.append(fileOrFolder)
    
    return output