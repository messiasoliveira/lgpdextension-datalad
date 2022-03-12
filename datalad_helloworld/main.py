import logging
from datalad_helloworld.utils.dataframe import Dataframe
from datalad_helloworld.writers.dataframe import Dataframe as dfutils
from datalad_helloworld.utils.folder import Folder
from datalad_helloworld.runner.actions import Actions
from datalad_helloworld.utils.generate_config import GenerateConfig
from datalad_helloworld.utils.folder import Folder

lgr = logging.getLogger('datalad.helloworld.hello_cmd.writers.dataframe')

class Main:
    def __init__(self,filename=f"{Folder().getcurrent()}/_settings.json"):
        self.filename = filename
    def update_file(self,settings):
        defauld_field = "Added the '{{FIELD}} field'. YOU NEED TO CONFIGURE THE '{{FIELD}} FIELD' FROM SETTINGS JSON."
        msgs = ""
        if settings.get("ofuscation",None):
            msg = defauld_field.replace("{{FIELD}}","OFUSCATION")
            msgs += "\n" + msg
            lgr.info(msg)
            settings["ofuscation"] = GenerateConfig().addExampleOfuscation()
        if settings.get("tokenization",None):
            msg = defauld_field.replace("{{FIELD}}","TOKENIZATION")
            msgs = "\n" + msg
            lgr.info(msg)
            settings["tokenization"] = GenerateConfig().addExampleTokenization()
        if settings.get("file",None):
            msg = defauld_field.replace("{{FIELD}}","FILE")
            msgs += "\n"
            lgr.info(msg)
            settings["file"] = GenerateConfig().addExampleFile()
        if settings.get("columns",None):
            msg = defauld_field.replace("{{FIELD}}","COLUMNS")
            msgs += "\n" + msg
            lgr.info(msg)
            settings["columns"] = GenerateConfig().addExampleColumn()
        Folder(self.filename).save(settings)
        if msgs != "":
            raise Exception(msgs)
        return settings
    def run(self):
        if not Folder(self.filename).exists():
            settings = self.update_file(dict())
        else:
            fld = Folder(self.filename)
            settings = self.update_file(fld.read())
        dataframe = dfutils.read(settings)
        for colname,value in settings["columns"].items():
            if value.get("enable",None) == "true":
                Actions(colname,dataframe,settings,self.filename).run(settings["actions"])
        return True