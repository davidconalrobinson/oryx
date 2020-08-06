"""
Ingest sharadar data from batch tables to database.
"""


# Imports.
import pandas as pd
from sqlalchemy import event
from src.database.base import engine
from src.helpers.pandas_extensions import DataFrameExt
from src.helpers.psql_insert_copy import psql_insert_copy


# Set path, compression and destination for each table.
table_dict={
	'actions': {
		'path': 'data/sharadar_actions.zip',
		'compression': 'zip',
		'schema': 'sharadar',
		'table': 'actions'
	},
	'sf1': {
		'path': 'data/sharadar_sf1.zip',
		'compression': 'zip',
		'schema': 'sharadar',
		'table': 'sf1'
	}
}


# Loop through dict.
for key, value in table_dict.items():
	# Load table from csv.
	print('Loading table {key} from {path}.'.format(key=key, path=value['path']))
	df=DataFrameExt(
		pd.read_csv(
			value['path'],
			compression=value['compression']))
	print('Table loaded.')
	# Write to db.
	print('Writing table to {schema}.{table}'.format(schema=value['schema'], table=value['table']))
	df.to_sql_tqdm(
		value['table'],
		engine,
		schema=value['schema'],
		if_exists='append',
		index=True,
		index_label='index',
		chunksize=10000,
		method=psql_insert_copy)
