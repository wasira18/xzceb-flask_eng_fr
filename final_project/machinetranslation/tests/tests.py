import unittest
from deep_translator import MyMemoryTranslator

class TranslatorTestCase(unittest.TestCase):
    def test_englishToFrench(self):
        # Test case 1: Translation of 'Hello' to French
        english_text = 'Hello'
        expected_translation = 'Bonjour'
        translator = MyMemoryTranslator(source='en-GB', target='fr-CA')
        french_text = translator.translate(english_text)
        self.assertEqual(french_text, expected_translation)

        # Test case 2: Translation of 'Bonjour' to French
        french_text = 'Bonjour'
        expected_translation = 'Bonjour'  # Expected translation should remain the same
        translator = MyMemoryTranslator(source='fr-CA', target='fr-CA')
        french_text = translator.translate(french_text)
        self.assertEqual(french_text, expected_translation)

    def test_frenchToEnglish(self):
        # Test case 1: Translation of 'Bonjour' to English
        french_text = 'Bonjour'
        expected_translation = 'Hello'
        translator = MyMemoryTranslator(source='fr-CA', target='en-GB')
        english_text = translator.translate(french_text)
        self.assertEqual(english_text, expected_translation)

        # Test case 2: Translation of 'Hello' to English
        english_text = 'Hello'
        expected_translation = 'Hello'  # Expected translation should remain the same
        translator = MyMemoryTranslator(source='en-GB', target='en-GB')
        english_text = translator.translate(english_text)
        self.assertEqual(english_text, expected_translation)


if __name__ == '__main__':
    unittest.main()