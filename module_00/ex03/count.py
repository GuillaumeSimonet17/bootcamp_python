import string
import sys

def text_analyzer(arg=""):
    """
        This function counts the number of upper characters, lower characters,
        punctuation and spaces in a given text.
    """
    if not isinstance(arg, str):
        return print("AssertionError: argument is not a string")
    if (arg == ""):
        arg = input("What is the text to analyze?\n")
    
    nb_char = len(arg)
    nb_up =  sum(1 for char in arg if char.isupper())
    nb_low = sum(1 for char in arg if char.islower())
    nb_punct = sum(1 for char in arg if char in string.punctuation)
    nb_space = sum(1 for char in arg if char.isspace())
    print(f'The text contains {nb_char} character(s):')
    print(f'- {nb_up} upper letters(s)')
    print(f'- {nb_low} lower letters(s)')
    print(f'- {nb_punct} punctuation mark(s)')
    print(f'- {nb_space} space(s)')

def main():
    if len(sys.argv) == 2:
        return text_analyzer(sys.argv[1])
    return print("I'm waiting only one string bro, so calm down.")

if __name__ == "__main__":
    main()
