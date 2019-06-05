import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy
import datetime



inputFile = 'd02_robin_geo.db'
outputFileRural = 'd03_robin_rural.db'
outputFileUrban = 'd03_robin_urban.db'

# start = datetime.date(year, 2, 1)
# end = datetime.date(year, 5, 1)


disk_engine_clean = create_engine('sqlite:///' + inputFile)
disk_engine_rural = create_engine('sqlite:///' + outputFileRural)
disk_engine_urban = create_engine('sqlite:///' + outputFileUrban)

sqlDtypes = {
        'count': sqlalchemy.Integer(), 
        'state':  sqlalchemy.types.String(),
        'lat': sqlalchemy.types.Float(),
        'long': sqlalchemy.types.Float(),
        'date': sqlalchemy.types.DateTime(),
        'urban': sqlalchemy.types.Boolean()}

df = pd.read_sql_query('SELECT * FROM data WHERE`lat` < {}'.format(33.5), disk_engine_clean)
df = df[['date','count','urban']]

df['date'] = pd.to_datetime(df['date'])

df_filtered_r = df[(df['date'] >= str(2000) + '-2-1') & (df['date'] < str(2000) + '-5-1') & (df['urban'] == 0)]
df_filtered_u = df[(df['date'] >= str(2000) + '-2-1') & (df['date'] < str(2000) + '-5-1') & (df['urban'] == 1)]

for year in [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]:
	temp = df[(df['date'] >= str(year) + '-2-1') & (df['date'] < str(year) + '-5-1') & (df['urban'] == 0)]
	df_filtered_r = pd.concat([df_filtered_r, temp])

	temp = df[(df['date'] >= str(year) + '-2-1') & (df['date'] < str(year) + '-5-1') & (df['urban'] == 1)]
	df_filtered_u = pd.concat([df_filtered_u, temp])


aggregation_functions = {'date': 'first', 'count': 'sum', 'urban': 'first'}
df_filtered_r = df_filtered_r.groupby(df_filtered_r['date']).aggregate(aggregation_functions)
df_filtered_u = df_filtered_u.groupby(df_filtered_u['date']).aggregate(aggregation_functions)


disk_engine_rural.execute('DROP TABLE IF EXISTS data')
df_filtered_r.to_sql('data', disk_engine_rural, if_exists='append', index=False, dtype=sqlDtypes)

disk_engine_urban.execute('DROP TABLE IF EXISTS data')
df_filtered_u.to_sql('data', disk_engine_urban, if_exists='append', index=False, dtype=sqlDtypes)







	