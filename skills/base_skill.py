from abc import ABC, abstractmethod

class BaseSkill(ABC):
    """Base class for all agent skills."""
    
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def execute(self, input_data):
        """Execute the skill with the given input data.
        
        Args:
            input_data: The input data from the user or system.
        
        Returns:
            The result of the skill execution.
        """
        pass

    def can_handle(self, input_data):
        """Determine if this skill can handle the given input.
        
        Args:
            input_data: The input data to check.
        
        Returns:
            Boolean indicating if this skill can handle the input.
        """
        return False