import sys

def operations(nb1, nb2):
    print(f'Sum: {nb1 + nb2}')
    print(f'Difference: {nb1 - nb2}')
    print(f'Product: {nb1 * nb2}')
    if nb2 == 0:
        print('Quotient: ERROR (division by zero)')
        print('Remainder: ERROR (modulo by zero)')
    else:
        print(f'Quotient: {nb1 / nb2}')
        print(f'Remainder: {nb1 % nb2}')

def get_args():
    try:
        nb1 = int(sys.argv[1])
        nb2 = int(sys.argv[2])
        operations(nb1, nb2)
    except:
        print("AssertionError: only integers")

def main():
    ac = len(sys.argv)
    if ac == 1 or ac == 2:
        return print("Usage: python operations.py <number1> <number2>\nExample: python operations.py 10 3")
    if ac == 3:
        return get_args()
    print("AssertionError: too many arguments")

    

if __name__ == "__main__":
    main()

