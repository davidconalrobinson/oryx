"""
Events class.
"""


# Imports.
from sqlalchemy import Column, Date, String, BigInteger
from src.database.base import Base, create_schema


# Set schema and table names.
SCHEMA='sharadar'
TABLENAME='events'


class Events(Base):
	__table_args__={'schema' : SCHEMA}
	__tablename__=TABLENAME
	index=Column(BigInteger, primary_key=True)
	ticker=Column(String)
	date=Column(Date)
	eventcodes=Column(String)


	create_schema(Base, SCHEMA)
