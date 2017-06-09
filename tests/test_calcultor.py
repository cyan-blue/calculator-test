#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import json
import unittest

sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "../")
))
from cal.calcultor import Calculator


class CalculatorTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(3, Calculator().add(1, 2))


if __name__ == '__main__':
    unittest.main()
