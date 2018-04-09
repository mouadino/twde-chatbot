# -*- coding: utf-8 -*-
import unittest


class TestExample(unittest.TestCase):
    def test_failing(self):
        self.assertEquals(True, False)
