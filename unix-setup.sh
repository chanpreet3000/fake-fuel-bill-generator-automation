#!/usr/bin/env bash
echo "Setting up the project..."

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null
then
    echo "Python 3 is not installed. Please install Python 3 and try again."
    read -p "Press any key to continue..."
    exit 1
fi

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install requirements
echo "Installing requirements..."
pip3 install -r requirements.txt

echo "Setup complete. You can now run the project using the run_project.sh script."
read -p "Press any key to continue..."