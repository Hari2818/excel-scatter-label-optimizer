from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import os
import time


# Logging Configuration

logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def download_dataset():

    download_folder = os.getcwd()

    chrome_options = webdriver.ChromeOptions()

    prefs = {
        "download.default_directory": download_folder,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }

    chrome_options.add_experimental_option("prefs", prefs)

    driver = None

    try:

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )

        wait = WebDriverWait(driver, 20)

        driver.maximize_window()

        print("Chrome launched.")
        logging.info("Chrome launched.")

        
        # Step 1 : Open GitHub Repository

        url = "https://github.com/microsoft/powerbi-desktop-samples/tree/main/AdventureWorks%20Sales%20Sample"

        driver.get(url)

        print("GitHub page opened.")
        logging.info("GitHub page opened.")

        
        # Step 2 : Click Excel File
        excel_file = wait.until(
            EC.element_to_be_clickable(
                (
                    By.PARTIAL_LINK_TEXT,
                    "AdventureWorks Sales.xlsx"
                )
            )
        )

        driver.execute_script("arguments[0].scrollIntoView(true);", excel_file)
        time.sleep(2)

        driver.execute_script("arguments[0].click();", excel_file)

        print("Excel file page opened.")
        logging.info("Excel file page opened.")

        
        # Step 3 : Wait for View Raw

        wait.until(
            EC.presence_of_element_located(
                (
                    By.LINK_TEXT,
                    "View raw"
                )
            )
        )

        raw_link = wait.until(
            EC.element_to_be_clickable(
                (
                    By.LINK_TEXT,
                    "View raw"
                )
            )
        )

        driver.execute_script("arguments[0].scrollIntoView(true);", raw_link)
        time.sleep(2)

        driver.execute_script("arguments[0].click();", raw_link)

        print("Download started.")
        logging.info("Download started.")

        # Wait for download
        time.sleep(10)

        print("Download completed.")
        logging.info("Download completed.")

    except Exception as e:

        print("ERROR:", e)
        logging.error(f"Website automation failed: {e}")

        input("Press Enter to continue...")

    finally:

        if driver:
            driver.quit()

        print("Browser closed.")
        logging.info("Browser closed.")


if __name__ == "__main__":
    download_dataset()