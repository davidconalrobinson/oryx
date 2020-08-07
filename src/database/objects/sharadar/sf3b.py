"""
Sf3b class.
"""


# Imports.
from sqlalchemy import Column, Date, String, Numeric, BigInteger
from src.database.base import Base, create_schema


# Set schema and table names.
SCHEMA='sharadar'
TABLENAME='sf3b'


class Sf3b(Base):
	__table_args__={'schema' : SCHEMA}
	__tablename__=TABLENAME
	index=Column(BigInteger, primary_key=True)
	calendardate=Column(Date)
	investorname=Column(String)
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
