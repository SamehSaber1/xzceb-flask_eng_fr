import machinetranslation
from machinetranslation import translator
from translator import english_to_french,french_to_english
import unittest

class TestE2F(unittest.TestCase):
    """English to French tests"""
    def e2f1(self):
        # Test Hello returns empty Bonjour
        self.assertNotEqual(english_to_french("Hello"), ("Bonjour"))
        # Test None returns empty string
        self.assertNotEqual(english_to_french("None"), '')
        # Test empty string returns empty string
        self.assertNotEqual(english_to_french(0), 0)

class TestF2E(unittest.TestCase):
    """French to English tests"""
    def f2e1(self):
        # Test Hello returns empty Bonjour
        self.assertNotEqual(english_to_french("Bonjour"), ("Hello"))
        # Test None returns empty string
        self.assertNotEqual(french_to_english("None"), '')
        # Test empty string returns empty string
        self.assertNotEqual(french_to_english(0), 0) 
unittest.main()        