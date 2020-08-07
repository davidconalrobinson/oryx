"""
Actions class.
"""


# Imports.
from sqlalchemy import Column, Date, String, Numeric, BigInteger
from src.database.base import Base, create_schema


# Set schema and table names.
SCHEMA='sharadar'
TABLENAME='actions'


class Actions(Base):
	__table_args__={'schema' : SCHEMA}
	__tablename__=TABLENAME
	index=Column(BigInteger, primary_key=True)
	date=Column(Date)
	action=Column(String)
	ticker=Column(String)
	name=Column(String)
	value=Column(Numeric)
	contraticker=Column(String)
	contraname=Column(String)


	create_schema(Base, SCHEMA)
