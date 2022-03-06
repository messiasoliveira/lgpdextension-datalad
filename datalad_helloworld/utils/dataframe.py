import logging
import pandas as pd
from datalad_helloworld.crypto.rsa import Rsa

lgr = logging.getLogger('datalad.helloworld.hello_cmd.utils.dataframe')

class Dataframe:
    def __init__(self, dataframe:pd.DataFrame,rsa:Rsa,colname):
        self.cryptoObj = rsa
        self.dataframe = dataframe
        self.colname = colname
        self.date_format = {"BR":"%d/%m/%y","US":"%m/%d/%y","CN":"%y/%m/%d"}
        self.price_format = {"BR":"${:.,2f}","US":"${:,.2f}"}
    
    def encrypt(self,colname):
        lgr.info("Encrypt to " + self.colname)
        self.dataframe[colname].apply(self.cryptoObj.encrypt)
    
    def decrypt(self,colname):
        lgr.info("Decrypt to " + self.colname)
        self.dataframe[colname].apply(self.cryptoObj.decrypt)    

    def upper(self):
        lgr.info("Upper to " + self.colname)
        self.dataframe[self.colname] = self.dataframe[self.colname].str.upper()
    
    def lower(self):
        lgr.info("Lower to " + self.colname)
        self.dataframe[self.colname] = self.dataframe[self.colname].str.lower()
    
    def toInt(self):
        lgr.info("toInt to " + self.colname)
        self.dataframe[self.colname] = self.dataframe[self.colname].astype(int)
    
    def toFloat(self):
        lgr.info("toFloat to " + self.colname)
        self.dataframe[self.colname] = self.dataframe[self.colname].astype(float)
    
    def toNumeric(self):
        lgr.info("toNumeric to " + self.colname)
        self.dataframe[self.colname] = pd.to_numeric(self.dataframe[self.colname])

    def toPrice(self,format="BR"):
        lgr.info("toPrice to " + self.colname + " - format to " + format)
        self.dataframe[self.colname] = self.dataframe[self.colname].map(self.price_format.get(format,format).format)
    
    def toDate(self,format="BR"):
        lgr.info("toDate to " + self.colname + " - format to " + format)
        self.dataframe[self.colname] = self.dataframe[self.colname].dt.strftime(self.date_format.get(format,format))
    
    def json(self,text):
        lgr.info("json to " + self.colname + " - " + text)
        self.dataframe[self.colname] = self.dataframe[self.colname].map(text)

    def range_numeric(self,text):
        lgr.info("range_numeric to " + self.colname + " - " + text)
        values = {}
        for i in text.keys():
            key = i.split("-")
            nums = [str(i) for i in range(int(key[0]),int(key[1])+1)]
            for j,_ in enumerate(nums):
                values.update(dict(zip(nums[j::], str(text[i]))))
        self.json(values)