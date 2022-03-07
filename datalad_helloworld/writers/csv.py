import pandas as pd
import logging

lgr = logging.getLogger('datalad.helloworld.hello_cmd.writers.csv')

class Csv:
    def __init__(self, settings):
        self.settings = settings
    def read(self):
        lgr.info("Reading csv file ",self.settings)
        if self.settings.get("header","None") != "None":
            return pd.read_csv(
                self.settings.path,
                sep=self.settings.separator,
                header=self.settings.header
                )
        elif self.settings.get("names",[]) != []:
            return pd.read_csv(
                self.settings.path,
                sep=self.settings.separator,
                names=self.settings.names
                )
        else:
            return pd.read_csv(
                self.settings.path,
                sep=self.settings.separator
                )
    def write(self, dataframe:pd.DataFrame):
        lgr.info("Writing csv file ",self.settings)
        if self.settings.get("header","None") != "None":
            return dataframe.to_csv(
                path_or_buf=self.settings.path,
                sep=self.settings.separator,
                header=self.settings.header
                )
        elif self.settings.get("names",[]) != []:
            return dataframe.to_csv(
                path_or_buf=self.settings.path,
                sep=self.settings.separator,
                columns=self.settings.names
                )
        else:
            return dataframe.to_csv(
                path_or_buf=self.settings.path,
                sep=self.settings.separator
                )