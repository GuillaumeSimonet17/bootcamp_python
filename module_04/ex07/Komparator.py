from FileLoader import FileLoader
from MyPlotLib import MyPlotLib
import matplotlib.pyplot as plt
import seaborn as sns


class Komparator:

    def __init__(self, data):
        self.data = data

    def compare_box_plots(self, categorical_var, numerical_var):
        if categorical_var not in self.data.columns or numerical_var not in self.data.columns:
            print(f"Les variables {categorical_var} ou {numerical_var} ne sont pas présentes dans le dataset.")
            return

        sns.boxplot(x=categorical_var, y=numerical_var, data=self.data)
        plt.title(f"Comparaison des distributions de {numerical_var} par catégorie de {categorical_var}")
        plt.show()

    def density(self, categorical_var, numerical_var):
        if categorical_var not in self.data.columns or numerical_var not in self.data.columns:
            print(f"Les variables {categorical_var} ou ne sont pas présentes dans le dataset.")
            return

        sns.kdeplot(data=self.data, x=numerical_var, hue=categorical_var, fill=True, common_norm=False)
        plt.title(f"Densite de {numerical_var} par catégorie de {categorical_var}")
        plt.show()

    def compare_histograms(self, categorical_var, numerical_var):
        sns.histplot(data=self.data, x=numerical_var, hue=categorical_var, multiple="stack")
        plt.title(categorical_var)
        plt.show()


loader = FileLoader()
data = loader.load('../dataset/athlete_events.csv')

komp = Komparator(data)
komp.compare_histograms("Sport", "Height")