#!/bin/bash
echo "Setting up the project..."

# Check if Python is installed
if ! command -v python &> /dev/null
then
    echo "Python is not installed. Please install Python and try again."
    read -p "Press any key to continue..."
    exit 1
fi

# Create virtual environment
echo "Creating virtual environment..."
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt

echo "Setup complete. You can now run the project using the run_project.sh script."
read -p "Press any key to continue..."
