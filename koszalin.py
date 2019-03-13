from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np


source = requests.get('http://rj.mzk.koszalin.pl/?linia=8').text
soup = BeautifulSoup(source, 'html.parser')

schedule_table = soup.find('table', {'class': 'trasa'})

schedule_1 = []
schedule_2 = []
titles = []
for row in schedule_table.find_all('tr'):
        cols = row.find_all('td')
        if len(cols) == 5:
            schedule_1.append((cols[1].text.strip()))
            schedule_2.append((cols[4].text.strip()))
        elif len(cols) == 3:
            titles.append((cols[0].text.strip()))
            titles.append((cols[2].text.strip()))

# convert list output to array
schedule_array = np.column_stack((schedule_1, schedule_2))

# convert array to dataframe
df = pd.DataFrame(schedule_array, columns=titles)
df.index = df.index + 1

print(df)

