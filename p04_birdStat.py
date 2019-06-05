import pandas as pd
from sqlalchemy import create_engine
import datetime
from math import floor
from pprint import pprint

inputFile_unfilter = 'robin_filter_03.db'
inputFile_filter = 'robin_filter_03.db'





def percentile(start, end):

	inputFile_filter = 'robin_{}_{}_03_filter.db'.format(start.year, end.year)

	disk_engine = create_engine('sqlite:///' + inputFile_filter)
	df = pd.read_sql_query('SELECT * FROM data ORDER BY date', disk_engine)

	df['date'] = pd.to_datetime(df['date'])

	df_urban = df.loc[df['urban'] == True, ['count', 'date']]
	df_rural = df.loc[df['urban'] == False, ['count', 'date']]

	l = [None] * 3

	print('all')
	l[0] = percentileDF(df)
	print('urban')
	l[1] = percentileDF(df_urban)
	print('rural')
	l[2] = percentileDF(df_rural)

	l = [item for sublist in l for item in sublist]
	return l



def percentileParam(inputFile_unfilter, start, end, states, lat):

	inputFile_filter = 'robin_{}_{}_03_filter.db'.format(start.year, end.year)

	filterPy = __import__('03_birdFilter')
	filterPy.filterDB(inputFile_unfilter, start, end, states)

	percentile(start, end)

def percentileDF(df):
	l = []
	aggregation_functions = {'date': 'first', 'count': 'sum'}
	df = df.groupby(df['date']).aggregate(aggregation_functions)

	totCount = df['count'].sum()

	for p in [.5,.9,.95]:
		percentileCount = floor(totCount * p)
		index = -1

		for rowIndex in range(len(df)):

			percentileCount = percentileCount - df.iloc[rowIndex]['count']

			if(percentileCount <= 0):
				l.append(str(df.iloc[rowIndex]['date']))
				print(str(p) + ": " + str(df.iloc[rowIndex]['date']))
				break
	return l


tbl = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007 ,2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
l = [None] * 1000
for i in range(len(tbl)):
	year = tbl[i]
	start = datetime.date(year, 8, 7)
	end = datetime.date(year + 1, 1, 1)
	states = ("US-AL", "US-AR", "US-AZ", "US-CA", "US-CO", "US-FL", "US-GA", "US-KS", "US-KY", "US-LA", "US-MO", "US-MS", "US-NC", "US-NM", "US-NV", "US-OK", "US-SC", "US-TN", "US-TX", "US-UT", "US-VA")
	lat = 33.5


	print(year)
	l[i] = percentile(start, end)
pprint(l)
l = [x for x in l if x is not None]
a = pd.DataFrame(l)
print(a)
a.to_excel('output.xlsx', header=False, index=False)
	
	




