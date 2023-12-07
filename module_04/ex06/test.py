from FileLoader import FileLoader
from MyPlotLib import MyPlotLib

loader = FileLoader()
data = loader.load('../dataset/athlete_events.csv')

plot = MyPlotLib()
plot.box_plot(data, ["Height", "Weight"])