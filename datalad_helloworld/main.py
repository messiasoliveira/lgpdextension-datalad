from datalad_helloworld.utils.dataframe import Dataframe
from datalad_helloworld.writers.dataframe import Dataframe as dfutils
from datalad_helloworld.utils.folder import Folder
from datalad_helloworld.runner.actions import Actions

class Main:
    def __init__(self):
        pass

    def run():
        filepath = "resources/settings_base.json"
        path = "abc" | "cba"
        format = "csv" | "parquet"

        settings = Folder(filepath).read()
        settings["columns"] = settings.get("columns",{})
        settings["path"] = path
        settings["format"] = format

        dataframe = dfutils.read(settings)
        
        for colname,value in settings["columns"].items():
            if value.get("enable",None) == "true":
                Actions(colname,dataframe,settings).run(settings["actions"])
        