import unittest
import testExample
import testmedian_degree

def suite():
    s = unittest.TestSuite()

    s.addTest(unittest.makeSuite(testExample.TestSequenceFunctions))
    s.addTest(unittest.makeSuite(testmedian_degree.Testmedian_degree))

    return s

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
