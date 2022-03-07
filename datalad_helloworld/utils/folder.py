import os
import sys
import json
import logging

lgr = logging.getLogger('datalad.helloworld.hello_cmd.utils.folder')

class Folder:
    def __init__(self, path=None):
        self.path = path
    @classmethod
    def getcurrent(self):
        return os.getcwd()
    @classmethod
    def updatevalue(self,element):
        element.obj[element.key] = element.value
        return element
    def read(self):
        content = ""
        with open(self.path, 'r') as openfile:
            content = json.load(openfile)
        return content
    def save(self,settings):
        output = json.dumps(settings, indent = 4)
        with open(self.path, "w") as file:
            file.write(output)