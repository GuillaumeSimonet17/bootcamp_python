import sys

def get_argv():
    try:
        return (int(sys.argv[1]))
    except:
        print("AssertionError: argument is not an integer.")

def main():
    ac = len(sys.argv)
    if (ac == 1):
        return
    if (ac == 2):
        nb = get_argv()
        if (nb == 0):
            return print("I'm Zero.")
        if (nb % 2 == 0):
            return print("I'm Even.")
        return print("I'm Odd.")
    print("AssertionError: more than one argument are provided.")
    

if __name__ == "__main__":
    main()