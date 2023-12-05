from FileLoader import FileLoader
from ProportionBySport import ProportionBySport

loader = FileLoader()
data = loader.load('../dataset/athlete_events.csv')
print(ProportionBySport.proportion_by_sport(data, 2004, 'Tennis', 'F'))
