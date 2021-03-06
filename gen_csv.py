"""
The following module reads locations.list file, modifies it and writes to a
data.csv file.

NOTE: because of the huge amount of time demanded for the analysis, the module
selects and writes only 300 000 elements (line 88) to the file.
"""

import re
import pandas as pd


def read_list():
    '''
    The following function reads "locations.list" file and generates a list.
    Is not needed to be run, already created a list for lists, used by
    convert_to_df() function to write a data.csv file.
    '''

    with open('locations.list', 'r') as data:

        filtered = []
        coordinates = data.readlines()
        for line in coordinates:

            line = line.replace('UK', 'United Kingdom')
            line = line.replace('USA', 'United States')
            line = line.split('\t')

            if len(line) > 1:
                name = line[0]
                date = re.findall('[/(/)0-9/?]{4,100}', name)

                name = re.sub('#[0-9]{1,3}.[0-9]{1,3}', '', name)

                if '{' in name:
                    index = name.find('{')
                    name = name[:index]

                if '(' in name:
                    index = name.find('(')
                    name = name[:index]

                if '"' in name:
                    name = name.replace('"', '')

                try:
                    date = int(date[0][1:-1])
                except ValueError:
                    continue

                location = line[-1]

                if len(re.findall('[/(/)0-9/?]{4,100}', location)) != 0:
                    index = location.find('(')
                    location = location[:index]

                location = location.replace('\n', '')

                if ',' not in location:

                    location = line[-2]
                    filtered.append([name[:-1], date, line[-2]])

                else:
                    filtered.append([name[:-1], date, location])

        return filtered


def convert_to_df(lst: list):
    '''
    The following function creates a data.csv file from a list of lists,
    generated by the read__list function.

    Is not needed to be run. Already generated the file.
    '''
    data = pd.DataFrame(lst)
    data.columns = ['Title', 'Year', 'Location']

    data = data.dropna(how='any')

    data = data[data['Location'].str.contains('{') == False]
    data = data[data['Location'].str.contains('}') == False]
    data = data[data['Location'] != '']

    data = data.sample(n=300000)
    data.to_csv('data.csv', index=False)


if __name__ == "__main__":

    raw_data = read_list()
    convert_to_df(raw_data)
