# test_pivotflux.py
"""
Tests for PivotFlux module.
"""

import unittest
from pivotflux import PivotFlux

class TestPivotFlux(unittest.TestCase):
    """Test cases for PivotFlux class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PivotFlux()
        self.assertIsInstance(instance, PivotFlux)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PivotFlux()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
