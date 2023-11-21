
class Evaluator:

    @staticmethod
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        res = zip(coefs, words)
        tot = 0
        for c, w in res:
            tot += (len(w) * c)
        print(tot)

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        co = enumerate(coefs, start=0)
        wo = enumerate(words, start=0)
        tot = 0
        for (i, coef), (j, word) in zip(enumerate(coefs, start=0), enumerate(words, start=0)): 
            tot += (len(word) * coef)
        print(tot)
        
def main():
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    Evaluator.enumerate_evaluate(coefs, words)

if __name__ == "__main__":
    main()