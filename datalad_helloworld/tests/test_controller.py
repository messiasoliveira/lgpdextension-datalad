import unittest   
from datalad_helloworld.tests.crypto.rsa import TestRsa
from datalad_helloworld.tests.runner.actions import TestActions
from datalad_helloworld.tests.runner.operations import TestOperations
from datalad_helloworld.tests.utils.dataframe import TestDataframe
from datalad_helloworld.tests.utils.folder import TestFolder 
from datalad_helloworld.tests.writers.csv import TestCsv
from datalad_helloworld.tests.writers.dataframe import TestDataframe
from datalad_helloworld.tests.writers.parquet import TestParquet
def create_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestCsv)
    test_suite.addTest(TestActions)
    test_suite.addTest(TestRsa)
    test_suite.addTest(TestDataframe)
    test_suite.addTest(TestOperations)
    test_suite.addTest(TestFolder)
    test_suite.addTest(TestParquet)
    return test_suite

if __name__ == '__main__':
   suite = create_suite()
   runner=unittest.TextTestRunner()
   runner.run(suite)