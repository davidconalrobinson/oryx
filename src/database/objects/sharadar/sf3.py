"""
Sf3 class.
"""


# Imports.
from sqlalchemy import Column, Date, String, Numeric, BigInteger
from src.database.base import Base, create_schema


# Set schema and table names.
SCHEMA='sharadar'
TABLENAME='sf3'


class Sf3(Base):
	__table_args__={'schema' : SCHEMA}
	__tablename__=TABLENAME
	index=Column(BigInteger, primary_key=True)
	ticker=Column(String)
	investorname=Column(String)
	securitytype=Column(String)
	calendardate=Column(Date)
	value=Column(Numeric)
	units=Column(Numeric)
	price=Column(Numeric)


	create_schema(Base, SCHEMA)
