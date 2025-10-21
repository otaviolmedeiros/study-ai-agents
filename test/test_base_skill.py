import unittest
from skills.base_skill import BaseSkill

class TestBaseSkill(unittest.TestCase):
    def test_base_class_cannot_be_instantiated(self):
        """Test that BaseSkill abstract class cannot be instantiated directly"""
        with self.assertRaises(TypeError):
            BaseSkill(name="Invalid Skill")

    def test_execute_method_requires_implementation(self):
        """Test that subclasses must implement execute method"""
        class InvalidSkill(BaseSkill):
            def __init__(self):
                super().__init__(name="Invalid Skill")

        with self.assertRaises(TypeError):
            InvalidSkill()

    def test_can_handle_default_implementation(self):
        """Test the default can_handle implementation returns False"""
        class TestSkill(BaseSkill):
            def __init__(self):
                super().__init__(name="Test Skill")
            
            def execute(self, input_data):
                pass

        skill = TestSkill()
        self.assertFalse(skill.can_handle("any input"))

    def test_skill_initialization_with_name(self):
        """Test skill initialization with proper name setting"""
        class TestSkill(BaseSkill):
            def __init__(self):
                super().__init__(name="Test Skill")
            
            def execute(self, input_data):
                pass

        skill = TestSkill()  # Removed the name argument
        self.assertEqual(skill.name, "Test Skill")

    def test_concrete_skill_execution(self):
        """Test concrete skill implementation"""
        mock_response = "Mock response"
        
        class ValidSkill(BaseSkill):
            def __init__(self):
                super().__init__(name="Valid Skill")
            
            def execute(self, input_data):
                return mock_response

        skill = ValidSkill()
        self.assertEqual(skill.execute("test input"), mock_response)

if __name__ == '__main__':
    unittest.main()