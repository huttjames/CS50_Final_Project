import os, sys
from os.path import dirname, join, abspath
sys.path.append(abspath(join(dirname(__file__), '../lib')))

from csvtosql import CSVtoSQL as CtoS
import pandas as pd
from sqlalchemy import create_engine

######### Opening File and Creating sqlite engine #########

file1 = open(abspath(join(dirname(__file__), "./china_082019_1_users_csv_hashed.csv")),'r', encoding='utf-8',
                 errors='ignore')
file2 = open(abspath(join(dirname(__file__), "./china_082019_2_users_csv_hashed.csv")),'r', encoding='utf-8',
                 errors='ignore')
file3 = open(abspath(join(dirname(__file__), "./china_082019_3_users_csv_hashed.csv")),'r', encoding='utf-8',
                 errors='ignore')
disk_engine = create_engine('sqlite:///chinadatalocal.db')

######### Initialize Class #########
cs = CtoS()

cs.makeFileIntoSQL(file1, 'users', disk_engine)


cs.makeFileIntoSQL(file2, 'users', disk_engine)


cs.makeFileIntoSQL(file3, 'users', disk_engine)


