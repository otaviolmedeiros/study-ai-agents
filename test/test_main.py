import unittest
from unittest.mock import patch, MagicMock
from main import main

class TestMain(unittest.TestCase):
    @patch('main.Router')
    @patch('builtins.input')
    @patch('builtins.print')
    def test_exit_command(self, mock_print, mock_input, mock_router):
        # Tests the exit command functionality
        mock_input.side_effect = ['exit']
        main()
        
        # Verifies exit behavior
        mock_print.assert_any_call("AI Agent initialized. Type 'exit' to quit.")
        mock_print.assert_any_call("Goodbye!")
        self.assertEqual(mock_input.call_count, 1)

    @patch('main.Router')
    @patch('builtins.input')
    @patch('builtins.print')
    def test_process_flow(self, mock_print, mock_input, mock_router):
        # Tests normal processing flow
        input_data = "test input"
        expected_response = "test response"
        
        # Configure mocks
        mock_input.side_effect = [input_data, 'exit']
        mock_skill = MagicMock()
        mock_router_instance = MagicMock()
        mock_router_instance.process.return_value = expected_response
        mock_router.return_value = mock_router_instance

        main()
        
        # Verifies processing
        mock_router_instance.process.assert_called_once_with(input_data)
        mock_print.assert_any_call(f"Agent: {expected_response}")
        self.assertEqual(mock_input.call_count, 2)

    @patch('main.Router')
    @patch('builtins.input')
    def test_router_initialization(self, mock_input, mock_router):
        # Tests router initialization
        mock_input.side_effect = ['exit']
        main()
        mock_router.assert_called_once()

if __name__ == '__main__':
    unittest.main()