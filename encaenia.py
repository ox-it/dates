# See http://www.ox.ac.uk/about_the_university/university_year/dates_of_term.html#5Ref
import copy
import json
import sys

skeleton = {
    'title': 'Dates of Encaenia',
    'divisions': {
        'university-of-oxford': {
             'title': 'University of Oxford'
        }
    }
}

dates = [
    '2014-06-25',
    '2015-06-24',
    '2016-06-22',
    '2017-06-21',
    '2018-06-20',
    '2019-06-26',
    '2020-06-25',
]

if __name__ == '__main__':
    data = copy.deepcopy(skeleton)
    for date in dates:
        data['divisions']['university-of-oxford'][date[:4]] = {
            'date': date
        }
    json.dump(data, sys.stdout, indent=2, sort_keys=True)
