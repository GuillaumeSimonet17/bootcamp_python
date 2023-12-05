from FileLoader import FileLoader
from pprint import pprint 
from HowManyMedalsByCountry import HowManyMedalsByCountry
loader = FileLoader()
data = loader.load('../dataset/athlete_events.csv')
res = HowManyMedalsByCountry.how_many_medals_by_country(data, 'France')
pprint(res)