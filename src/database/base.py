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


def create_functions(Base, functions=[], schema=None, tablename=None, string_columns=[], set_created_utc=False, set_updated_utc=False, set_null_strings_to_empty=False):
	"""
	Create functions after creating database.
	"""
	def after_create(target, connection, **kwargs):
		sql=functions
		if set_created_utc:
			# Create function for setting created_utc fied.
			sql+=["""
				CREATE OR REPLACE FUNCTION {schema}.set_created_utc()
				RETURNS TRIGGER AS
				$$
					BEGIN
						NEW.created_utc=current_timestamp;
						RETURN NEW;
					END;
				$$
				LANGUAGE PLPGSQL;
			""".format(schema=schema)]
		if set_updated_utc:
			# Create function for setting updated_utc fied.
			sql+=["""
				CREATE OR REPLACE FUNCTION {schema}.set_updated_utc()
				RETURNS TRIGGER AS
				$$
					BEGIN
						NEW.updated_utc=current_timestamp;
						RETURN NEW;
					END;
				$$
				LANGUAGE PLPGSQL;
			""".format(schema=schema)]
		if set_null_strings_to_empty:
			# Create function for setting null string to empty.
			sql+=["""
				CREATE OR REPLACE FUNCTION {schema}.\"{tablename}.set_null_strings_to_empty\"()
				RETURNS TRIGGER AS
				$$
					BEGIN
						{conversion}
						RETURN NEW;
					END;
				$$
				LANGUAGE PLPGSQL;
			""".format(
					schema=schema,
					tablename=tablename,
					conversion='\n\t\t\t\t\t\t'.join(['NEW.'+col+' = COALESCE(NEW.'+col+', \'\');' for col in string_columns]))]
		if sql:
			connection.execute(text(''.join(set(sql))))
	event.listen(Base.metadata, 'after_create', after_create)


def create_triggers(Base, triggers=[], schema=None, tablename=None, set_created_utc=False, set_updated_utc=False, set_null_strings_to_empty=False):
	"""
	Create triggers after creating database.
	"""
	def after_create(target, connection, **kwargs):
		sql=triggers
		if set_created_utc:
			# Create trigger for setting created_utc fied.
			sql+=["""
				DROP TRIGGER IF EXISTS set_created_utc ON {schema}."{tablename}";
				CREATE TRIGGER set_created_utc
				BEFORE INSERT ON {schema}."{tablename}"
				FOR EACH ROW EXECUTE PROCEDURE {schema}.set_created_utc();
			""".format(schema=schema, tablename=tablename)]
		if set_updated_utc:
			# Create trigger for setting updated_utc fied.
			sql+=["""
				DROP TRIGGER IF EXISTS set_updated_utc ON {schema}."{tablename}";
				CREATE TRIGGER set_updated_utc
				BEFORE INSERT ON {schema}."{tablename}"
				FOR EACH ROW EXECUTE PROCEDURE {schema}.set_updated_utc();
			""".format(schema=schema, tablename=tablename)]
		if set_null_strings_to_empty:
			# Create trigger for setting null string to empty.
			sql+=["""
				DROP TRIGGER IF EXISTS set_null_strings_to_empty ON {schema}."{tablename}";
				CREATE TRIGGER set_null_strings_to_empty
				BEFORE INSERT ON {schema}."{tablename}"
				FOR EACH ROW EXECUTE PROCEDURE {schema}.\"{tablename}.set_null_strings_to_empty\"();
			""".format(schema=schema, tablename=tablename)]
		if sql:
			connection.execute(text(''.join(set(sql))))
	event.listen(Base.metadata, 'after_create', after_create)
