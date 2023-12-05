from FileLoader import FileLoader
loader = FileLoader()
data = loader.load('../dataset/athlete_events.csv')

from HowManyMedals import HowManyMedals
res = (HowManyMedals.how_many_medals(data, 'Kjetil Andr Aamodt'))
print(res)