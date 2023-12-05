

class HowManyMedalsByCountry:

    @staticmethod
    def how_many_medals_by_country(data, country_name):
        if data is None: return None
        '''
            return nb et type of medal for each competition where the country won medal
            {
                year: {
                    'G':
                    'S':
                    'B':
                }
            }
        '''
        res = {}

        data_country = data[data['Team'] == country_name]

        for year in data_country['Year'].unique():
            medals_year = data_country[data_country['Year'] == year]
            medals_count = {
                'G': len(medals_year[medals_year['Medal'] == 'Gold']),
                'S': len(medals_year[medals_year['Medal'] == 'Silver']),
                'B': len(medals_year[medals_year['Medal'] == 'Bronze'])
            }
            res[year] = medals_count
        return res