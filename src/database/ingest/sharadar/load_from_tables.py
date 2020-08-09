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
	'daily': {
		'path': 'data/sharadar_daily.zip',
		'compression': 'zip',
		'schema': 'sharadar',
		'table': 'daily'
	},
	'events': {
		'path': 'data/sharadar_events.zip',
		'compression': 'zip',
		'schema': 'sharadar',
		'table': 'events'
	},
	'indicators': {
		'path': 'data/sharadar_indicators.zip',
		'compression': 'zip',
		'schema': 'sharadar',
		'table': 'indicators'
	},
	'sep': {
		'path': 'data/sharadar_sep.zip',
		'compression': 'zip',
		'schema': 'sharadar',
		'table': 'sep'
	},
	'sf1': {
		'path': 'data/sharadar_sf1.zip',
		'compression': 'zip',
		'schema': 'sharadar',
		'table': 'sf1'
	},
	'sf2': {
		'path': 'data/sharadar_sf2.zip',
		'compression': 'zip',
		'schema': 'sharadar',
		'table': 'sf2'
	},
	'sf3': {
		'path': 'data/sharadar_sf3.zip',
		'compression': 'zip',
		'schema': 'sharadar',
		'table': 'sf3'
	},
	'sf3a': {
		'path': 'data/sharadar_sf3a.zip',
		'compression': 'zip',
		'schema': 'sharadar',
		'table': 'sf3a'
	},
	'sf3b': {
		'path': 'data/sharadar_sf3b.zip',
		'compression': 'zip',
		'schema': 'sharadar',
		'table': 'sf3b'
	},
	'sfp': {
		'path': 'data/sharadar_sfp.zip',
		'compression': 'zip',
		'schema': 'sharadar',
		'table': 'sfp'
	},
	'sp500': {
		'path': 'data/sharadar_sp500.zip',
		'compression': 'zip',
		'schema': 'sharadar',
		'table': 'sp500'
	},
	'tickers': {
		'path': 'data/sharadar_tickers.zip',
		'compression': 'zip',
		'schema': 'sharadar',
		'table': 'tickers'
	}
}


# Loop through dict.
for key, value in table_dict.items():
	# Load table from csv.
	print('Loading table {key} from {path}.'.format(key=key, path=value['path']))
	df=DataFrameExt(
		pd.read_csv(
			value['path'],
			compression=value['compression'],
			low_memory=False))
	print('Table loaded.')
	# Write to db.
	print('Writing table to {schema}.{table}'.format(schema=value['schema'], table=value['table']))
	df.to_sql_tqdm(
		value['table'],
		engine,
		schema=value['schema'],
		if_exists='append',
		index=False,
		chunksize=10000,
		method=psql_insert_copy)
