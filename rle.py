#Run Length Coding
def encode(message):
    encoded_message = ""
    i = 0

    while (i <= len(message)-1):
        count = 1
        ch = message[i]
        j = i
        while (j < len(message)-1):
            if (message[j] == message[j+1]):
                count = count+1
                j = j+1
            else:
                break

        encoded_message=encoded_message+str(count)+ch
        i = j+1
    return encoded_message
 
#providing value for message and testing the program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)
print("kailash BADU\nRoll No: 09")