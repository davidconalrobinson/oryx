"""
Sf3a class.
"""


# Imports.
from sqlalchemy import Column, Date, String, Numeric
from src.database.base import Base, create_schema, create_functions, create_triggers


# Set schema and table names.
SCHEMA='sharadar'
TABLENAME='sf3a'


class Sf3a(Base):
	__table_args__={'schema' : SCHEMA}
	__tablename__=TABLENAME
	calendardate=Column(Date, primary_key=True)
	ticker=Column(String, primary_key=True)
	name=Column(String)
	shrholders=Column(Numeric)
	cllholders=Column(Numeric)
	putholders=Column(Numeric)
	wntholders=Column(Numeric)
	dbtholders=Column(Numeric)
	prfholders=Column(Numeric)
	fndholders=Column(Numeric)
	undholders=Column(Numeric)
	shrunits=Column(Numeric)
	cllunits=Column(Numeric)
	putunits=Column(Numeric)
	wntunits=Column(Numeric)
	dbtunits=Column(Numeric)
	prfunits=Column(Numeric)
	fndunits=Column(Numeric)
	undunits=Column(Numeric)
	shrvalue=Column(Numeric)
	cllvalue=Column(Numeric)
	putvalue=Column(Numeric)
	wntvalue=Column(Numeric)
	dbtvalue=Column(Numeric)
	prfvalue=Column(Numeric)
	fndvalue=Column(Numeric)
	undvalue=Column(Numeric)
	totalvalue=Column(Numeric)
	percentoftotal=Column(Numeric)


	create_schema(Base, SCHEMA)
	create_functions(
		Base, 
		schema=SCHEMA, 
		tablename=TABLENAME, 
		set_null_strings_to_empty=True,
		string_columns=['ticker', 'name'])
	create_triggers(
		Base, 
		schema=SCHEMA, 
		tablename=TABLENAME, 
		set_null_strings_to_empty=True)
