# -*- coding: utf-8 -*-

import unittest
from Answer import _2_AddTwoNumbers


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.expect = [7, 0, 8]

    def test_solution(self):
        input_1 = [2, 4, 3]
        input_2 = [5, 6, 4]
        calc = _2_AddTwoNumbers.Solution()
        actual = calc.addTwoNumbers(input_1, input_2)
        self.assertEqual(self.expect, actual)
