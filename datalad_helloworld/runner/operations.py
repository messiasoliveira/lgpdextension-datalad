import logging
from datalad_helloworld.utils.dataframe import Dataframe

lgr = logging.getLogger('datalad.helloworld.hello_cmd.runner.operations')

class Operations:
    def __init__(self, dataframe:Dataframe):
        self.dataframe:Dataframe = dataframe

    def run(self, settings):
        lgr.info("run to " + settings)
        operations = [x for x in settings.keys()]
        for op in operations:
            self.select(op)

    def select(self,operation):
        lgr.info("select to " + operation)
        switch = {
            "upper":self.dataframe.upper(),
            "lower":self.dataframe.lower(),
            "toInt":self.dataframe.toInt(),
            "toFloat":self.dataframe.toFloat(),
            "toNumeric":self.dataframe.toNumeric(),
            "toPrice":self.dataframe.toPrice(),
            "toDate":self.dataframe.toDate(),
            "json":self.dataframe.json(),
            "range_numeric":self.dataframe.range_numeric()
        }
        switch.get(operation,None)
    
    @property
    def dataframe(self):
        return self.dataframe