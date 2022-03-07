import unittest
import pandas as pd
from datalad_helloworld.writers.dataframe import Dataframe

class TestDataframe(unittest.TestCase):
    def __init__(self,*args,**kwargs):
        unittest.TestCase.__init__(self,*args,**kwargs)
        self.settings_csv = {"file":{"format":"csv","separator":";","names":[],"header":0,"path":"./resources/test_exists.csv"}}
        self.settings_parquet = {"file":{"format":"parquet","path":"./resources/test_exists.parquet"}}
        self.settings_none = {"file":{"format":"","path":"./resources/test_exists.parquet"}}
    def test_read_none(self):
        self.assertEqual(Dataframe.read(settings = self.settings_none),None)
    def test_read_parquet(self):
        res = Dataframe.read(settings = self.settings_parquet)
        self.assertEqual(isinstance(res),pd.DataFrame)
    def test_read_csv(self):
        res = Dataframe.read(settings = self.settings_csv)
        self.assertEqual(isinstance(res),pd.DataFrame)
    def test_write_none(self):
        self.assertEqual(Dataframe.write(settings = self.settings_none),None)
    def test_write_parquet(self):
        df = pd.DataFrame(["test1","test2"])
        res = Dataframe.write(df,settings = self.settings_parquet)
        self.assertEqual(isinstance(res),pd.DataFrame)
    def test_write_csv(self):
        df = pd.DataFrame(["test1","test2"])
        res = Dataframe.write(df,settings=self.settings_csv)
        self.assertEqual(isinstance(res),pd.DataFrame)