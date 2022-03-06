import pandas as pd
import logging
from datalad_helloworld.utils.dataframe import Dataframe
from datalad_helloworld.crypto.rsa import Rsa
from datalad_helloworld.writers.dataframe import Dataframe as dfutils
from datalad_helloworld.runner.operations import Operations

lgr = logging.getLogger('datalad.helloworld.hello_cmd.runner.actions')

class Actions:
    def __init__(self,colname,dataframe:pd.DataFrame,settings):
        self.colname = colname
        self.dataframe:pd.DataFrame = dataframe
        self.settings = settings

    def run(self, action):
        lgr.info("run to " + action)
        switch = {
            "tokenization":self.tokenization(),
            "ofuscation":self.ofuscation(),
            "anonymation":self.anonymation()
        }
        switch.get(action,None)
    
    def execute(self,rsa):
        lgr.info("execute to " + rsa)
        print("PUBLICKEY :: " + rsa.publickey())
        print("PRIVATEKEY :: " + rsa.privatekey())
        dfobj = Dataframe(self.dataframe,rsa,self.colname)
        opobj = Operations(dfobj)
        opobj.run(self.settings["columns"][self.colname]["operations"])
        opobj.dataframe.encrypt(self.colname)
        dfutils.write(self.dataframe,self.settings)
    
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
        dfobj = Dataframe(self.dataframe,None,self.colname)
        opobj = Operations(dfobj)
        opobj.run()
        dfutils.write(self.dataframe,self.settings)
    
    @property
    def settings(self):
        return self.settings

    @property
    def dataframe(self):
        return self.dataframe