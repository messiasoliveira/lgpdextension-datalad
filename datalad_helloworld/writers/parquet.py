import pandas as pd
import logging

lgr = logging.getLogger('datalad.helloworld.hello_cmd.writers.parquet')

class Parquet:
    def __init__(self,settings):
        self.settings = settings

    def read(self):
        lgr.info("Reading parquet file",self.settings)
        return pd.read_parquet(self.settings.path)

    def write(self):
        lgr.info("Writing parquet file",self.settings)
        return pd.DataFrame.to_parquet(self.settings.path)