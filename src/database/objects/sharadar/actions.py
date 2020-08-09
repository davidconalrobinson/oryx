"""
Actions class.
"""


# Imports.
from sqlalchemy import Column, Date, String, Numeric
from src.database.base import Base, create_schema, create_functions, create_triggers


# Set schema and table names.
SCHEMA='sharadar'
TABLENAME='actions'


class Actions(Base):
	__table_args__={'schema' : SCHEMA}
	__tablename__=TABLENAME
	date=Column(Date, primary_key=True)
	action=Column(String, primary_key=True)
	ticker=Column(String, primary_key=True)
	name=Column(String)
	value=Column(Numeric)
	contraticker=Column(String, primary_key=True)
	contraname=Column(String)


	create_schema(Base, SCHEMA)
	create_functions(
		Base, 
		schema=SCHEMA, 
		tablename=TABLENAME, 
		set_null_strings_to_empty=True,
		string_columns=['action', 'ticker', 'name', 'contraticker', 'contraname'])
	create_triggers(
		Base, 
		schema=SCHEMA, 
		tablename=TABLENAME, 
		set_null_strings_to_empty=True)
