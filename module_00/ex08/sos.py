import sys
import re

morse = {
    'A': ".-",
    'B': "-...",
    'C': "-.-.",
    'D': "-..",
    'E': ".",
    'F': "..-.",
    'G': "--.",
    'H': "....",
    'I': "..",
    'J': ".---",
    'K': "-.-",
    'L': ".-..",
    'M': "--",
    'N': "-.",
    'O': "---",
    'P': ".--.",
    'Q': "--.-",
    'R': ".-.",
    'S': "...",
    'T': "-",
    'U': "..-",
    'V': "...-",
    'W': ".--",
    'X': "-..-",
    'Y': "-.--",
    'Z': "--..",
    '0': "-----",
    '1': ".----",
    '2': "..---",
    '3': "...--",
    '4': "....-",
    '5': ".....",
    '6': "-....",
    '7': "--...",
    '8': "---..",
    '9': "----.",
}

def merge_string(tab, nb):
    the_string = ""
    for string in tab[1:]:
        the_string += (string + ' ')
    return the_string[:-1]

def morse_code(to_encode):

    regex = re.compile('[^A-Za-z0-9 ]')
    if bool(regex.search(to_encode)):
        print('ERROR')
        return

    for letter in to_encode:
        if letter in morse:
            print(morse[letter], end=' ')
        if letter == ' ':
            print(' / ', end="")
        


def main():
    ac = len(sys.argv)
    if ac == 1:
        print("Write at leat one word")
        return
    if ac > 2:
        morse_code((merge_string(sys.argv, ac-1)).upper())
    else:
        morse_code((sys.argv[1]).upper())

if __name__ == "__main__":
    main()