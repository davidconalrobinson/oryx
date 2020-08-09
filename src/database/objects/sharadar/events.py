"""
Events class.
"""


# Imports.
from sqlalchemy import Column, Date, String
from src.database.base import Base, create_schema, create_functions, create_triggers


# Set schema and table names.
SCHEMA='sharadar'
TABLENAME='events'


class Events(Base):
	__table_args__={'schema' : SCHEMA}
	__tablename__=TABLENAME
	ticker=Column(String, primary_key=True)
	date=Column(Date, primary_key=True)
	eventcodes=Column(String)


	create_schema(Base, SCHEMA)
	create_functions(
		Base, 
		schema=SCHEMA, 
		tablename=TABLENAME, 
		set_null_strings_to_empty=True,
		string_columns=['ticker', 'eventcodes'])
	create_triggers(
		Base, 
		schema=SCHEMA, 
		tablename=TABLENAME, 
		set_null_strings_to_empty=True)
