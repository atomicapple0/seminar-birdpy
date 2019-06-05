import pandas as pd
from sqlalchemy import create_engine
from pprint import pprint
import os
os.chdir('C:/users/brian/desktop/birdpy')
disk_engine = create_engine('sqlite:///final_BOTH_FULL.db')
disk_engine = create_engine('sqlite:///final_BOTH_60.db')
df = pd.read_sql_query('SELECT * FROM data', disk_engine)

rural = df[df['1']==0]
urban = df[df['1']==1]
bigd = [rural,urban]

for i in range(2000,2019):
	print(str(i) + ': ' + str(rural[rural['2']==i]['0'].median()))

for i in range(2000,2019):
	print(str(i) + ': ' + str(len(df[df['2']==i])))