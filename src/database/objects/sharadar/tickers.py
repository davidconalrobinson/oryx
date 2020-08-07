"""
Tickers class.
"""


# Imports.
from sqlalchemy import Column, Date, String, Numeric, BigInteger
from src.database.base import Base, create_schema


# Set schema and table names.
SCHEMA='sharadar'
TABLENAME='tickers'


class Tickers(Base):
	__table_args__={'schema' : SCHEMA}
	__tablename__=TABLENAME
	index=Column(BigInteger, primary_key=True)
	table=Column(String)
	permaticker=Column(Numeric)
	ticker=Column(String)
	name=Column(String)
	exchange=Column(String)
	isdelisted=Column(String)
	category=Column(String)
	cusips=Column(String)
	siccode=Column(Numeric)
	sicsector=Column(String)
	sicindustry=Column(String)
	famasector=Column(String)
	famaindustry=Column(String)
	sector=Column(String)
	industry=Column(String)
	scalemarketcap=Column(String)
	scalerevenue=Column(String)
	relatedtickers=Column(String)
	currency=Column(String)
	location=Column(String)
	lastupdated=Column(Date)
	firstadded=Column(Date)
	firstpricedate=Column(Date)
	lastpricedate=Column(Date)
	firstquarter=Column(String)
	lastquarter=Column(String)
	secfilings=Column(String)
	companysite=Column(String)


	create_schema(Base, SCHEMA)
