
def ft_filter(function_to_apply, iterable):
    """
    Filter the result of function apply to all elements of the iterable.
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
            if function_to_apply(el):
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
    it = ft_filter(lambda dum: not (dum % 2), iterable)
    # it = filter(lambda dum: not (dum % 2), iterable)
    print(it)
    print(list(it))

if __name__ == "__main__":
    main()
