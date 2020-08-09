"""
Sf3b class.
"""


# Imports.
from sqlalchemy import Column, Date, String, Numeric
from src.database.base import Base, create_schema, create_functions, create_triggers


# Set schema and table names.
SCHEMA='sharadar'
TABLENAME='sf3b'


class Sf3b(Base):
	__table_args__={'schema' : SCHEMA}
	__tablename__=TABLENAME
	calendardate=Column(Date, primary_key=True)
	investorname=Column(String, primary_key=True)
	shrholdings=Column(Numeric)
	cllholdings=Column(Numeric)
	putholdings=Column(Numeric)
	wntholdings=Column(Numeric)
	dbtholdings=Column(Numeric)
	prfholdings=Column(Numeric)
	fndholdings=Column(Numeric)
	undholdings=Column(Numeric)
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
		string_columns=['investorname'])
	create_triggers(
		Base, 
		schema=SCHEMA, 
		tablename=TABLENAME, 
		set_null_strings_to_empty=True)
