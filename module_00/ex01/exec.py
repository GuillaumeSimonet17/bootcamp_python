import sys

def main():
    argc = len(sys.argv)
    if argc == 1:
        return
    print(get_arg(argc))

def get_arg(argc):
    string = ""
    for n in range(1, argc):
        string += sys.argv[n]
        if (n < argc - 1):
            string += " "
    return string[::-1].swapcase()


if __name__ == "__main__":
    main()