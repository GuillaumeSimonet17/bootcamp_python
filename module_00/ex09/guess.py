import random

def main():
    random_nb = random.random()
    random_int = random.randint(1, 99)
    count = 0
    while 1:
        res = input("What's your guess between 1 and 99?\n")
        if res == 'exit':
            print("Goodbye!")
            return
        count+=1
        try:
            nb = int(res)
        except:
            print("That's not a number.")
        if nb < random_int:
            print("Too low!")
        elif nb > random_int:
            print("Too high!")
        else:
            if nb == 42:
                print("The answer to the ultimate question of life, the universe and everything is 42.") 
            if count == 1:
                return print("Congratulations! You got it on your first try!")
            print("Congratulations, you've got it!")
            return print(f"You won in {count} attempts!")

if __name__ == "__main__":
    main()