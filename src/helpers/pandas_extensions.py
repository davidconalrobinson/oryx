"""
Pandas extensions.
"""


# Imports.
import pandas as pd
from tqdm import tqdm


class DataFrameExt(pd.DataFrame):


	def __init__(self, *args, **kwargs):
		pd.DataFrame.__init__(self, *args, **kwargs)


	def to_sql_tqdm(self, name, con, chunksize, **kwargs):
		"""
		Pandas to_sql method with tqdm.
		"""
		for i in tqdm(range(0, len(self), chunksize)):
			self.iloc[i:i+chunksize].to_sql(name, con, **kwargs)
