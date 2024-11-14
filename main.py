from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from config import FS_AMOUNT, FUEL_RATE, FUEL_STATION_NAME, NAME, RECEIPT_NUMBER, VEHICLE_NUMBER, FUEL_TIME_HOUR, \
    FUEL_TIME_MIN, FUEL_DATE_DAY, FUEL_DATE_MONTH, FUEL_DATE_YEAR
from Logger import Logger
import time
import random
import os


def generate_fuel_bill(num_bills: int = 1):
    Logger.info("Starting fuel bill generation process")
    driver = None
    try:
        os.makedirs("./data", exist_ok=True)
        Logger.debug("Created or verified data directory at ./data")

        download_path = os.path.abspath("./data")

        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")

        prefs = {
            "download.default_directory": download_path,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
            "plugins.always_open_pdf_externally": True
        }
        chrome_options.add_experimental_option("prefs", prefs)
        Logger.info("Initializing Chrome WebDriver")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        Logger.info("Navigating to fuel bill generator website")
        driver.get("https://freeforonline.com/fuel-bills/index.html")
        time.sleep(7)

        Logger.debug("Selecting template-1")
        template = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "template-1"))
        )
        driver.execute_script("arguments[0].click();", template)
        time.sleep(2)

        for i in range(num_bills):
            Logger.info(f"Generating bill {i + 1} of {num_bills}")

            fields = {
                "fs-station-name": FUEL_STATION_NAME,
                "fs-fuel-rate": random.choice(FUEL_RATE),
                "fs-amount": random.choice(FS_AMOUNT),
                "fs-date": f"{random.choice(FUEL_DATE_DAY)}:{random.choice(FUEL_DATE_MONTH)}:{random.choice(FUEL_DATE_YEAR)}",
                "fs-time": f"{random.choice(FUEL_TIME_HOUR)}:{random.choice(FUEL_TIME_MIN)}:AM",
                "u-name": NAME,
                "u-vechicle-number": VEHICLE_NUMBER,
                "fs-receipt-number": random.choice(RECEIPT_NUMBER)
            }
            Logger.debug("Preparing to fill form fields", details=fields)

            for field_id, value in fields.items():
                Logger.debug(f"Filling field: {field_id} with value: {value}")
                element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, field_id))
                )
                element.clear()
                element.send_keys(value)

            time.sleep(2)
            Logger.info("Initiating bill download")
            download_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "download-fuel-bills"))
            )
            driver.execute_script("arguments[0].click();", download_button)
            Logger.debug("Download button clicked")

            time.sleep(3)

        Logger.info("Bill generation and download completed successfully")

    finally:
        if driver:
            Logger.debug("Closing WebDriver")
            driver.quit()


if __name__ == "__main__":
    try:
        num_bills = int(input("Enter the number of fuel bills to generate: "))
        generate_fuel_bill(num_bills)
    except Exception as e:
        Logger.critical("Something went wrong", e)
    finally:
        Logger.info("Application execution completed")
