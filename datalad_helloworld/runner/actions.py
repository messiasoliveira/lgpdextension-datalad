import pandas as pd
import logging
from datalad_helloworld.utils.dataframe import Dataframe as dfoperations
from datalad_helloworld.crypto.rsa import Rsa
from datalad_helloworld.writers.dataframe import Dataframe as dfutils
from datalad_helloworld.runner.operations import Operations
from datalad_helloworld.utils.folder import Folder
lgr = logging.getLogger('datalad.helloworld.hello_cmd.runner.actions')

class Actions:
    def __init__(self,colname,settings,df,settingspath):
        self.colname = colname
        setattr(Actions, 'dataframe', df)
        setattr(Actions, 'settings', settings)
        self.colsettings = settings["columns"][colname]
        self.filenamesettings = settingspath
    def run(self, action):
        lgr.info("run to " + str(action))
        switch = {
            "tokenization":self.tokenization(),
            "ofuscation":self.ofuscation(),
            "anonymation":self.anonymation()
        }
        switch.get(action,None)
    def execute(self,rsa):
        lgr.info("execute to " + str(rsa))
        print("PUBLICKEY :: " + str(rsa.publickey))
        print("PRIVATEKEY :: " + str(rsa.privatekey))
        dfobj = dfoperations(self.dataframe,rsa,self.colname)
        opobj = Operations(dfobj)
        opobj.run(self.settings["columns"][self.colname]["operations"])
        dfutils().write(opobj.dataframe.dataframe,self.settings)
        
    def tokenization(self):
        lgr.info("tokenization action")
        rsa = Rsa()
        self.settings["tokenization"] = rsa.tokenization(self.settings.get("tokenization",{}))
        self.execute(rsa)
    def ofuscation(self):
        lgr.info("ofuscation action")
        rsa = Rsa()
        self.settings["ofuscation"] = rsa.ofuscation(self.settings.get("ofuscation",{}))
        self.execute(rsa)
    def anonymation(self):
        lgr.info("anonymation action")
        dfobj = dfoperations(self.dataframe,None,self.colname)
        opobj = Operations(dfobj)
        opobj.run(self.colsettings["operations"])
        dfutils().write(self.dataframe,self.settings)
    @property
    def settings(self):
        return self.settings
    def settings_set(self, value):
        self.settings = value
    @property
    def dataframe(self):
        return self.dataframe