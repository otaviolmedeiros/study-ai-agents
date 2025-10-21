from .base_skill import BaseSkill

class ExampleSkill(BaseSkill):
    """An example skill that demonstrates the skill structure."""
    
    def __init__(self):
        super().__init__(name="Example Skill")
    
    def execute(self, input_data):
        """Process the input and return a response.
        
        Args:
            input_data: The input data from the user.
        
        Returns:
            A string response to the user input.
        """
        return f"Example skill processed: {input_data}"
    
    def can_handle(self, input_data):
        """Check if this skill can handle the input.
        
        Args:
            input_data: The input to check.
        
        Returns:
            True if the input contains keywords this skill can handle.
        """
        keywords = ["example", "demo", "test"]
        return any(keyword in input_data.lower() for keyword in keywords)