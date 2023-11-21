
def ft_map(function_to_apply, iterable):
    """
    Map the function to all elements of the iterable.
        Args:
            function_to_apply: a function taking an iterable.
            iterable: an iterable object (list, tuple, iterator).
        Return:
            An iterable.
            None if the iterable can not be used by the function.
    """
    if not is_iterable(iterable):
        return None
    try:
        for index, el in enumerate(iterable):
            el = function_to_apply(el)
            yield el
        return iterable
    except:
        return None

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

def main():
    iterable = [1, 2, 3, 4, 5]
    # it = ft_map(lambda dum: dum + 1, iterable)
    it = map(lambda dum: dum + 1, iterable)
    print(list(it))
    print(it)

if __name__ == "__main__":
    main()