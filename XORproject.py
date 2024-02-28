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
    ncryptsent = ""

    for i in range(len(sentence)):

        ncryptsent += XORonLetter(sentence[i], key[i])

    return ncryptsent

print(XORonSentence("$L&MK", "world"))
print(XORonSentence("sussy", "world"))
    
