"""
Sf1 class.
"""


# Imports.
from sqlalchemy import Column, Date, String, Numeric
from src.database.base import Base, create_schema, create_functions, create_triggers


# Set schema and table names.
SCHEMA='sharadar'
TABLENAME='sf1'


class Sf1(Base):
	__table_args__={'schema' : SCHEMA}
	__tablename__=TABLENAME
	ticker=Column(String, primary_key=True)
	dimension=Column(String, primary_key=True)
	calendardate=Column(Date)
	datekey=Column(Date, primary_key=True)
	reportperiod=Column(Date, primary_key=True)
	lastupdated=Column(Date)
	accoci=Column(Numeric)
	assets=Column(Numeric)
	assetsavg=Column(Numeric)
	assetsc=Column(Numeric)
	assetsnc=Column(Numeric)
	assetturnover=Column(Numeric)
	bvps=Column(Numeric)
	capex=Column(Numeric)
	cashneq=Column(Numeric)
	cashnequsd=Column(Numeric)
	cor=Column(Numeric)
	consolinc=Column(Numeric)
	currentratio=Column(Numeric)
	de=Column(Numeric)
	debt=Column(Numeric)
	debtc=Column(Numeric)
	debtnc=Column(Numeric)
	debtusd=Column(Numeric)
	deferredrev=Column(Numeric)
	depamor=Column(Numeric)
	deposits=Column(Numeric)
	divyield=Column(Numeric)
	dps=Column(Numeric)
	ebit=Column(Numeric)
	ebitda=Column(Numeric)
	ebitdamargin=Column(Numeric)
	ebitdausd=Column(Numeric)
	ebitusd=Column(Numeric)
	ebt=Column(Numeric)
	eps=Column(Numeric)
	epsdil=Column(Numeric)
	epsusd=Column(Numeric)
	equity=Column(Numeric)
	equityavg=Column(Numeric)
	equityusd=Column(Numeric)
	ev=Column(Numeric)
	evebit=Column(Numeric)
	evebitda=Column(Numeric)
	fcf=Column(Numeric)
	fcfps=Column(Numeric)
	fxusd=Column(Numeric)
	gp=Column(Numeric)
	grossmargin=Column(Numeric)
	intangibles=Column(Numeric)
	intexp=Column(Numeric)
	invcap=Column(Numeric)
	invcapavg=Column(Numeric)
	inventory=Column(Numeric)
	investments=Column(Numeric)
	investmentsc=Column(Numeric)
	investmentsnc=Column(Numeric)
	liabilities=Column(Numeric)
	liabilitiesc=Column(Numeric)
	liabilitiesnc=Column(Numeric)
	marketcap=Column(Numeric)
	ncf=Column(Numeric)
	ncfbus=Column(Numeric)
	ncfcommon=Column(Numeric)
	ncfdebt=Column(Numeric)
	ncfdiv=Column(Numeric)
	ncff=Column(Numeric)
	ncfi=Column(Numeric)
	ncfinv=Column(Numeric)
	ncfo=Column(Numeric)
	ncfx=Column(Numeric)
	netinc=Column(Numeric)
	netinccmn=Column(Numeric)
	netinccmnusd=Column(Numeric)
	netincdis=Column(Numeric)
	netincnci=Column(Numeric)
	netmargin=Column(Numeric)
	opex=Column(Numeric)
	opinc=Column(Numeric)
	payables=Column(Numeric)
	payoutratio=Column(Numeric)
	pb=Column(Numeric)
	pe=Column(Numeric)
	pe1=Column(Numeric)
	ppnenet=Column(Numeric)
	prefdivis=Column(Numeric)
	price=Column(Numeric)
	ps=Column(Numeric)
	ps1=Column(Numeric)
	receivables=Column(Numeric)
	retearn=Column(Numeric)
	revenue=Column(Numeric)
	revenueusd=Column(Numeric)
	rnd=Column(Numeric)
	roa=Column(Numeric)
	roe=Column(Numeric)
	roic=Column(Numeric)
	ros=Column(Numeric)
	sbcomp=Column(Numeric)
	sgna=Column(Numeric)
	sharefactor=Column(Numeric)
	sharesbas=Column(Numeric)
	shareswa=Column(Numeric)
	shareswadil=Column(Numeric)
	sps=Column(Numeric)
	tangibles=Column(Numeric)
	taxassets=Column(Numeric)
	taxexp=Column(Numeric)
	taxliabilities=Column(Numeric)
	tbvps=Column(Numeric)
	workingcapital=Column(Numeric)


	create_schema(Base, SCHEMA)
	create_functions(
		Base, 
		schema=SCHEMA, 
		tablename=TABLENAME, 
		set_null_strings_to_empty=True,
		string_columns=['ticker', 'dimension'])
	create_triggers(
		Base, 
		schema=SCHEMA, 
		tablename=TABLENAME, 
		set_null_strings_to_empty=True)
