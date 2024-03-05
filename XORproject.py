import math
characters = [
    # lowercase characters
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    # uppercase characters
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    # space and symbols
    ' ',',','.','?','!','@','#','$','&','*','(',')'
]

# use this method to encode an alphabet character into a binary string
def encode(character):
    charIndex = characters.index(character)
    return '{0:06b}'.format(charIndex)

# use this method to decode a binary string into an alphabet character
def decode(binary):
    charIndex = int(binary, 2)
    return characters[charIndex]

def XOR(bit1, bit2):
    if bit1==bit2:
        return '1'
    else:
        return '0'

def XORonByte(byte, key):
    emsg = ""
    for i in range(len(byte)):
        emsg += XOR(byte[i], key[i])
    return emsg 

def XORonLetter(letter, keyLetter):

    ltrBin = encode(letter)
    keyltrBin = encode(keyLetter)
    
    ncryptltr = XORonByte(ltrBin, keyltrBin)

    return decode(ncryptltr)

def XORonSentence(sentence, key):
    key = generateKey(sentence, key)
    ncryptsent = ""

    for i in range(len(sentence)):

        ncryptsent += XORonLetter(sentence[i], key[i])

    return ncryptsent

def generateKey(msg, key):
    if len(msg) == len(key):
        return key

    elif len(msg) < len(key):
        key[0:len(msg)]
        return key

    else: 
        genkey = ""
        remainder = len(msg)%len(key)
        for i in range(math.floor(len(msg)/len(key))):
            genkey += key
        genkey += key[0:remainder]
        return genkey
        

msg = input("Please enter a message you want to encypt: ")
key = input("Please Enter a key: ")
print("Your encrypted message is ", XORonSentence(msg, key))

    
