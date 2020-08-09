"""
Tickers class.
"""


# Imports.
from sqlalchemy import Column, Date, String, Numeric
from src.database.base import Base, create_schema, create_functions, create_triggers


# Set schema and table names.
SCHEMA='sharadar'
TABLENAME='tickers'


class Tickers(Base):
	__table_args__={'schema' : SCHEMA}
	__tablename__=TABLENAME
	table=Column(String, primary_key=True)
	permaticker=Column(Numeric, primary_key=True)
	ticker=Column(String, primary_key=True)
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
	create_functions(
		Base, 
		schema=SCHEMA, 
		tablename=TABLENAME, 
		set_null_strings_to_empty=True,
		string_columns=[
			'table',
			'ticker',
			'name',
			'exchange',
			'isdelisted',
			'category',
			'cusips',
			'sicsector',
			'sicindustry',
			'famasector',
			'famaindustry',
			'sector',
			'industry',
			'scalemarketcap',
			'scalerevenue',
			'relatedtickers',
			'currency',
			'location',
			'firstquarter',
			'lastquarter',
			'secfilings',
			'companysite'])
	create_triggers(
		Base, 
		schema=SCHEMA, 
		tablename=TABLENAME, 
		set_null_strings_to_empty=True)
