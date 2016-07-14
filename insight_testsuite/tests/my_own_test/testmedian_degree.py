import unittest
import numpy as np
import pandas as pd
import json 
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

    def test_Timestamp(self): 
        expected = '2016-03-28 23:25:12'
        actual = median_degree.TimeStamp(self.d,2)
        self.assertEqual(expected,actual.__str__())

    def test_IntersectDataFrame(self): 
        expected = 54 
        actual = median_degree.IntersectDataFrame(self.d,0)
        self.assertEqual(0,norm(expected-len(actual)))
     

    def test_EdgeList(self):
        expected = [(u'Amber-Sauer', u'charlotte-macfarlane'),
                 (u'Amber-Sauer', u'Caroline-Kaiser-2'),
                 (u'Amber-Sauer', u'Raffi-Antilian'),
                 (u'Raffi-Antilian', u'charlotte-macfarlane'),
                 (u'Raffi-Antilian', u'Caroline-Kaiser-2'),
                 (u'andres-camacho', u'Matt-LaPointe-1'),
                 (u'andres-camacho', u'BPNeal'),
                 (u'andres-camacho', u'Ricardo-Lach'),
                 (u'andres-camacho', u'Tallulah-Daly'),
                 (u'Caroline-Kaiser-2', u'Megan-Braverman'),
                 (u'Caroline-Kaiser-2', u'Ricardo-Lach'),
                 (u'Caroline-Kaiser-2', u'Cary-Gitter'),
                 (u'Caroline-Kaiser-2', u'Joey-Feste'),
                 (u'Caroline-Kaiser-2', u'charlotte-macfarlane'),
                 (u'Caroline-Kaiser-2', u'Trong-Dang'),
                 (u'Caroline-Kaiser-2', u'Lizzy-Smith-5'),
                 (u'charlotte-macfarlane', u'Megan-Braverman'),
                 (u'charlotte-macfarlane', u'Ricardo-Lach'),
                 (u'charlotte-macfarlane', u'Cary-Gitter'),
                 (u'charlotte-macfarlane', u'Joey-Feste'),
                 (u'charlotte-macfarlane', u'Trong-Dang'),
                 (u'charlotte-macfarlane', u'Lizzy-Smith-5'),
                 (u'Trong-Dang', u'Lizzy-Smith-5'),
                 (u'Megan-Braverman', u'Cary-Gitter'),
                 (u'Megan-Braverman', u'Ricardo-Lach'),
                 (u'Megan-Braverman', u'Joey-Feste'),
                 (u'Ricardo-Lach', u'Cary-Gitter'),
                 (u'Ricardo-Lach', u'Tallulah-Daly'),
                 (u'Ricardo-Lach', u'Joey-Feste'),
                 (u'Cary-Gitter', u'Joey-Feste'),
                 (u'Lexi-Romanchuk', u'Nelida-Mendoza'),
                 (u'michael92v', u'Faisal49'),
                 (u'michael92v', u'Maxwell-Parkinson'),
                 (u'michael92v', u'Ian-Leefmans'),
                 (u'Maxwell-Parkinson', u'Faisal49'),
                 (u'Maxwell-Parkinson', u'Ian-Leefmans'),
                 (u'trishalynnberry', u'douknowbinh'),
                 (u'Ian-Leefmans', u'Faisal49'),
                 (u'Clint-Brotherton', u'Isaac-Santos'),
                 (u'Lizzy-Greener', u'Elliott-Yodh'),
                 (u'Chase-McAlister', u'Sarah-Motta-1'),
                 (u'Chase-McAlister', u'Alex-Holle'),
                 (u'Chase-McAlister', u'Lincoln-Howarth'),
                 (u'Chase-McAlister', u'CVRogers'),
                 (u'BPNeal', u'Matt-LaPointe-1'),
                 (u'GillyQuinn', u'StephenTipton'),
                 (u'Sarah-Motta-1', u'Alex-Holle'),
                 (u'Sarah-Motta-1', u'Lincoln-Howarth'),
                 (u'Sarah-Motta-1', u'CVRogers'),
                 (u'Alex-Holle', u'Lincoln-Howarth'),
                 (u'Alex-Holle', u'CVRogers'),
                 (u'CVRogers', u'Lincoln-Howarth')]
        actual = median_degree.EdgeList(self.d,0)
        self.assertEqual(expected,actual)

    def test_MedianDegree(self):
        d = median_degree.parse('venmo-trans-test.txt')
        expected = 1.0 
        actual = median_degree.MedianDegree(d,0)
        self.assertEqual(expected,actual)
