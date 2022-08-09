import unittest

from unittest.loader import makeSuite

from test_cases.fill_in_a_form import TestFillInaForm
from test_cases.framework import Test
from test_cases.login_to_the_system import TestLoginPage


def full_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(makeSuite(TestLoginPage))
    test_suite.addTest(makeSuite(TestFillInaForm))
    test_suite.addTest(makeSuite(Test))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())