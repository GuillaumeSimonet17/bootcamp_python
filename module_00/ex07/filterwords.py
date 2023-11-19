import sys
import string

def filterword(to_split, number):
    res = []
    # remove punctuation
    table = str.maketrans("", "", string.punctuation)
    new_str = to_split.translate(table)
    
    res = new_str.split(" ")
    res = list(filter(lambda el: len(el) > number, res))
    print(res)


def main():
    if len(sys.argv) == 3:
        try:
            number = int(sys.argv[2])
        except:
            return print("Error")
        filterword(sys.argv[1], number)
        return
    return print("ERROR")

if __name__ == "__main__":
    main()
