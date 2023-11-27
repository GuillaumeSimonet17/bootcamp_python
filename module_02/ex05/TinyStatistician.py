import numpy as np
import math

class TinyStatistician:

    def check_tab(self, x):
        if isinstance(x, list) or isinstance(x, np.ndarray):
            return True
        return False

    def check_len(self, x):
        try:
            nb_el = len(x)
            if nb_el == 0:
                return None
            return nb_el
        except:
            return None

    def mean(self, x):
        try:
            nb_el = self.check_len(x)
            if nb_el is None or self.check_tab(x) is False:
                return None
            res = 0
            for i in x:
                res += i
            return res/nb_el
        except:
            print('pas un tab')

    def median(self, x):
        nb_el = self.check_len(x)
        if nb_el is None or self.check_tab(x) is False:
            return None
        ordered = sorted(x)
        if (nb_el) % 2 != 0:
            nb_el += 1
            return ordered[round(nb_el/2)-1]
        else:
            return (ordered[round((nb_el/2)-1)] + ordered[round((nb_el/2))]) / 2 
            
    def quartiles(self, x):
        nb_el = self.check_len(x)
        if nb_el is None or self.check_tab(x) is False:
            return None
        p25 = (nb_el + 3) / 4
        p75 = ((nb_el * 3) + 1) / 4
        ret = []
        ordered = sorted(x)
        q1 = float(ordered[math.ceil(p25) - 1])
        ret.append(q1)
        try:
            q3 = float(ordered[math.ceil(p75) - 1])
            ret.append(q3)
        except:
            q3 = float(ordered[nb_el - 1])
            ret.append(q3)
        return ret

    def var(self, x):
        nb_el = self.check_len(x)
        if nb_el is None or self.check_tab(x) is False:
            return None
        mean = self.mean(x)
        res = 0
        for n in x:
            res += (n - mean)**2
        return res / nb_el 

    def std(self, x):
        nb_el = self.check_len(x)
        if nb_el is None or self.check_tab(x) is False:
            return None
        return math.sqrt(self.var(x))

def main():
    obj = TinyStatistician()
    # lst = [1, 2.5, 4, 5, 8]
    # lst = [1, 2.5, 1, 2.5, 5, 8]
    # lst = [1, 1, 1, 1, 1, 1]
    # lst = [8]
    # lst = []
    lst = [1, 42, 300, 10, 59]
    print(obj.mean(lst))
    print(obj.median(lst))
    print(obj.quartiles(lst))
    print(obj.var(lst))
    print(obj.std(lst))

if __name__ == "__main__":
    main()