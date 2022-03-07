import logging
import pandas as pd
from datalad_helloworld.writers.csv import Csv
from datalad_helloworld.writers.parquet import Parquet

lgr = logging.getLogger('datalad.helloworld.hello_cmd.writers.dataframe')

class Dataframe:
    def __init__():
        pass
    def read(self, settings):
        lgr.info("Reading path to " + settings.get("format",None))
        if settings.get("format",None) == "csv":
            return Csv(settings["file"]).read()
        elif settings.get("format",None) == "parquet":
            return Parquet(settings["file"]).read()
        return None
    def write(self, dataframe:pd.DataFrame, settings):
        lgr.info("Writing dataframe to " + settings.get("format",None))
        if settings.get("format",None) == "csv":
            return Csv(settings["file"]).write(dataframe)
        elif settings.get("format",None) == "parquet":
            return Parquet(settings["file"]).write(dataframe)
        return None