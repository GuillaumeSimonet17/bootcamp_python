import functools

def ft_reduce(function_to_apply, iterable):
    """
    Apply function of two arguments cumulatively.
        Args:
            function_to_apply: a function taking an iterable.
            iterable: an iterable object (list, tuple, iterator).
        Return:
            A value, of same type of elements in the iterable parameter.
            None if the iterable can not be used by the function.
    """
    if not is_iterable(iterable):
        return None
    try:
        it = iter(iterable)
        res = next(it)
        for el in it:
            res = function_to_apply(res, el)
        return res
    except:
        return None

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

def main():
    lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
    it = functools.reduce(lambda u, v: u + v, lst)
    print((it))
    it = ft_reduce(lambda u, v: u + v, lst)
    # print(list(it))
    print((it))

if __name__ == "__main__":
    main()
