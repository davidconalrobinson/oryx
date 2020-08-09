"""
Sf3 class.
"""


# Imports.
from sqlalchemy import Column, Date, String, Numeric
from src.database.base import Base, create_schema, create_functions, create_triggers


# Set schema and table names.
SCHEMA='sharadar'
TABLENAME='sf3'


class Sf3(Base):
	__table_args__={'schema' : SCHEMA}
	__tablename__=TABLENAME
	ticker=Column(String, primary_key=True)
	investorname=Column(String, primary_key=True)
	securitytype=Column(String, primary_key=True)
	calendardate=Column(Date, primary_key=True)
	value=Column(Numeric)
	units=Column(Numeric)
	price=Column(Numeric)


	create_schema(Base, SCHEMA)
	create_functions(
		Base, 
		schema=SCHEMA, 
		tablename=TABLENAME, 
		set_null_strings_to_empty=True,
		string_columns=['ticker', 'investorname', 'securitytype'])
	create_triggers(
		Base, 
		schema=SCHEMA, 
		tablename=TABLENAME, 
		set_null_strings_to_empty=True)
