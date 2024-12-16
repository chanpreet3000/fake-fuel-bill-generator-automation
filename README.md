# Fake Fuel Bill Generator Automation

An automated tool that generates sample fuel bills using Selenium WebDriver. This project automates interactions with
freeforonline.com's fuel bill generator service to create multiple sample bills with customizable parameters.

## ⚠️ Disclaimer

This tool is intended for **testing and educational purposes only**. Do not use this for creating fraudulent documents
or any illegal activities. Users are responsible for ensuring compliance with all applicable laws and regulations.

## Features

- Automated generation of multiple fuel bills
- Customizable bill parameters
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
Just double click on the win-setup.bat file 

# Unix/Linux
chmod +x unix-setup.sh
./unix-setup.sh
```

## Configuration

The configuration parameters are defined in the `config.py` file. You can customize the following:

- `CUSTOMER_NAME`: Customer name
- `VEHICLE_NUMBER`: Vehicle registration number
- `FUEL_STATION_NAME`: Name of the fuel station
- `FUEL_RATE`: Range of fuel rates
- `FUEL_PURCHASE_AMOUNTS`: List of possible fuel purchase amounts
- `FUEL_PURCHASE_HOUR`: Possible hours of purchase time (9 AM to 11 AM)
- `FUEL_PURCHASE_MINUTE`: Possible minutes of purchase time (0 to 59)
- `RECEIPT_NUMBER_RANGE`: Range for generating random receipt numbers (1000 to 9999)
- `FUEL_BILL_START_DATE`: Starting date for fuel bills (format: DD:MM:YYYY)

## Usage

Run the application using the provided script:

```bash
# Windows
Double click on the win-run.bat file

# Unix/Linux
chmod +x unix-run.sh
./unix-run.sh
```

The script will prompt you for the number of bills to generate. Generated PDFs will be saved in the `./data` directory.

## Project Structure

```
fake-fuel-bill-generator-automation/
├── config.py          # Configuration parameters
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

## License

This project is distributed under the MIT License. See [LICENSE](LICENSE) file for more information.
