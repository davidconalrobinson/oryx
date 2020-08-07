"""
Sp500 class.
"""


# Imports.
from sqlalchemy import Column, Date, String, BigInteger
from src.database.base import Base, create_schema


# Set schema and table names.
SCHEMA='sharadar'
TABLENAME='sp500'


class Sp500(Base):
	__table_args__={'schema' : SCHEMA}
	__tablename__=TABLENAME
	index=Column(BigInteger, primary_key=True)
	date=Column(Date)
	action=Column(String)
	ticker=Column(String)
	name=Column(String)
	contraticker=Column(String)
	contraname=Column(String)
	note=Column(String)


	create_schema(Base, SCHEMA)
