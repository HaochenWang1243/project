import pandas as pd
import os
import argparse
import re
from time import time
from sqlalchemy import create_engine
parser = argparse.ArgumentParser(description='Postgres params')
parser.add_argument('--username',required=True,help='Postgres username')
parser.add_argument('--password', help='Postgres password',required=True)
parser.add_argument('--server', help='Postgres server',required=True)
parser.add_argument('--port', help='Postgres port',required=True)
parser.add_argument('--database', help='Postgres db name',required=True)
parser.add_argument('--src_url', help='',required=True)
parser.add_argument('--table_name',required=True)
filename='data.csv'
args = parser.parse_args()
print(args)

engine=create_engine(f'postgresql://{args.username}:{args.password}@{args.server}:{args.port}/{args.database}')

os.system(f'wget {args.src_url} -O {filename}')
# regex=re.compile('.\parquet') how to get downloaded filename if the file is downloaded with wget?
# if regex.search('')
# df = pd.read_parquet('yellow_tripdata_2023-01.parquet')
# df.to_csv('yellow_tripdata_2023-01.csv')

df_iter=pd.read_csv(filename,iterator=True,chunksize=100000)
df=next(df_iter,None) # df_iter isn't a df - use next() to get the first df
while df is not None:
    start=time()
    df.to_sql(name=args.table_name,con=engine,if_exists='append') 
    end=time()
    print('one chunck ingested, time: %.3f' % (end-start))
    df=next(df_iter,None)