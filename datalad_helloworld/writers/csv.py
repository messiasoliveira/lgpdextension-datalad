import pandas as pd
import logging
lgr = logging.getLogger('datalad.helloworld.hello_cmd.writers.csv')

class Csv:
    def __init__(self, settings):
        self.settings = settings 

    def read(self):
        lgr.info("Reading csv file ",self.settings)
        if self.settings.get("header",None):
            return pd.read_csv(
                self.settings.path,
                sep=self.settings.separator,
                header=self.settings.header
                )
        elif self.settings.get("usecols",None):
            return pd.read_csv(
                self.settings.path,
                sep=self.settings.separator,
                usecols=self.settings.usecols
                )
        else:
            return pd.read_csv(
                self.settings.path,
                sep=self.settings.separator
                )
    
    def write(self):
        lgr.info("Writing csv file ",self.settings)
        if self.settings.get("header",None):
            return pd.DataFrame.to_csv(
                path_or_buf=self.settings.path,
                sep=self.settings.separator,
                header=self.settings.header
                )
        elif self.settings.get("header",None):
            return pd.DataFrame.to_csv(
                path_or_buf=self.settings.path,
                sep=self.settings.separator,
                columns=self.settings.usecols
                )
        else:
            return pd.DataFrame.to_csv(
                path_or_buf=self.settings.path,
                sep=self.settings.separator
                )