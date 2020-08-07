"""
Sf2 class.
"""


# Imports.
from sqlalchemy import Column, Date, String, Numeric, BigInteger
from src.database.base import Base, create_schema


# Set schema and table names.
SCHEMA='sharadar'
TABLENAME='sf2'


class Sf2(Base):
	__table_args__={'schema' : SCHEMA}
	__tablename__=TABLENAME
	index=Column(BigInteger, primary_key=True)
	ticker=Column(String)
	filingdate=Column(Date)
	formtype=Column(String)
	issuername=Column(String)
	ownername=Column(String)
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
	rownum=Column(Numeric)


	create_schema(Base, SCHEMA)
