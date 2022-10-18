from cypherMain import*

def interfaceIs():
    while True:
    
        print ("Send a secret message")
        print ("1 = encode message")
        print ("2 = decode message")
        print ("3 = exit")

        userChoice = int(input("...."))

        if userChoice == 1:
            encodeMessage()
        elif userChoice == 2:
            decodeMessage()
        elif userChoice == 3:
            break

        else:
            print("other choices not coded yet")

interfaceIs()