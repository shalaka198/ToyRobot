import sys
import unittest
import app.tests.unit_tests


if __name__ == '__main__':    
    
        testsuite = unittest.TestLoader().discover('app.tests', pattern='test_*.py')
        result = unittest.TextTestRunner(verbosity=2).run(testsuite)
        sys.exit(not result.wasSuccessful())