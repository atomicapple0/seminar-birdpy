import pandas as pd
from sqlalchemy import create_engine
import datetime as dt
from math import floor
from pprint import pprint
from statistics import mean

def percentileSubset(df, p):

	totCount = df['count'].sum()

	percentileCount = floor(totCount * p)
	index = -1

	for rowIndex in range(len(df)):

		percentileCount = percentileCount - df.iloc[rowIndex]['count']

		if(percentileCount <= 0):
			# l.append(str(df.iloc[rowIndex]['date']))
			# print(str(p) + ": " + str(df.iloc[rowIndex]['date']))
			percentileRowIndex = rowIndex
			break

	df_new = df.copy()
	df_new.at[percentileRowIndex, 'count'] = abs(percentileCount)

	print(percentileRowIndex)
	df_new = df_new[percentileRowIndex:len(df)]


	return df_new, df.loc[percentileRowIndex]['date']


inputFiles = ['d03_robin_rural.db', 'd03_robin_urban.db']
dfSubsets = []

for inputFile in inputFiles:
	disk_engine = create_engine('sqlite:///' + inputFile)
	df = pd.read_sql_query('SELECT * FROM data ORDER BY `date`', disk_engine)

	df['date'] = pd.to_datetime(df['date'])
	df['date'] = df['date'].dt.dayofyear
	df = df.sort_values('date')

	aggregation_functions = {'date': 'first', 'count': 'sum', 'urban': 'first'}
	df = df.groupby(df['date']).aggregate(aggregation_functions)

	df = df.reset_index(drop=True)

	tempList = []
	for p in [.5,.9,.95]:
		df_new, date = percentileSubset(df,p)
		tempList.append(df_new)

		# print(date)
		# print(df_new)
	dfSubsets.append(tempList)


def rankdata(rural, urban):
	df = pd.concat([rural, urban])
	aggregation_functions = {'date': 'first', 'count': 'sum', 'urban': 'first'}
	df = df.groupby(df['date']).aggregate(aggregation_functions)

	ranks = {}
	rank = 1

	for i,row in df.iterrows():
		ranks[row['date']] = mean(range(rank, int(rank + row['count'])))
		rank = int(rank + row['count'])
	print('ranks')
	print(ranks)
	return ranks

def tiecorrection(rural, urban):
	df = pd.concat([rural, urban])
	aggregation_functions = {'date': 'first', 'count': 'sum', 'urban': 'first'}
	df = df.groupby(df['date']).aggregate(aggregation_functions)

	n = df['count'].sum()



	sum = 0
	for i,row in df.iterrows():
		t = row['count']  ** 3 - row['count']
		sum = sum + t

	d = 1 - ( sum / ((n ** 3) - n) )
	print('d value is ' + str(d))
	return d



def kruskal(rural, urban):
	ranks = rankdata(rural,urban)

	df = pd.concat([rural, urban])
	aggregation_functions = {'date': 'first', 'count': 'sum', 'urban': 'first'}
	df = df.groupby(df['date']).aggregate(aggregation_functions)
	n = df['count'].sum()
	print(n)

	sumtot = 0
	for df_temp in [rural, urban]:
		ni = df_temp['count'].sum()
		print('ni' + str(ni))
		sumrn = 0
		for i,row in df_temp.iterrows():
			print('biiiiiigg')
			print(ranks[row['date']])
			print('aaaaa')
			sumrn = sumrn + ranks[row['date']] * row['count']

		print('sum of rnaks  ' + str(sumrn))
		sumtot = sumtot + (sumrn ** 2) / ni
		print('sum of ranks ^2/n  ' + str((sumrn ** 2) / ni))



	print(sumtot)
	print(12 / (n * (n+1)) * sumtot)
	print(3 * (n+1))
	h = (12 / (n * (n+1))) * sumtot - 3 * (n+1)
	d = tiecorrection(rural, urban)
	print('h value is ' + str(h))
	print('h-adj value is ' + str(h/d))
	return h


rural = []
for i,row in dfSubsets[0][0].iterrows():
	temp = [[row['date'],0]]*row['count']
	rural.extend(temp)

urban = []
for i,row in dfSubsets[1][0].iterrows():
	temp = [[row['date'],1]]*row['count']
	urban.extend(temp)
print('aaaaaaaaaaaaaaaaaaaaaaaaaa')	
print(len(urban))
print(len(rural))

urban.extend(rural)
print('aaaaaaaaaaaaaaaaaaaaaaaaaa')	
print(len(urban))

df_temp = pd.DataFrame(urban)
df_temp.to_csv('final.csv')



rural = dfSubsets[0][0]
urban = dfSubsets[1][0]

kruskal(rural,urban)


# df1 = pd.DataFrame({'date' : pd.Series([10,11,15,12,13,15], dtype='float'),\
# 					'count' : pd.Series([5,6,20,21,22,2], dtype='int'),\
# 					'urban' : pd.Series([1,1,1,1,1,1], dtype='int')},\
# 					index = [0,1,2,3,4,5])
# df2 = pd.DataFrame({'date' : pd.Series([10,16,18,16,10,29,40], dtype='float'),\
# 					'count' : pd.Series([8,6,22,5,2,3,5], dtype='int'),\
# 					'urban' : pd.Series([1,1,1,1,1,1,1], dtype='int')},\
# 					index = [0,1,2,3,4,5,6])
# df3 = pd.DataFrame({'date' : pd.Series([13.5,8.9,9.6,13.8,17.4,15.3], dtype='float'),\
# 					'count' : pd.Series([1,1,1,1,1,1], dtype='int'),\
# 					'urban' : pd.Series([1,1,1,1,1,1], dtype='int')},\
# 					index = [0,1,2,3,4,5])


# kruskal(df1, df2)

