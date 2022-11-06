from core.components.logs.log_generator import log
import unittest
from typing import Type
from unittest import TestCase
from unittest.suite import TestSuite
from tests.google.IntroPage import main as google_test
from tests.smarttap.button_test import main as smarttap_test
from dataclasses import dataclass


@dataclass
class RunTests:

    @log()
    def run_a_single_test(self, class_name: object, methods: list[str]) -> None:
        for each_method in methods:
            getattr(class_name, each_method)()
            print(f'test steps: {each_method}')

    @log()
    def run_multiple_tests(**args: Type[TestCase]) -> None:
        suite = TestSuite()
        tests = unittest.TestLoader()
        suite.addTest(tests.loadTestsFromTestCase(args))
        suite.addTest(tests.loadTestsFromTestCase(args))
        run = unittest.TextTestRunner()
        run.run(suite)
