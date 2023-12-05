import pandas as pd

class YoungestFellah:

    @staticmethod
    def youngest_fellah(data, year):
        try:
            year_selected = data[data['Year'] == year]
            men_data = year_selected[year_selected['Sex'] == 'M']
            women_data = year_selected[year_selected['Sex'] == 'F']

            youngest_man = men_data.loc[men_data['Age'].idxmin()]
            youngest_woman = women_data.loc[women_data['Age'].idxmin()]

            return {
                'F':youngest_man['Age'],
                'M':youngest_woman['Age']
            }
        except:
            return None
        