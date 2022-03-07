import unittest
import pandas as pd
from datalad_helloworld.writers.csv import Csv

class TestCsv(unittest.TestCase):
    def __init__(self,*args,**kwargs):
        unittest.TestCase.__init__(self,*args,**kwargs)
        self.settings_w_header = {"file":{"format":"csv","separator":";","names":["Name", "Age"],"header":"None","path":"./resources/test_exists.csv"}}
        self.settings_w_names = {"file":{"format":"csv","separator":";","names":[],"header":0,"path":"./resources/test_exists.csv"}}
        self.settings = {"file":{"format":"csv","separator":";","names":[],"header":0,"path":"./resources/test_exists.csv"}}
        self.dataframe = {'Name': ['Tom', 'Joseph', 'Krish', 'John'], 'Age': [20, 21, 19, 18]}  
    def test_read_header(self):
        res = Csv(self.settings_w_header).read()
        self.assertEqual(isinstance(res),pd.DataFrame)
    def test_read_names(self):
        res = Csv(self.settings_w_names).read()
        self.assertEqual(isinstance(res),pd.DataFrame)
    def test_read(self):
        res = Csv(self.settings).read()
        self.assertEqual(isinstance(res),pd.DataFrame)
    def test_write_header(self):
        df = pd.DataFrame(self.dataframe)
        res = Csv(self.settings_w_header).write(df)
        self.assertEqual(res,True)
    def test_write_names(self):
        df = pd.DataFrame(self.dataframe)
        res = Csv(self.settings_w_names).write(df)
        self.assertEqual(res,True)
    def test_write(self):
        df = pd.DataFrame(self.dataframe)
        res = Csv(self.settings).write(df)
        self.assertEqual(res,True)