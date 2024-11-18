from typing import List


def frange(start: float, stop: float, step: float) -> List[float]:
    values = []
    while start <= stop:
        values.append(round(start, 2))
        start += step
    return values


# Customer's name (for the fake bill)
NAME = 'Chanpreet'
# Vehicle number for the fake fuel bill
VEHICLE_NUMBER = 'DLTEMPTEMP'
# Fuel station name (used as a constant in the fake bill generator)
FUEL_STATION_NAME = 'Bharat Petroleum Petrol Pump - Jawala Service Station'

# List of possible fuel rates in the range of 94.55 to 94.77 with 0.01 increments
FUEL_RATE = frange(94.55, 94.77, 0.01)
# List of example fuel purchase amounts in currency (e.g., rupees)
FS_AMOUNT = ['3300', '2900']
# Possible hours of purchase time (9 AM to 11 AM)
FUEL_TIME_HOUR = [9, 10, 11]
# Possible minutes of purchase time (0 to 59)
FUEL_TIME_MIN = list(range(0, 60, 1))
# Range for generating random receipt numbers (1000 to 9999)
RECEIPT_NUMBER = list(range(1000, 9999, 1))
# Starting date for fuel bills (format: DD:MM:YYYY)
FUEL_DATE = "26:11:2024"
