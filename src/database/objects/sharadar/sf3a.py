"""
Sf3a class.
"""


# Imports.
from sqlalchemy import Column, Date, String, Numeric, BigInteger
from src.database.base import Base, create_schema


# Set schema and table names.
SCHEMA='sharadar'
TABLENAME='sf3a'


class Sf3a(Base):
	__table_args__={'schema' : SCHEMA}
	__tablename__=TABLENAME
	index=Column(BigInteger, primary_key=True)
	calendardate=Column(Date)
	ticker=Column(String)
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
