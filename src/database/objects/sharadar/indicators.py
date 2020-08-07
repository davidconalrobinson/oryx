"""
Indicators class.
"""


# Imports.
from sqlalchemy import Column, String, BigInteger
from src.database.base import Base, create_schema


# Set schema and table names.
SCHEMA='sharadar'
TABLENAME='indicators'


class Indicators(Base):
	__table_args__={'schema' : SCHEMA}
	__tablename__=TABLENAME
	index=Column(BigInteger, primary_key=True)
	table=Column(String)
	indicator=Column(String)
	isfilter=Column(String)
	isprimarykey=Column(String)
	title=Column(String)
	description=Column(String)
	unittype=Column(String)


	create_schema(Base, SCHEMA)
