#!/bin/bash

        # Configures the project environment
        echo "Starting environment configuration..."

        PROJECT_DIR="/home/otaviolm/projetos/study/study-ai-agents"  # Updated to actual path

        # Check if the project directory exists
        if [ ! -d "$PROJECT_DIR" ]; then
            echo "Error: Project directory not found: $PROJECT_DIR"
            exit 1
        fi

        echo "Project directory verified: $PROJECT_DIR"

        # Set environment variables
        export PROJECT_ENV="dev"
        echo "Environment variables configured: ENV=$PROJECT_ENV"

        # Load project dependencies
        source "$PROJECT_DIR/dependencies.sh"
        echo "Dependencies loaded successfully."

        # Check if virtualenv is installed
        if ! command -v virtualenv &> /dev/null; then
            echo "Error: virtualenv is not installed. Please install virtualenv."
            exit 1
        fi

        # Create a virtual environment if it doesn't exist
        VENV_DIR="$PROJECT_DIR/venv"
        if [ ! -d "$VENV_DIR" ]; then
            echo "Creating virtual environment in $VENV_DIR..."
            virtualenv "$VENV_DIR"
        fi

        # Activate the virtual environment
        source "$VENV_DIR/bin/activate"
        echo "Virtual environment activated: $VENV_DIR"

        # Install project dependencies
        echo "Installing project dependencies..."
        pip install -r "$PROJECT_DIR/requirements.txt"

        echo "Configuration completed successfully!"