# Fake Fuel Bill Generator Automation

An automated tool that generates sample fuel bills using Selenium WebDriver. This project automates interactions with
freeforonline.com's fuel bill generator service to create multiple sample bills with customizable parameters.

## ⚠️ Disclaimer

This tool is intended for **testing and educational purposes only**. Do not use this for creating fraudulent documents
or any illegal activities. Users are responsible for ensuring compliance with all applicable laws and regulations.

## Features

- Automated generation of multiple fuel bills
- Customizable bill parameters including:
    - Fuel rates (94.55-94.77)
    - Purchase amounts
    - Time ranges (9 AM - 11 AM)
    - Date ranges (2022-2024)
    - Custom receipt numbers
- Automatic PDF downloads
- Configurable customer details
- Detailed logging system

## Prerequisites

- Python 3.7+
- Google Chrome browser
- Internet connection

## Installation

1. Clone the repository:

```bash
git clone https://github.com/chanpreet3000/fake-fuel-bill-generator-automation
cd fake-fuel-bill-generator-automation
```

2. Run the setup script:

```bash
# Windows
setup.bat

# Unix/Linux
chmod +x setup.sh
./setup.sh
```

## Configuration

Edit `config.py` to customize bill generation parameters:

- `NAME`: Customer name
- `VEHICLE_NUMBER`: Vehicle registration number
- `FUEL_STATION_NAME`: Name of the fuel station
- `FUEL_RATE`: Range of fuel rates
- `FS_AMOUNT`: List of possible fuel purchase amounts
- Date and time ranges for bill generation

## Usage

Run the application using the provided script:

```bash
# Windows
run.bat

# Unix/Linux
./run.sh
```

The script will prompt you for the number of bills to generate. Generated PDFs will be saved in the `./data` directory.

## Project Structure

```
fake-fuel-bill-generator-automation/
├── config.py           # Configuration parameters
├── main.py            # Main script
├── Logger.py          # Logging functionality
├── data/              # Generated PDFs directory
├── logs/              # Log files
├── requirements.txt   # Python dependencies
├── setup.sh           # Unix setup script
├── setup.bat          # Windows setup script
├── run.sh             # Unix run script
└── run.bat            # Windows run script
```

## Logging

The application uses a custom logging system that saves detailed logs in the `./logs` directory. Logs include:

- Info level: General operation progress
- Debug level: Detailed operation information
- Critical level: Error messages and exceptions

## License

This project is distributed under the MIT License. See `LICENSE` file for more information.

## Support

For additional support or issues, please open an issue in the repository.