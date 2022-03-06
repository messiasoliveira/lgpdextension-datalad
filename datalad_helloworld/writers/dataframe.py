from datalad_helloworld.writers.csv import Csv
import logging
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
            return Parquet(settings).read()
        return None
    
    def write(self, settings):
        lgr.info("Writing dataframe to " + settings.get("format",None))
        if settings.get("format",None) == "csv":
            return Csv(settings["file"]).write()
        elif settings.get("format",None) == "parquet":
            return Parquet(settings).write()
        return None