import pandas as pd
from sqlalchemy import create_engine
import datetime as dt
from math import floor
from pprint import pprint
import sqlalchemy

inputFile = 'd02_robin_geo.db'

dfSubsets = []
dateSubsets = []


disk_engine = create_engine('sqlite:///' + inputFile)
df = pd.read_sql_query('SELECT `count`, `date`, `lat`, `long`, `urban` FROM data', disk_engine)

print('aaaaadasdda')
print(df)

df['date'] = pd.to_datetime(df['date'])
df['date'] = df['date'].dt.dayofyear
df = df.sort_values('date')
df = df.reset_index(drop=True)





temp = []
for index,row in df.iterrows():
	print('c')
	temptemp = [[ row['date'], row['urban'], row['lat'], row['long'] ]] * int(row['count'])
	temp.extend(temptemp)


print(len(temp))

df_temp = pd.DataFrame(temp)

df_temp = df_temp.rename(columns={'0': 'date', '1': 'urban', '2': 'lat', '3': 'long'})

print(df_temp)

disk_engine_temp = create_engine('sqlite:///05_robin_mapper.db')
disk_engine_temp.execute('DROP TABLE IF EXISTS data')
sqlDtypes = {
    'date': sqlalchemy.Integer(), 
    'lat':  sqlalchemy.types.Float(),
    'long':  sqlalchemy.types.Float(),
    'urban': sqlalchemy.types.Integer()}


df_temp.to_sql('data', disk_engine_temp, if_exists='append', index=False, dtype=sqlDtypes)

