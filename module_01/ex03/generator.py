import random

def generator(text, sep, option=None):
    """
        Splits the text according to sep value and yield the substrings.
        option precise if a action is performed to the substrings before it is yielded.
    """

    if not isinstance(text, str) or option not in ["shuffle", "unique", "ordered", None]:
        return "Error"
    lst = text.split(sep)
    if not option is None:
        if option == "shuffle":
            lst = fisher_yates_shuffle(lst)
        if option == "unique":
            unique_lst = set(lst)
            lst = sorted(unique_lst, key=lst.index)
        if option == "ordered":
            lst = sorted(lst)
    for word in lst:
        yield word

def fisher_yates_shuffle(input_list):
    shuffled_list = input_list.copy()

    for i in range(len(shuffled_list) - 1, 0, -1):
        j = random.randint(0, i)
        shuffled_list[i], shuffled_list[j] = shuffled_list[j], shuffled_list[i]

    return shuffled_list

def main():
    text = "Le Lorem Lorem le Le Ipsum est simplement du faux texte."
    for word in generator(text, sep=" ", option="unique"):
        print(word)

if __name__ == "__main__":
    main()