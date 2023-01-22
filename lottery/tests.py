from sqlalchemy import create_engine
import psycopg2 
import io
import pandas as pd
from pangres import upsert


engine = create_engine(
    'postgresql+psycopg2://linpostgres:^ycZUaSzWOrsK37E@lin-15054-4726-pgsql-primary.servers.linodedb.net:5432/postgres')


df = pd.read_csv('C:/Users/C.K.ABOAGYE/OneDrive/Documents/Desktop/startups-external/lottery-mis/mis/lottery/test.csv')
# Drop old table and create new empty table
df.head(0).to_sql('mobile_number_directory', engine, if_exists='append',index=False)

conn = engine.raw_connection()
cur = conn.cursor()
output = io.StringIO()
df.to_csv(output, sep='\t', header=False, index=False)
output.seek(0)
contents = output.getvalue()
cur.copy_from(output, 'mobile_number_directory', null="") # null values become ''
conn.commit()
cur.close()
conn.close()