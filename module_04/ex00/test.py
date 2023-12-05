from FileLoader import FileLoader

loader = FileLoader()
data = loader.load("../dataset/athlete_events.csv")
loader.display(data, -5)
