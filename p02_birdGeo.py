import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy
import georasters as gr

print('a')


inputFile = 'd01_robin_clean.db'
outputFile = 'd02_robin_geo.db'
states = ("US-AL", "US-AR", "US-AZ", "US-CA", "US-CO", "US-FL", "US-GA", "US-KS", "US-KY", "US-LA", "US-MO", "US-MS", "US-NC", "US-NM", "US-NV", "US-OK", "US-SC", "US-TN", "US-TX", "US-UT", "US-VA")

raster = 'raster.tif'
data = gr.from_file(raster)

disk_engine_clean = create_engine('sqlite:///' + inputFile)
disk_engine = create_engine('sqlite:///' + outputFile)

sqlDtypes = {
        'count': sqlalchemy.Integer(), 
        'state':  sqlalchemy.types.String(),
        'lat': sqlalchemy.types.Float(),
        'long': sqlalchemy.types.Float(),
        'date': sqlalchemy.types.DateTime(),
        'urban': sqlalchemy.types.Boolean()}

df = pd.read_sql_query('SELECT * FROM data WHERE `state` IN  {}'\
	        .format(states), disk_engine_clean)

df['date'] = pd.to_datetime(df['date'])

df['urban'] = data.map_pixel(df.long, df.lat) > 0


disk_engine.execute('DROP TABLE IF EXISTS data')
df.to_sql('data', disk_engine, if_exists='append', index=False, dtype=sqlDtypes)