import unittest
import pandas as pd
from datalad_helloworld.crypto.rsa import Rsa

class TestRsa(unittest.TestCase):
    def __init__(self,*args,**kwargs):
        unittest.TestCase.__init__(self,*args,**kwargs)