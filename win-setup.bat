@echo off
echo Setting up the project...

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python and try again.
    pause
    exit /b 1
)

REM Create virtual environment
echo Creating virtual environment...
python -m venv .venv

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Install requirements
echo Installing requirements...
pip install -r requirements.txt

echo Setup complete. You can now run the project using run_project.bat
pause