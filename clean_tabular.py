from numpy import product
from sqlalchemy import create_engine
import pandas as pd

DATABASE_TYPE = 'postgresql'
DBAPI = 'psycopg2'
HOST = 'products.c8k7he1p0ynz.us-east-1.rds.amazonaws.com' # Change it for your AWS endpoint
USER = 'postgres'
PASSWORD = 'aicore2022!'
PORT = 5432
DATABASE = 'postgres'

engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

engine.execute('''SELECT * FROM products
WHERE NOT category='N/A' ''').fetchall()
products = pd.read_sql_table('products', engine)
print(products.head(10))