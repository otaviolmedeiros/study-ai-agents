import unittest
from unittest.mock import MagicMock
from router import Router
from skills.example_skill import ExampleSkill

class TestRouter(unittest.TestCase):
    def setUp(self):
        self.router = Router()
        self.mock_skill = MagicMock(spec=ExampleSkill)
        self.router.skills["example"] = self.mock_skill

    def test_router_initialization(self):
        """Tests if router initializes with correct skills"""
        self.assertIn("example", self.router.skills)
        self.assertIsInstance(self.router.skills["example"], ExampleSkill)

    def test_process_with_example_keyword(self):
        """Tests processing input containing example keyword"""
        input_data = "Can you show me an example?"
        self.mock_skill.execute.return_value = "Example response"
        
        response = self.router.process(input_data)
        
        self.mock_skill.execute.assert_called_once_with(input_data)
        self.assertEqual(response, "Example response")

    def test_process_with_skill_handling(self):
        """Tests processing input handled by skill's can_handle"""
        input_data = "demo request"
        self.mock_skill.can_handle.return_value = True
        self.mock_skill.execute.return_value = "Handled response"
        
        response = self.router.process(input_data)
        
        self.mock_skill.can_handle.assert_called_once_with(input_data)
        self.mock_skill.execute.assert_called_once_with(input_data)
        self.assertEqual(response, "Handled response")

    def test_process_with_unhandled_input(self):
        """Tests processing unrecognized input"""
        input_data = "random question"
        self.mock_skill.can_handle.return_value = False
        
        response = self.router.process(input_data)
        
        self.assertEqual(response, "I'm not sure how to help with that yet.")
        self.mock_skill.execute.assert_not_called()

if __name__ == "__main__":
    unittest.main()