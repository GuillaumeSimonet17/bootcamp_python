
class HowManyMedals:

    @staticmethod
    def how_many_medals(data, name):
        '''
            return le nb de medaille gagner par {name} dans toutes les annees
        '''
        res = {}

        data_name = data[data['Name'] == name]

        # pour chaque annee compter nb medal
        for year in data_name['Year'].unique():
            medals_year = data_name[data_name['Year'] == year]
            medals_count = {
                'G': len(medals_year[medals_year['Medal'] == 'Gold']),
                'S': len(medals_year[medals_year['Medal'] == 'Silver']),
                'B': len(medals_year[medals_year['Medal'] == 'Bronze'])
            }
            res[year] = medals_count

        return res
