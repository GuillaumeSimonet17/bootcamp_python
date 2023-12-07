import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd

class MyPlotLib:

    @staticmethod
    def histogram(data, features):
        '''
            plots one histogram for each numerical feature in the list
        '''
        if data is None or features is None: return None
        for i, el in enumerate(features, 1):
            try:
                int(data[el][0])
            except:
                print('some feature in the list are not numerical')
                return
            plt.subplot(len(features), 1, i)
            plt.hist(data[el], bins=range(round(min(data[el])), round(max(data[el]) + 1)), edgecolor='black', alpha=0.7)
            plt.title(el)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def density(data, features):
        '''
            plots the density curve of each numerical feature in the list
        '''
        if data is None or features is None: return None
        for el in features:
            try:
                int(data[el][0])
            except:
                print('some feature in the list are not numerical')
                return
            sb.kdeplot(data[el], label=el)
        plt.legend()
        plt.show()

    @staticmethod
    def pair_plot(data, features):
        if data is None or features is None: return None
        new_data = []
        df = pd.DataFrame()
        for el in features:
            try:
                int(data[el][0])
                new_data.append(data[el])
            except:
                print('some feature in the list are not numerical')
                return
        df = (pd.concat(new_data, axis=1, keys=features))
        sb.pairplot(df)
        plt.show()

    @staticmethod
    def box_plot(data, features):
        '''
            displays a box plot for each numerical variable in the dataset
        '''
        if data is None or features is None: return None
        for i, el in enumerate(features, 1):
            try:
                int(data[el][0])
            except:
                print('some feature in the list are not numerical')
                return
            plt.subplot(len(features), 1, i)
            # plt.figure(figsize=(8,6))
            sb.boxplot(x=data[el])
        plt.tight_layout()
        plt.show()
