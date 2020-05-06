import os, sys
from os.path import dirname, join, abspath
sys.path.append(abspath(join(dirname(__file__), '../lib')))

from csvtosql import CSVtoSQL as CtoS
import pandas as pd
from sqlalchemy import create_engine

######### Opening File and Creating sqlite engine #########

#file1 = open(abspath(join(dirname(__file__), "./china_082019_1_tweets_csv_hashed.csv")),'r', encoding='utf-8', errors='ignore')
file2 = open(abspath(join(dirname(__file__), "./china_082019_2_tweets_csv_hashed.csv")),'r', encoding='utf-8',
                 errors='ignore')
file3 = open(abspath(join(dirname(__file__), "./china_082019_3_tweets_csv_hashed_part1.csv")),'r', encoding='utf-8',
                 errors='ignore')
file4 = open(abspath(join(dirname(__file__), "./china_082019_3_tweets_csv_hashed_part2.csv")),'r', encoding='utf-8',
                 errors='ignore')
file5 = open(abspath(join(dirname(__file__), "./china_082019_3_tweets_csv_hashed_part3.csv")),'r', encoding='utf-8',
                 errors='ignore')
disk_engine = create_engine('sqlite:///chinadatalocal.db')

######### Initialize Class #########
cs = CtoS()

#cs.makeFileIntoSQL(file1, 'tweets1', disk_engine)
#tweets1 = pd.read_sql_query('SELECT * FROM tweets1', disk_engine)

cs.makeFileIntoSQL(file2, 'tweets1', disk_engine)
#tweets2 = pd.read_sql_query('SELECT * FROM tweets2', disk_engine)

cs.makeFileIntoSQL(file3, 'tweets1', disk_engine)
#tweets3p1 = pd.read_sql_query('SELECT * FROM tweets3p1', disk_engine)

cs.makeFileIntoSQL(file4, 'tweets1', disk_engine)
#tweets3p2 = pd.read_sql_query('SELECT * FROM tweets3p2', disk_engine)

cs.makeFileIntoSQL(file5, 'tweets1', disk_engine)
#tweets3p3 = pd.read_sql_query('SELECT * FROM tweets3p3', disk_engine)

