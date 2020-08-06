"""
Create SQL Alchemy engine, session and base class.
"""


# Imports.
from sqlalchemy import create_engine, event
from sqlalchemy.sql import text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Create session.
engine=create_engine('postgresql://postgres:postgres@localhost:5432/oryx')
Session=sessionmaker(bind=engine)


# Create base class.
Base=declarative_base()


def create_schema(Base, schema):
	"""
	Create schema before creating database.
	"""
	def before_create(target, connection, **kwargs):
		sql=text('CREATE SCHEMA IF NOT EXISTS {schema};'.format(schema=schema))
		connection.execute(sql)
	event.listen(Base.metadata, 'before_create', before_create)
