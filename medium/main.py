from addOne import *
from deleteOne import *

convertThis = "big"
cutInToList = list(convertThis)
encodedList = []
decodedList = []

for n in convertThis: # loops for each letter in the message
    
    # converts a letter into an ordinal number
    for n in cutInToList:
        
        wordIs = ord(n)
        print ( f"{convertThis}: is also the ascii number:", wordIs)

        # encode the data
        secretNumber, keyIs = addOne(wordIs)
        encodedList.append(secretNumber)
        print("\n")
        print("------------------ENCODE----------------------------------------------------")
        print(f"The data is then shifted by one place: {secretNumber}")
        print(f"So hackers would see {secretNumber} instead of {wordIs} or {convertThis} ")
        print("send this message to your friend:",encodedList, f"\n the key is: {keyIs}")

# Creates a string
listToStr = ' '.join([str(elem) for elem in encodedList])
cutInToList2 = list(listToStr)
print (listToStr,"debug")

for n in listToStr:
    
    
    for n in cutInToList2:        
        # decode the data
        originalNumber = deleteOne(secretNumber)
        print("\n")
        print("------------------DECODE----------------------------------------------------")
        print(f"the data is now shifted back to the correct number {originalNumber}")


        # converts an ordinal number into a letter
        wordIs2 = chr(originalNumber)
        print( "And finally returned to the orignal letter which is:", wordIs2)
        

        print("\n")
        print("------------------Play----------------------------------------------------")
        print("Try other letters. Check the image in (files) to see all the ascii codes.")
        print("Shift the number by plus 3 etc.")
        print("What errors might happen if we shift the number too far? .....")


