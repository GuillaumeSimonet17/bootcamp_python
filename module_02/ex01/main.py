
def what_are_the_vars(*args, **kwargs):
    if not kwargs and not args:
        return None
    av = {}
    for key, value in kwargs.items():
        av[key] = value
    for i, n in enumerate(args):
        av['var_'+ str(i)] = n
    new = ObjectC(**av)
    return new

class ObjectC(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")

if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars(None, [])
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    # obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    # doom_printer(obj)
    # obj = what_are_the_vars(42, a=10, var_0="world")
    # doom_printer(obj)
    # obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
    # doom_printer(obj)