MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
   'C':'-.-.', 'D':'-..', 'E':'.',
   'F':'..-.', 'G':'--.', 'H':'....',
   'I':'..', 'J':'.---', 'K':'-.-',
   'L':'.-..', 'M':'--', 'N':'-.',
   'O':'---', 'P':'.--.', 'Q':'--.-',
   'R':'.-.', 'S':'...', 'T':'-',
   'U':'..-', 'V':'...-', 'W':'.--',
   'X':'-..-', 'Y':'-.--', 'Z':'--..',
   '1':'.----', '2':'..---', '3':'...--',
   '4':'....-', '5':'.....', '6':'-....',
   '7':'--...', '8':'---..', '9':'----.',
   '0':'-----', ', ':'--..--', '.':'.-.-.-',
   '?':'..--..', '/':'-..-.', '-':'-....-',
   '(':'-.--.', ')':'-.--.-'
}
def encryption(message):
    cipher=''
    for letter in message:
        if letter !='':
            cipher += MORSE_CODE_DICT[letter]+''
        else:
            cipher +=''
            return cipher
#morse code to english
def decryption(message):
    message +=''
    decipher=''
    text=''
    for letter in message:
        if letter != '':
            i=0
            text+=letter
        else:
            i +=1
            if i==2:
                decipher+=''
            else:
                decipher+=list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(text)]
                text=''
    return decipher
def main():
    message1= "H e l l o  S c h o l a r s "
    output=encryption(message1.upper())
    print(output)
    message1=".... . .-.. .-..---....-.-. ....--.-.. .-.-. ..."
    output=decryption(message1)
    print(output)
    if __name__=='__main__':
        main()
