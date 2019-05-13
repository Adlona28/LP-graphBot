import csv
import pandas as pd
url = 'https://github.com/jordi-petit/lp-graphbot-2019/blob/master/dades/worldcitiespop.csv.gz?raw=true'
cityName = 'City'
lon = 'Longitude'
lat = 'Latitude'
population = 'Population'
df = pd.read_csv(url, usecols=[cityName, lon, lat, population])
for row in df.itertuples():
    
