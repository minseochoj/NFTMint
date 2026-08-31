# test_nftmint.py
"""
Tests for NFTMint module.
"""

import unittest
from nftmint import NFTMint

class TestNFTMint(unittest.TestCase):
    """Test cases for NFTMint class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NFTMint()
        self.assertIsInstance(instance, NFTMint)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NFTMint()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
