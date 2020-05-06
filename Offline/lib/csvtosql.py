import pandas as pd
import csv
from sqlalchemy import create_engine # database connection

############################################
# uncomment this below if you want to see the output the of data in a table
# from IPython.display import display
# display(pd.read_csv('file1.csv'))
############################################

class CSVtoSQL:
        def __init__(self):
                pass

        def makeFileIntoSQL(self, filename, sqlName, sqlEngine):
                chunksize = 20000
                j = 0
                index_start = 1
                for df in pd.read_csv(filename, chunksize=chunksize, iterator=True, engine='python', quotechar='"', quoting=csv.QUOTE_MINIMAL,error_bad_lines=False, doublequote = True, skipinitialspace=True, skip_blank_lines=True, encoding='utf-8'):
                        df = df.rename(columns={c: c.replace(' ', '') for c in df.columns}) # Remove spaces from columns
                        df.to_sql(sqlName, sqlEngine, if_exists='append') ##change to if_exists='replace' if you don't want to replace the database file


