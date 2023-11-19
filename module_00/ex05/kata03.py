kata = "The right format"

def main():
    nb_t = 42 - len(kata)-1
    print(f'{"-" * nb_t}{kata}')

if __name__ == "__main__":
    main()