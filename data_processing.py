import pandas as pd
import logging


# ---------------------------------
# Logging Configuration
# ---------------------------------
logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def clean_data(input_file, output_file):
    """
    Reads the Excel workbook, validates the data,
    cleans every sheet and saves a new workbook.
    """

    try:

        logging.info("Data Cleaning Started")

        excel_file = pd.ExcelFile(input_file)

        print("Workbook Loaded Successfully.")
        logging.info("Workbook Loaded Successfully.")

        print("Available Sheets:")
        print(excel_file.sheet_names)

        cleaned_sheets = {}

        
        # Process Every Sheet

        for sheet in excel_file.sheet_names:

            print("\n" + "=" * 50)
            print(f"Processing Sheet : {sheet}")

            df = pd.read_excel(excel_file, sheet_name=sheet)

            print("Rows :", df.shape[0])
            print("Columns :", df.shape[1])

            
            # Validation
            
            print("\nMissing Values")
            print(df.isnull().sum())

            print("\nDuplicate Rows :", df.duplicated().sum())

            # Check SalesOrderLineKey only if it exists
            if "SalesOrderLineKey" in df.columns:
                print(
                    "SalesOrderLineKey Unique :",
                    df["SalesOrderLineKey"].is_unique
                )

            
            # Cleaning

            df.drop_duplicates(inplace=True)

            df.dropna(how="all", inplace=True)

            df.columns = df.columns.str.strip()

            df.columns = df.columns.str.replace(" ", "_")

            # Blank value check
            if "Sales_Order" in df.columns:
                print(
                    "Blank Sales_Order :",
                    (df["Sales_Order"].astype(str).str.strip() == "").sum()
                )

            if "Sales_Order_Line" in df.columns:
                print(
                    "Blank Sales_Order_Line :",
                    (df["Sales_Order_Line"].astype(str).str.strip() == "").sum()
                )

            cleaned_sheets[sheet] = df

            logging.info(f"{sheet} cleaned successfully.")

        
        # Save Clean Workbook

        with pd.ExcelWriter(output_file, engine="openpyxl") as writer:

            for sheet, data in cleaned_sheets.items():
                data.to_excel(
                    writer,
                    sheet_name=sheet,
                    index=False
                )

        print("\nCleaned workbook created successfully.")
        logging.info("Workbook cleaned successfully.")

    except Exception as e:

        print("ERROR :", e)
        logging.error(f"Data Cleaning Failed : {e}")



# Test the Script

if __name__ == "__main__":

    clean_data(
        "AdventureWorks.xlsx",
        "Cleaned_AdventureWorks.xlsx"
    )