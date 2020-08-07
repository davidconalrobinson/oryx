"""
Create database.
"""


# Imports.
from src.database.base import engine, Base
from src.database.objects.sharadar.actions import Actions
from src.database.objects.sharadar.daily import Daily
from src.database.objects.sharadar.events import Events
from src.database.objects.sharadar.indicators import Indicators
from src.database.objects.sharadar.sep import Sep
from src.database.objects.sharadar.sf1 import Sf1
from src.database.objects.sharadar.sf2 import Sf2
from src.database.objects.sharadar.sf3 import Sf3
from src.database.objects.sharadar.sf3a import Sf3a
from src.database.objects.sharadar.sf3b import Sf3b
from src.database.objects.sharadar.sfp import Sfp
from src.database.objects.sharadar.sp500 import Sp500
from src.database.objects.sharadar.tickers import Tickers


if __name__ == '__main__':
	Base.metadata.create_all(engine)
