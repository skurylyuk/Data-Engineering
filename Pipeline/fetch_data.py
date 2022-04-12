import pandas as pd
from sodapy import Socrata
from sqlalchemy import create_engine, inspect
import sqlite3

def get_data():
# # Import SQL File
	engine = create_engine("sqlite:///inspections.db", echo=False)

	# connect to the sql database
	conn = sqlite3.connect('inspections.db')

	# create the ability to perform logic on the database
	c = conn.cursor()

	# create the table in the database
	c.execute('CREATE TABLE IF NOT EXISTS food_inspections '          '(inspection_id TEXT, dba_name TEXT, aka_name TEXT, license_ TEXT, facility_type TEXT, risk TEXT, address TEXT, '          'city TEXT, state TEXT, zip TEXT, inspection_date TEXT, inspection_type TEXT, results TEXT, violations TEXT, '          'R1_1 TEXT, R1_2 TEXT, R1_3 TEXT, R2_1 TEXT, R2_2 TEXT, R2_3 TEXT, RS_1 TEXT, RS_2 TEXT, RS_3 TEXT, '          'latitude TEXT, longituide TEXT, locations TEXT, '          'PRIMARY KEY (inspection_id))')
	# commit the stock table
	conn.commit()

	# print table name
	print(inspect(engine).get_table_names())


	df_new= pd.read_sql('SELECT* FROM food_inspections', engine)
	
	return df_new
