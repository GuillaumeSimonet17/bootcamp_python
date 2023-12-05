from YoungestFellah import YoungestFellah
from FileLoader import FileLoader

loader = FileLoader()
data = loader.load('../dataset/athlete_events.csv')
print(YoungestFellah.youngest_fellah(data, 2004))