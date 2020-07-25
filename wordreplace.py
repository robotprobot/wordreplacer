import sys
import re
import os

#get arguments
try :
    inputfile = str(sys.argv[1]) #get first argument
    lookingforword = str(sys.argv[2]) #get second argument
    replacingwithword = str(sys.argv[3]) #get third argument
    print("Replacing all instances of '" + lookingforword + "' with '" + replacingwithword + "' in " + inputfile)
except:
    print("Insufficient arguments: <input file, word to be replaced, word to replace with>.")
    exit(0)

#check file
if os.access(inputfile, os.R_OK) == False:
    print("Could not read the specified file.")
    exit(0)

#check each word through the document for matches
try:
    replacecount = 0
    #create the new file
    path = os.path.splitext(inputfile)[0]
    extension = os.path.splitext(inputfile)[1]
    result = open(path+"-REPLACED"+extension, 'a')
    print("Outputting results to " + path+"-REPLACED"+extension)
    #check each word
    with open(inputfile, "r") as file:
        for line in file:
            for word in line.split():
                if word.lower() == lookingforword.lower():
                    #if word needs to be replaced
                    result.write(replacingwithword.lower() + " ")
                    replacecount += 1
                else:
                    result.write(word.lower() + " ")
    #when done close the file
    result.close()
    print("Execution was successfully completed, replacing " + str(replacecount) + " word(s).")
except:
    print("Word replace could not be performed on this file.")
