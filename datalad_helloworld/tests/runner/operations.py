import unittest
import pandas as pd
from datalad_helloworld.runner.operations import Operations
from datalad_helloworld.utils.dataframe import Dataframe

class TestOperations(unittest.TestCase):
    def __init__(self,*args,**kwargs):
        unittest.TestCase.__init__(self,*args,**kwargs)
        self.dataframe = {'Name': ['Tom', 'Joseph', 'Krish', 'John'], 'Age': [20, 21, 19, 18]}  
        self.operations = {"upper": "true"}
    def test_run(self):
        df = pd.DataFrame(self.dataframe)
        dataframe = Dataframe(df,None,"Name")
        res = Operations(dataframe).run(self.operations)
        self.assertTrue(res)
    def test_select(self):
        df = pd.DataFrame(self.dataframe)
        dataframe = Dataframe(df,None,"Name")
        res = Operations(dataframe).select("upper",self.operations["upper"])
        self.assertTrue(res)