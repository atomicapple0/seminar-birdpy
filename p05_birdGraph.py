import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import matplotlib

matplotlib.use('TkAgg')

inputFile = 'robin_filter_03.db'

start = datetime.date(2016, 1, 1)
end = datetime.date(2017, 1, 1)
title = 'test'

inputFile = 'robin_{}_{}_03_filter.db'.format(start.year, end.year)


def bargraph(inputFile, title):

	disk_engine = create_engine('sqlite:///' + inputFile)
	df = pd.read_sql_query('SELECT * FROM data ORDER BY date', disk_engine)

	df['date'] = pd.to_datetime(df['date'])

	aggregation_functions = {'date': 'first', 'count': 'sum'}
	df = df.groupby(df['date']).aggregate(aggregation_functions)


	df.set_index('date',inplace=True)
	plt.style.use('ggplot')

	fig, ax = plt.subplots(figsize=(15,7))
	ax.bar(df.index, df['count'])


	ax.xaxis.set_major_locator(mdates.MonthLocator())
	ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

	ax.set_title(title)
	ax.set_ylabel('Count')
	ax.set_xlabel('Date')

	print('bb')
	plt.show(ax)
	print('a')

for i in [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007 ,2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]:
	start = datetime.date(i, 1, 1)
	end = datetime.date(i+1, 1, 1)
	inputFile = 'robin_{}_{}_03_filter.db'.format(start.year, end.year)
	bargraph(inputFile, i)