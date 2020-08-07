"""
Sep class.
"""


# Imports.
from sqlalchemy import Column, Date, String, Numeric, BigInteger
from src.database.base import Base, create_schema


# Set schema and table names.
SCHEMA='sharadar'
TABLENAME='sep'


class Sep(Base):
	__table_args__={'schema' : SCHEMA}
	__tablename__=TABLENAME
	index=Column(BigInteger, primary_key=True)
	ticker=Column(String)
	date=Column(Date)
	open=Column(Numeric)
	high=Column(Numeric)
	low=Column(Numeric)
	close=Column(Numeric)
	volume=Column(Numeric)
	dividends=Column(Numeric)
	closeunadj=Column(Numeric)
	lastupdated=Column(Date)


	create_schema(Base, SCHEMA)
