import unittest
from typing import Type
from unittest import TestCase
from unittest.suite import TestSuite


def run_single_test(class_name: object, methods: list[str]) -> None:
    for each_method in methods:
        getattr(class_name, each_method)()
        print(f'test steps: {each_method}')


def run_multiple_tests(class_name: Type[TestCase]) -> None:
    suite = TestSuite()
    tests = unittest.TestLoader()
    suite.addTest(tests.loadTestsFromTestCase(class_name))
    suite.addTest(tests.loadTestsFromTestCase(class_name))
    run = unittest.TextTestRunner()
    run.run(suite)
