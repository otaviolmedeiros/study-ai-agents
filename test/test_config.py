import unittest
import config

class TestConfig(unittest.TestCase):
    def test_api_key(self):
        self.assertEqual(config.API_KEY, "your_api_key_here")  # Verifies API key configuration

    def test_debug_mode(self):
        self.assertTrue(config.DEBUG_MODE)  # Checks debug mode status

    def test_log_level(self):
        self.assertEqual(config.LOG_LEVEL, "INFO")  # Validates logging level setting

    def test_log_file(self):
        self.assertEqual(config.LOG_FILE, "agent.log")  # Confirms log file name

    def test_request_timeout(self):
        self.assertEqual(config.REQUEST_TIMEOUT, 30)  # Ensures correct timeout duration

    def test_skills_dir(self):
        self.assertEqual(config.SKILLS_DIR, "skills")  # Verifies skills directory path

if __name__ == '__main__':
    unittest.main()