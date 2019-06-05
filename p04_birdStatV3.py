import pandas as pd
from sqlalchemy import create_engine
import datetime as dt
from math import floor
from pprint import pprint
import sqlalchemy

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
dateSubsets = []

for inputFile in inputFiles:
	disk_engine = create_engine('sqlite:///' + inputFile)
	df = pd.read_sql_query('SELECT * FROM data ORDER BY `date`', disk_engine)

	print('aaaaadasdda')
	print(df['count'].sum())

	df['date'] = pd.to_datetime(df['date'])
	df['year'] = df['date'].dt.year
	df['date'] = df['date'].dt.dayofyear
	df = df.sort_values('date')

	# aggregation_functions = {'date': 'first', 'count': 'sum', 'urban': 'first'}
	# df = df.groupby(df['date']).aggregate(aggregation_functions)

	df = df.reset_index(drop=True)

	tempList = []
	tempListDates = []
	for p in [0,.6]:
		df_new, date = percentileSubset(df,p)
		tempList.append(df_new)
		tempListDates.append(date)

		# print(date)
		# print(df_new)
	dfSubsets.append(tempList)
	dateSubsets.append(tempListDates)

pprint(dateSubsets)

# for i in range(2):
# 	for j in range(len(dfSubsets[i])):
# 		print('b' + str(i))
# 		print(j)
# 		print(len(dfSubsets[i][j]))
# 		if i == 0:
# 			output = []
# 			for index,row in dfSubsets[i][j].iterrows():
# 				print('c')
# 				temp = [[row['date'],0,row['year']]]*row['count']
# 				output.extend(temp)
# 			df_temp = pd.DataFrame(output)
# 			df_temp.to_csv('final_rural_' + str(j) + '.csv')
# 		elif i == 1:
# 			output = []
# 			for index,row in dfSubsets[i][j].iterrows():
# 				temp = [[row['date'],1,row['year']]]*row['count']
# 				output.extend(temp)
# 			df_temp = pd.DataFrame(output)
# 			df_temp.to_csv('final_urban_' + str(j) + '.csv')

# 		print('a' + str(i))
# 		print(j)


for j in range(len(dfSubsets[0])):
	print(j)

	i = 0
	rural = []
	for index,row in dfSubsets[i][j].iterrows():
		print('c')
		temp = [[row['date'],0,row['year']]]*row['count']
		rural.extend(temp)

	i = 1
	urban = []
	for index,row in dfSubsets[i][j].iterrows():
		temp = [[row['date'],1,row['year']]]*row['count']
		urban.extend(temp)

	print(rural[1])

	rural.extend(urban)

	print(len(rural))
	df_temp = pd.DataFrame(rural)
	df_temp = df_temp.rename(columns={'0': 'date', '1': 'urban', '2': 'year'})

	disk_engine_temp = create_engine('sqlite:///' + 'final_BOTH_' + str(j) + '.db')
	disk_engine_temp.execute('DROP TABLE IF EXISTS data')
	sqlDtypes = {
        'date': sqlalchemy.Integer(), 
        'year':  sqlalchemy.types.Integer(),
        'urban': sqlalchemy.types.Integer()}
	df_temp.to_sql('data', disk_engine_temp, if_exists='append', index=False, dtype=sqlDtypes)


	df_temp.to_csv('final_BOTH_' + str(j) + '.csv',index=False)

	print('a' + str(i))
	print(j)


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

