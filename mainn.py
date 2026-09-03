from website_automation import download_dataset
from data_processing import clean_data
from sharepoint_upload import upload_to_sharepoint

INPUT_FILE = "AdventureWorks.xlsx"
OUTPUT_FILE = "Cleaned_AdventureWorks.xlsx"

print("Starting Automation Pipeline...")

# Step 1 - Download dataset
download_dataset()

# Step 2 - Clean dataset
clean_data(INPUT_FILE, OUTPUT_FILE)

# Step 3 - Upload to SharePoint
upload_to_sharepoint(OUTPUT_FILE)

print("Pipeline Completed Successfully!")