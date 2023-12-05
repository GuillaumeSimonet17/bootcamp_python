import pandas as pd

class FileLoader:

    def load(self, path):
        try:
            df = pd.read_csv(path)
            print('Dimensions: ', df.shape)
            return df
        except:
            return None


    def display(self, df, n):
        if df is None: return None
        if n < 0:
            return print(df.tail(n*-1))
        return print(df.head(n))


