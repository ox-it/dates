# See http://www.ox.ac.uk/about_the_university/university_year/dates_of_term.html
import copy
from datetime import timedelta
import json
import sys

import oxford_term_dates

skeleton = {
    "title": "Dates of Term",
    "description": "Dates of Term for the University of Oxford",
    "divisions": {
        "full-term": {
             'title': "Full Term"
        }
    }
}

def get_dates(year):
    dates = []
    for term in oxford_term_dates.TERM_NAMES:
        try:
            term_start = oxford_term_dates.TERM_STARTS[(year, term)]
        except KeyError:
            continue
        for week in range(1, 9):
            for day in range(0, 7):
                date = term_start + timedelta(7*week+day)
                ox_date_dict = oxford_term_dates.ox_date_dict(date)
                dates.append({
                    'date': date.strftime('%Y-%m-%d'),
                    'title': '{day_name} of {week}{ordinal} week, {term_long} {year}'.format(**ox_date_dict),
                    #'oxfordDate': ox_date_dict,
                })
    return dates

def generate():
    data = copy.deepcopy(skeleton)

    years = sorted(set(year for (year, term) in oxford_term_dates.TERM_STARTS))
    for year in years:
        data['divisions']['full-term'][str(year)] = get_dates(year)

    return data

if __name__ == '__main__':
    data = generate()
    json.dump(data, sys.stdout, indent=2, sort_keys=True)
