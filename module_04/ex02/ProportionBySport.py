

class ProportionBySport:

    @staticmethod
    def proportion_by_sport(data, year, sport, gender):
        '''
            return percent of participants who played the given sport among the participants of the given gender.
        '''
        gender_selected = data[data['Sex'] == gender]
        sport_selected = gender_selected[gender_selected['Sport'] == sport]
        year_selected = sport_selected[sport_selected['Year'] == year]
        return (len(year_selected) * 100) / len(data)
