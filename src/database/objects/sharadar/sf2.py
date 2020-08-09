"""
Sf2 class.
"""


# Imports.
from sqlalchemy import Column, Date, String, Numeric
from src.database.base import Base, create_schema, create_functions, create_triggers


# Set schema and table names.
SCHEMA='sharadar'
TABLENAME='sf2'


class Sf2(Base):
	__table_args__={'schema' : SCHEMA}
	__tablename__=TABLENAME
	ticker=Column(String, primary_key=True)
	filingdate=Column(Date, primary_key=True)
	formtype=Column(String, primary_key=True)
	issuername=Column(String)
	ownername=Column(String, primary_key=True)
	officertitle=Column(String)
	isdirector=Column(String)
	isofficer=Column(String)
	istenpercentowner=Column(String)
	transactiondate=Column(Date)
	securityadcode=Column(String)
	transactioncode=Column(String)
	sharesownedbeforetransaction=Column(Numeric)
	transactionshares=Column(Numeric)
	sharesownedfollowingtransaction=Column(Numeric)
	transactionpricepershare=Column(Numeric)
	transactionvalue=Column(Numeric)
	securitytitle=Column(String)
	directorindirect=Column(String)
	natureofownership=Column(String)
	dateexercisable=Column(Date)
	priceexercisable=Column(Numeric)
	expirationdate=Column(Date)
	rownum=Column(Numeric, primary_key=True)


	create_schema(Base, SCHEMA)
	create_functions(
		Base, 
		schema=SCHEMA, 
		tablename=TABLENAME, 
		set_null_strings_to_empty=True,
		string_columns=[
			'ticker',
			'formtype',
			'issuername',
			'ownername',
			'officertitle',
			'isdirector',
			'isofficer',
			'istenpercentowner',
			'securityadcode',
			'transactioncode',
			'securitytitle',
			'directorindirect',
			'natureofownership'])
	create_triggers(
		Base, 
		schema=SCHEMA, 
		tablename=TABLENAME, 
		set_null_strings_to_empty=True)
