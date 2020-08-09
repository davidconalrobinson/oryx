"""
Daily class.
"""


# Imports.
from sqlalchemy import Column, Date, String, Numeric
from src.database.base import Base, create_schema, create_functions, create_triggers


# Set schema and table names.
SCHEMA='sharadar'
TABLENAME='daily'


class Daily(Base):
	__table_args__={'schema' : SCHEMA}
	__tablename__=TABLENAME
	ticker=Column(String, primary_key=True)
	date=Column(Date, primary_key=True)
	lastupdated=Column(Date)
	ev=Column(Numeric)
	evebit=Column(Numeric)
	evebitda=Column(Numeric)
	marketcap=Column(Numeric)
	pb=Column(Numeric)
	pe=Column(Numeric)
	ps=Column(Numeric)


	create_schema(Base, SCHEMA)
	create_functions(
		Base, 
		schema=SCHEMA, 
		tablename=TABLENAME, 
		set_null_strings_to_empty=True,
		string_columns=['ticker'])
	create_triggers(
		Base, 
		schema=SCHEMA, 
		tablename=TABLENAME, 
		set_null_strings_to_empty=True)
