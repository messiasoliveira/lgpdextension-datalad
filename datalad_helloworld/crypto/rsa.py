import logging
import rsa
from datalad_helloworld.utils.folder import Folder

lgr = logging.getLogger('datalad.helloworld.hello_cmd.runner.operations')

class Rsa:
    def __init__(self):
        self.publicKey = None
        self.privateKey = None

    def ofuscation(self,settings):
        lgr.info("ofuscation to " + settings)
        if not settings.get("publicKey",None) or not settings.get("privateKey",None):
            self.setkeys()
        settings = self.updatefile(settings,"publicKey",self.publicKey)
        settings = self.updatefile(settings,"privateKey",self.privateKey)
        return settings

    def tokenization(self,settings):
        lgr.info("tokenization to " + settings)
        if not settings.get("publicKey",None):
            self.publicKey = settings.get("publicKey",self.setpublickey())
        settings = self.updatefile(settings,"publicKey",self.publicKey)
        return settings

    def encrypt(self,text):
        lgr.info("encrypt to " + text)
        if self.publicKey:
            return rsa.encrypt(text.encode(),self.publicKey)
        return text
        
    def decrypt(self,text):
        lgr.info("decrypt to " + text)
        if self.privateKey:
            return rsa.decrypt(text, self.privateKey).decode()
        return text

    def generate(self):
        lgr.info("generate keys")
        publicKey,privateKey = rsa.newkeys(512)
        return publicKey,privateKey

    def setpublickey(self):
        lgr.info("setpublickey key")
        self.publicKey,_ = self.generate()
        
    def setkeys(self):
        lgr.info("setkeys keys")
        self.publicKey,self.privateKey = self.generate()

    def updatefile(self,settings):
        lgr.info("updatefile to " + settings)
        return Folder().updatevalue({"obj":settings,"key":self.key,"value":self.publicKey})

    @property
    def publickey(self):
        return self.publicKey
    
    @property
    def privatekey(self):
        return self.privateKey