import unittest
from xml.parsers.expat import ExpatError
from src.services.save_service import load_save_file

class TestSaveService(unittest.TestCase):

    def test_file_is_loaded(self):
        data = load_save_file("tests/Ivans_401983009.xml")
        self.assertIsNotNone(data)

    def test_valid_file(self):
        data = load_save_file("tests/Ivans_401983009.xml")
        self.assertIn("name", data["SaveGame"]["player"])
        self.assertEqual(data["SaveGame"]["player"]["name"], "Ivan")

    def test_invalid_xml(self):
        with self.assertRaises(ExpatError):
            data = load_save_file("tests/badxml.xml")

    def test_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            load_save_file("tests/data/does_not_exist.xml")

if __name__ == "__main__":
    unittest.main()