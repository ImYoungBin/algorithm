# decode_morse('.... . -.--   .--- ..- -.. .')
# should return "HEY JUDE"

def decode_morse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message 
    lst = morse_code.replace('   ', '  ').split(' ')
    words = []
    print(lst)
    for i in lst:
        if i != '':  
            words.append(MORSE_CODE[i])
            print(words)
        else:
            words.append(' ')
    words = "".join(words)
    print(words)
    return words.strip()

