from skills.example_skill import ExampleSkill

class Router:
    def __init__(self):
        # Initialize available skills
        self.skills = {
            "example": ExampleSkill()
        }

    def process(self, user_input):
        # Logic to determine which skill to use
        if "example" in user_input.lower() or self.skills["example"].can_handle(user_input):
            return self.skills["example"].execute(user_input)
        # Default response if no skill is identified
        return "I'm not sure how to help with that yet."