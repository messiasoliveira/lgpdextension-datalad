import pandas as pd
import logging

from sqlalchemy import column

lgr = logging.getLogger('datalad.helloworld.hello_cmd.writers.parquet')

class Parquet:
    def __init__(self,settings):
        self.settings = settings

    def read(self):
        lgr.info("Reading parquet file",self.settings)
        if self.settings.get("names",[]) != []:
            return pd.read_parquet(path=self.settings.path,columns=self.settings.names)
        return pd.read_parquet(path=self.settings.path)
    
    def write(self,dataframe:pd.DataFrame):
        lgr.info("Writing parquet file",self.settings)
        dataframe.to_parquet(self.settings.path)