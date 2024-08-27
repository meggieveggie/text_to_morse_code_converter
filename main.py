MORSE_CODE_DICT = { 
    'A':'.-', 'B':'-...',
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

def encrypt(message):
    cipher = ''
    message = message.upper()
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
            continue
        cipher += ' '
    return cipher
 
def decrypt(message):
    message += ' '
    decipher = ''
    citext = ''
    whitespace_indicator = 0
    for letter in message:
        if (letter != ' '):
            whitespace_indicator = 0
            citext += letter
            continue

        whitespace_indicator += 1
        # If whitespace_indicator equals 2 it means there is a space between words
        if whitespace_indicator == 2 :
            decipher += ' '
            continue
        
        decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
        citext = ''
    return decipher
 
def main():
    encryption_map = { 
        "encrypt": encrypt,
        "decrypt": decrypt
    }
    encryption = input("Would you like to decrypt or encrypt: ")
    message = input(f"Type the word you want {encryption}ed: ")

    if encryption.lower() in encryption_map.keys():
        result = encryption_map.get(encryption.lower())(message)
        print (result)
        return
    
    print("Please indicate whether you would like to decrypt or encrypt")

if __name__ == '__main__':
    main()