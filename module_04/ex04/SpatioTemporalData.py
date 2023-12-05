

class SpatioTemporalData:

    def __init__(self, data):
        self.data = data

    def when(self, location):
        if self.data is None: return None
        return (self.data[self.data['City'] == location]['Year']).unique().tolist()

    def where(self, date):
        if self.data is None: return None
        return (self.data[self.data['Year'] == date]['City']).unique().tolist()

