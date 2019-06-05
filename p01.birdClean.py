import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy
import datetime as dt


inputFile = 'd00_robin_ebd.csv'
outputFile = 'd01_robin_clean.db'

colNames = ['GLOBAL UNIQUE IDENTIFIER', 'LAST EDITED DATE', 'TAXONOMIC ORDER',
       'CATEGORY', 'COMMON NAME', 'SCIENTIFIC NAME', 'SUBSPECIES COMMON NAME',
       'SUBSPECIES SCIENTIFIC NAME', 'count',
       'BREEDING BIRD ATLAS CODE', 'BREEDING BIRD ATLAS CATEGORY', 'AGE/SEX',
       'COUNTRY', 'COUNTRY CODE', 'STATE', 'state', 'COUNTY',
       'COUNTY CODE', 'IBA CODE', 'BCR CODE', 'USFWS CODE', 'ATLAS BLOCK',
       'LOCALITY', 'LOCALITY ID', 'LOCALITY TYPE', 'lat', 'long',
       'date', 'TIME OBSERVATIONS STARTED', 'OBSERVER ID',
       'SAMPLING EVENT IDENTIFIER', 'PROTOCOL TYPE', 'PROTOCOL CODE',
       'PROJECT CODE', 'DURATION MINUTES', 'EFFORT DISTANCE KM',
       'EFFORT AREA HA', 'NUMBER OBSERVERS', 'ALL SPECIES REPORTED',
       'GROUP IDENTIFIER', 'HAS MEDIA', 'APPROVED', 'REVIEWED', 'REASON',
       'TRIP COMMENTS', 'SPECIES COMMENTS', 'Unnamed: 46']

pdDtypes = {
        'count': str, 
        'state': str,
        'lat': float,
        'long': float,
        'date': str}

sqlDtypes = {
        'count': sqlalchemy.Integer(), 
        'state':  sqlalchemy.types.String(),
        'lat': sqlalchemy.types.Float(),
        'long': sqlalchemy.types.Float(),
        'date': sqlalchemy.types.DateTime()}


pd.set_option('display.max_columns', None)
start = dt.datetime.now()
chunksize = 20000
j = 0
index_start = 1

disk_engine = create_engine('sqlite:///' + outputFile)
disk_engine.execute('DROP TABLE IF EXISTS data')

for df in pd.read_csv(inputFile, sep='\t', chunksize=chunksize, iterator=True, encoding='utf-8', names=colNames, skiprows=1, dtype= pdDtypes):

    df.index += index_start

    df['date'] = pd.to_datetime(df['date'])

    #df['count'] = df['count'].replace('X', 1)
    df = df.drop(df[df['count'] == 'X'].index)

    df['count'].map(int)

    # Remove the un-interesting columns
    columns = ['count', 'state', 'lat', 'long', 'date']

    for c in df.columns:
        if c not in columns:
            df = df.drop(c, axis=1)    

    j+=1
    print('{} seconds: completed {} rows'.format((dt.datetime.now() - start).seconds, j*chunksize))

    df.to_sql('data', disk_engine, if_exists='append', index=False, dtype=sqlDtypes)

    index_start = df.index[-1] + 1