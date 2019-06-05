import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy
import datetime


inputFile = 'd02_robin_geo.db'


def filterDB(inputFile, start, end, states, lat):

	if(states == 'all'):
		states = ("US-AL", "US-AR", "US-AZ", "US-CA", "US-CO", "US-FL", "US-GA", "US-KS", "US-KY", "US-LA", "US-MO", "US-MS", "US-NC", "US-NM", "US-NV", "US-OK", "US-SC", "US-TN", "US-TX", "US-UT", "US-VA")


	outputFile = 'd03_robin/d03_robin_{}_filter.db'.format(start.year)
	outputFileCSV = 'c03_robin/c03_robin_{}_filter.csv'.format(start.year)

	disk_engine_clean = create_engine('sqlite:///' + inputFile)
	disk_engine = create_engine('sqlite:///' + outputFile)
	
	sqlDtypes = {
	        'count': sqlalchemy.Integer(), 
	        'state':  sqlalchemy.types.String(),
	        'lat': sqlalchemy.types.Float(),
	        'long': sqlalchemy.types.Float(),
	        'date': sqlalchemy.types.DateTime(),
	        'urban': sqlalchemy.types.Boolean()}

	df = pd.read_sql_query('SELECT * FROM data WHERE\
	        `date` > "{}" AND\
	        `date` < "{}" AND\
	        `state` IN  {} AND\
	        `lat` < {}'\
	        .format(start,end,states,lat), disk_engine_clean)


	df['date'] = pd.to_datetime(df['date'])


	print(df)

	df.to_csv(outputFileCSV, sep=',')
	disk_engine.execute('DROP TABLE IF EXISTS data')
	df.to_sql('data', disk_engine, if_exists='append', index=False, dtype=sqlDtypes)



for year in [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]:
	start = datetime.date(year, 2, 1)
	end = datetime.date(year, 5, 1)
	states = 'all'
	lat = 33.5
	filterDB(inputFile, start, end, states, lat)