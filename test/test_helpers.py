import unittest
from utils.helpers import setup_logger, format_response, validate_input

class TestHelpers(unittest.TestCase):

    def test_setup_logger(self):
        logger = setup_logger("test_logger")  # Sets up the logger
        self.assertIsNotNone(logger)  # Verifies that the logger is not None
        self.assertEqual(logger.name, "test_logger")  # Checks if the logger name is correct

    def test_format_response(self):
        response = format_response("Test message", True)  # Formats response for success
        self.assertEqual(response, {"success": True, "message": "Test message"})  # Asserts the response for success
        
        response = format_response("Test message", False)  # Formats response for failure
        self.assertEqual(response, {"success": False, "message": "Test message"})  # Asserts the response for failure

    def test_validate_input(self):
        self.assertIsNone(validate_input(""))  # Asserts that empty input returns None
        self.assertIsNone(validate_input("    "))  # Asserts that whitespace input returns None
        self.assertEqual(validate_input("valid input"), "valid input")  # Asserts that valid input returns itself

if __name__ == '__main__':
    unittest.main()