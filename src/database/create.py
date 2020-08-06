"""
Create database.
"""


# Imports.
from src.database.base import engine, Base
from src.database.objects.sharadar.actions import Actions
from src.database.objects.sharadar.sf1 import Sf1


if __name__ == '__main__':
	Base.metadata.create_all(engine)
