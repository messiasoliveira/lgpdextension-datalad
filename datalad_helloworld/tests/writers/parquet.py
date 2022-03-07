import unittest
import pandas as pd
from datalad_helloworld.writers.parquet import Parquet

class TestParquet(unittest.TestCase):
    def __init__(self,*args,**kwargs):
        unittest.TestCase.__init__(self,*args,**kwargs)
        self.settings_w_names = {"file":{"format":"parquet","separator":"","names":["Name", "Age"],"header":"None","path":"./resources/test_exists.parquet"}}
        self.settings = {"file":{"format":"parquet","separator":"","names":[],"header":"None","path":"./resources/test_exists.parquet"}}
        self.dataframe = {'Name': ['Tom', 'Joseph', 'Krish', 'John'], 'Age': [20, 21, 19, 18]}  
    def test_read_header(self):
        res = Parquet(self.settings_w_names).read()
        self.assertEqual(isinstance(res),pd.DataFrame)
    def test_read(self):
        res = Parquet(self.settings).read()
        self.assertEqual(isinstance(res),pd.DataFrame)
    def test_write_names(self):
        df = pd.DataFrame(self.dataframe)
        res = Parquet(self.settings_w_names).write(df)
        self.assertEqual(res,True)
    def test_write(self):
        df = pd.DataFrame(self.dataframe)
        res = Parquet(self.settings).write(df)
        self.assertEqual(res,True)