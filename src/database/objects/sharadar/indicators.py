"""
Indicators class.
"""


# Imports.
from sqlalchemy import Column, String
from src.database.base import Base, create_schema, create_functions, create_triggers


# Set schema and table names.
SCHEMA='sharadar'
TABLENAME='indicators'


class Indicators(Base):
	__table_args__={'schema' : SCHEMA}
	__tablename__=TABLENAME
	table=Column(String, primary_key=True)
	indicator=Column(String, primary_key=True)
	isfilter=Column(String, primary_key=True)
	isprimarykey=Column(String, primary_key=True)
	title=Column(String)
	description=Column(String)
	unittype=Column(String)


	create_schema(Base, SCHEMA)
	create_functions(
		Base, 
		schema=SCHEMA, 
		tablename=TABLENAME, 
		set_null_strings_to_empty=True,
		string_columns=[
			'table',
			'indicator',
			'isfilter',
			'isprimarykey',
			'title',
			'description',
			'unittype'])
	create_triggers(
		Base, 
		schema=SCHEMA, 
		tablename=TABLENAME, 
		set_null_strings_to_empty=True)
