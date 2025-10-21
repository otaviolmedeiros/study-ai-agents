# AI Agent Python Application

## Overview
This project implements a simple AI agent system using Python. The architecture follows a user input > router > skill pattern.

## Project Structure
```
.
├── main.py           # Entry point of the application
├── router.py         # Routes user inputs to appropriate skills
├── config.py         # Configuration settings
├── skills/           # Directory containing all agent skills
│   ├── __init__.py
│   ├── base_skill.py # Abstract base class for all skills
│   └── example_skill.py # Demo skill implementation
├── utils/            # Utility functions package
│   ├── __init__.py
│   └── helpers.py    # Helper functions for logging and input handling
```

## Setup and Installation
1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python main.py`

## Usage
- Type your messages to interact with the AI agent
- The agent will route your input to appropriate skills
- Type 'exit' to quit the application

## Key Features
- Modular skill system
- Configurable through config.py
- Extensible router mechanism
- Utility helpers for common tasks