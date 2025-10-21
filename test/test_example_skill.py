import unittest
from skills.example_skill import ExampleSkill

class TestExampleSkill(unittest.TestCase):
    
    def setUp(self):
        self.skill = ExampleSkill()

    def test_skill_initialization(self):
        self.assertEqual(self.skill.name, "Example Skill")  # Assertion to check the skill's name
        self.assertTrue(isinstance(self.skill, ExampleSkill))  # Checks if the instance is of type ExampleSkill
    
    def test_execute(self):
        input_data = "This is a test input."  # Input data for the test
        expected_output = "Example skill processed: This is a test input."  # Expected output
        self.assertEqual(self.skill.execute(input_data), expected_output)  # Assertion to check the output

    def test_can_handle_with_keywords(self):
        input_data = "This is an example input."  # Input data for test with keywords
        self.assertTrue(self.skill.can_handle(input_data))  # Checks if the skill can handle the input

    def test_can_handle_without_keywords(self):
        input_data = "This input does not match."  # Input data that does not match
        self.assertFalse(self.skill.can_handle(input_data))  # Checks if the skill cannot handle the input

    def test_can_handle_with_invalid_input(self):
        invalid_inputs = [
            "hello world",  # Invalid input
            "how are you?",  # Invalid input
            "",  # Empty input
            "    ",  # Input with spaces
            "unrelated content"  # Unrelated content
        ]
        for input in invalid_inputs:
            with self.subTest(input=input):  # Subcase test for invalid inputs
                self.assertFalse(self.skill.can_handle(input))  # Checks if the skill cannot handle the input
    
    def test_edge_cases(self):
        self.assertTrue(self.skill.can_handle("EXAMPLE"))  # Checks if the skill can handle an edge case
        self.assertFalse(self.skill.can_handle(None))  # Checks if the skill cannot handle null input

if __name__ == '__main__':
    unittest.main()