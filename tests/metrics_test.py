from unittest.mock import patch
from datetime import datetime

from core.graph import plotMarksGraph
from data.metrics import getMean, getTrendingValue, getMedianValue
import unittest

from main import marksArray


class MockMark:
    def __init__(self, markDate, markValue):
        self.markDate = markDate
        self.markValue = markValue

"""
    Unit test to ensure code reliability on
    metrics calculation trough mock data loaded
    as lists
"""


class TestMetricsCalc(unittest.TestCase):
    """
    Unit test to ensure reliability for mean value calculation
    through a list of mock marks.
    """
    def test_mean(self):
        marksArray = [
            MockMark(datetime(2023, 1, 1), 85),
            MockMark(datetime(2023, 1, 2), 90),
            MockMark(datetime(2023, 1, 3), 95),
        ]
        self.assertEqual(getMean(marksArray), 90.0)
    
    def test_trending(self):
        marksArray = [
            MockMark(datetime(2023, 1, 1), 85),
            MockMark(datetime(2023, 1, 2), 90),
            MockMark(datetime(2023, 1, 3), 90),
        ]
        self.assertEqual(90.0, getTrendingValue(marksArray))

    """
    Unit test for medain value calculation
    for both even and odd marks count cases
    """
    def test_median_even(self):
        marksArray = [
            MockMark(datetime(2023, 1, 1), 85),
            MockMark(datetime(2023, 1, 2), 90),
            MockMark(datetime(2023, 1, 2), 90),
        ]
        self.assertEqual(getMedianValue(marksArray), 2)

    def test_median_odd(self):
            marksArray = [
                MockMark(datetime(2023, 1, 1), 85),
                MockMark(datetime(2023, 1, 2), 90),
            ]
            self.assertEqual(getMedianValue(marksArray), 1)
if __name__ == "__main__":
    unittest.main()