from addOne import *
from deleteOne import *

def writeToFile(encodedList):
    with open('secretMessage.txt', 'w') as f:
        listToStr = ' '.join([str(elem)+"," for elem in encodedList])
        f.write(listToStr)

def readFromFile():
    with open('secretMessage.txt') as f:
        
        contents = f.read()
        
        contentsAsList = list(contents.split(","))
        contentsAsList.pop()
        # print(contents,"debug")
        return contentsAsList


def encodeMessage():

    userMessage = input("Type your message here: ")

    convertThis = userMessage
    cutInToList = list(convertThis)
    encodedList = []
   

    for n in convertThis: # loops for each letter in the message
        
        # converts a letter into an ordinal number
        # for n in cutInToList:
            
        wordIs = ord(n)
        # print ( f"{convertThis}: is also the ascii number:", wordIs)

        # encode the data
        secretNumber, keyIs = addOne(wordIs)
        encodedList.append(secretNumber)
        # print("\n")
        # print("------------------ENCODE----------------------------------------------------")
        # print(f"The data is then shifted by one place: {secretNumber}")
        # print(f"So hackers would see {secretNumber} instead of {wordIs} or {convertThis} ")
        # print("send this message to your friend:",encodedList, f"\n the key is: {keyIs}")
    writeToFile(encodedList)
    


def decodeMessage():
    decodedListNew = []
    dataFromFile = readFromFile()
    lengthOfSecretMessage = len(dataFromFile)
    # print(dataFromFile,"debug222")
    # print(lengthOfSecretMessage,"debug")
    
    for n in range (0,lengthOfSecretMessage):
        originalNumber = deleteOne(dataFromFile[n])
        
        

        # print("\n")
        # print("------------------DECODE----------------------------------------------------")
        # print(f"the data is now shifted back to the correct number {originalNumber}")


        # converts an ordinal number into a letter
        wordIs2 = chr(originalNumber)
        decodedListNew.append(wordIs2)
        # print( "And finally returned to the orignal letter which is:", wordIs2)
        

        # print("\n")
        # print("------------------Play----------------------------------------------------")
        # print("Try other letters. Check the image in (files) to see all the ascii codes.")
        # print("Shift the number by plus 3 etc.")
        # print("What errors might happen if we shift the number too far? .....")
    print(decodedListNew, " original message")
