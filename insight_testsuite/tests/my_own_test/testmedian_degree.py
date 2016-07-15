import unittest
import numpy as np
import pandas as pd
import json 
import sys
sys.path.append('../../../src') 
import median_degree
from numpy.linalg import norm

class Testmedian_degree(unittest.TestCase):
    def setUp(self): 
        self.d = median_degree.parse('venmo-trans.txt')
    
    def tearDown(self): 
        pass

    def test_parse(self):
        d = [{"created_time": "2016-04-07T03:33:19Z", "target": "Jamie-Korn", "actor": "Jordan-Gruber"}]
        expected = pd.DataFrame(d)
        actual = median_degree.parse('venmo-trans-test.txt')
        self.assertEqual(0,norm(len(expected)-len(actual)))

    def test_IntersectDataFrame(self): 
        expected = 54 
        actual = median_degree.IntersectDataFrame(self.d,0)
        self.assertEqual(0,norm(expected-len(actual)))
     

    def test_MedianDegree(self):
        d = median_degree.parse('venmo-trans-test.txt')
        expected = 1.0 
        actual = median_degree.MedianDegree(d,0)
        self.assertEqual(expected,actual)

    def test_RollingMedianDegree(self): 
        pass 
