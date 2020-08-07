"""
Daily class.
"""


# Imports.
from sqlalchemy import Column, Date, String, Numeric, BigInteger
from src.database.base import Base, create_schema


# Set schema and table names.
SCHEMA='sharadar'
TABLENAME='daily'


class Daily(Base):
	__table_args__={'schema' : SCHEMA}
	__tablename__=TABLENAME
	index=Column(BigInteger, primary_key=True)
	ticker=Column(String)
	date=Column(Date)
	lastupdated=Column(Date)
	ev=Column(Numeric)
	evebit=Column(Numeric)
	evebitda=Column(Numeric)
	marketcap=Column(Numeric)
	pb=Column(Numeric)
	pe=Column(Numeric)
	ps=Column(Numeric)


	create_schema(Base, SCHEMA)
