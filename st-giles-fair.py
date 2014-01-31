# See http://www.oxford.gov.uk/PageRender/decVanilla/StGilesFair.htm
import copy
from datetime import date, timedelta
import json
import sys

skeleton = {
    "title": "Dates of the St Giles' Fair",
    "description": "Find out when St Giles' Fair comes to Oxford. Relevant as some places along St Giles are shut.",
    "divisions": {
        "st-giles": {
            "title": "St Giles"
        }
    }
}

def get_dates(year):
    # The fair is held on the Monday and Tuesday following the first Sunday
    # after St Giles' Day (1 September).

    st_giles_day = date(year, 9, 1)

    # First Sunday after St Giles Day
    first_sunday_hence = st_giles_day + timedelta(7 - (st_giles_day.isoweekday() % 7))

    monday = first_sunday_hence + timedelta(1)
    tuesday = first_sunday_hence + timedelta(2)

    return [monday, tuesday]

def generate(years):
    data = copy.deepcopy(skeleton)
    target = data['divisions']['st-giles']

    for year in years:
        target[str(year)] = [{"date": d.strftime("%Y-%m-%d")} for d in get_dates(year)]
        
    return data

if __name__ == '__main__':
    data = generate(range(2000, 2200))
    json.dump(data, sys.stdout, indent=2, sort_keys=True)
