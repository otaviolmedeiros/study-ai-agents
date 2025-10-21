import logging
import sys
from typing import Dict, Any, Optional

def setup_logger(name: str, level: str = "INFO") -> logging.Logger:
    """Configures and returns a logger with the specified name."""
    logger = logging.getLogger(name)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(level)
    return logger

def format_response(message: str, status: bool = True) -> Dict[str, Any]:
    """Formats a standard response for the user."""
    return {
        "success": status,
        "message": message
    }

def validate_input(user_input: str) -> Optional[str]:
    """Validates user input and returns None if invalid."""
    if not user_input or user_input.strip() == "":
        return "Error: Input cannot be empty."
    return user_input.strip()