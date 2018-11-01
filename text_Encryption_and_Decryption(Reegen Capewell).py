#importing modules
from random import randint
separator = ('--------------------------------------------------------------------------------------------------------------------------------------------------')
characterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#main menu
def mainMenu():
    x = 0
    while x == 0:
        mode = input('encrypt message press e \n\nto decrypt message press d \n\nto encrypt at a higher level encryption press p \n\nto exit press q \n\nplease press the corresponding button: ')
        
        if mode == 'e':
            print(separator)
            encryption(mode)
        elif mode == 'd':
            decryptMessage(mode)
            print(separator)
        elif mode == 'p':
            encryption(mode)
            print(separator)
        elif mode =='q':
            exit()
        else:
            print('That is not a valid answer.Try again')
            x = 0

#loading the original file
def loadFile():
    fileName = input('Please enter the file name: ')
    try:
        messageFile = open(fileName,'r')
        message = messageFile.read()
        messageFile.close()
        print(separator)
    except:
        print('that is an invalid file name please try again')
        fileNameRetry = input('Please enter the file name: ')
        try:
            messageFile = open(fileNameRetry,'r')
            message = messageFile.read()
            messageFile.close()
            print(separator)
        except:
            exit()
    return message

#Generating the 8-character key
def createKey():
    key = []
    for x in range (8):
        tempKeyChar = randint(33,126)
        tempKeyChar = chr(tempKeyChar)
        key.append(tempKeyChar)
    print(separator)
    return key

#calculating the offset factor
def calcOffset(key):
    offset = 0
    for x in range(len(key)):
        offset = offset + ord(key[x])
    offset = offset/8
    offset = int(offset)
    offset = offset - 32
    print(separator)
    return offset

#saving file
def saveMessage(message):
    fileName = input('Please enter the new file name: ')
    file = open(fileName,'w')
    file.write(message)
    file.close()
    print(separator)
    return message

#auto-save file
def autoSaveFile(message):
    fileNameInd = randint(0,7)
    fileName = characterList[fileNameInd]
    file = open(fileName, 'w')
    file.write(message)
    file.close()
    return message

#encrypt the message
def encryption(mode):
    message = loadFile()
    print('')
    print(message)
    key = createKey()
    print('')
    print ('here is your 8-character key: ',key)
    offset = calcOffset(key)
    tempMessage = []
    message.split()
    for x in range(len(message)):
        if message[x] == ' ':
            if mode == 'e':
                tempMessage.append(message[x])
        else:
            tempChar = ord(message[x])
            tempChar = tempChar + offset
            if tempChar>126:
                tempChar = tempChar-94
            tempChar = chr(tempChar)
            tempMessage.append(tempChar)
    if mode == 'p':
        additionalSpace = int(len(tempMessage)/5)
        for x in range(5,len(tempMessage)+additionalSpace,6):           
            tempMessage.insert(x,' ')           
    message = ''.join(tempMessage)
    print('')
    print('this is your encypted message: '+message)
    print(separator)
    autoSaveFile(message)
    return message

#loading encrypted file
def loadEncryptedFile():
    print(separator)
    fileName = input('What is the name of the file?')
    messageFile = open(fileName,'r')
    encryptedMessage = messageFile.read()
    messageFile.close()
    return encryptedMessage

#decrypting message
def decryptMessage(mode):
    print(separator)
    fileName = input('What is the name of the file?')
    messageFile = open(fileName,'r')
    encryptedMessage = messageFile.read()
    messageFile.close()
    key = input('what is the key')
    key = list(key)
    calcOffset(key)
    tempMessage = []
    encryptedMessafe=messageFile.read
    encryptedMessage.split()
    for x in range(len(encryptedMessage)):
        if encryptedMessage[x] == ' ':
            tempMessage.append(encryptedMessage[x])
        else:
            offset = calcOffset(key)
            tempChar = ord(encryptedMessage[x])
            tempChar = tempChar-(offset)
            if tempChar<33:
                tempChar = tempChar+94
            tempChar = chr(tempChar)
            tempMessage.append(tempChar)
    encryptedMessage = ''.join(tempMessage)
    try:
     print('')
     print('Here is your message: '+encryptedMessage)
    except:
        print('Something has gone wrong with your message. Please try again')

#main
mainMenu()
message = loadFile()
key = createKey()
offset = calcOffset(Key)
autoSaveFile(message)
message = encryption(mode)
decrypt = decryptmessage(mode)
