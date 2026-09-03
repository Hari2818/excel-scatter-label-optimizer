**Excel Data Automation Pipeline using Python**

**Project Overview**

This project is an end-to-end Excel data automation pipeline developed using Python. It automates the process of downloading an Excel dataset from a GitHub repository, cleaning and validating the workbook, and uploading the processed Excel file to Microsoft SharePoint.

The pipeline reduces manual data-processing activities and provides a reusable workflow for handling Excel datasets.

****Project Objective****

The main objective of this project is to automate the complete Excel data-processing workflow:

Download the Excel dataset automatically.
Read and process all worksheets.
Validate data quality.
Remove duplicate and empty records.
Standardize column names.
Generate a cleaned Excel workbook.
Upload the cleaned workbook to SharePoint.
Maintain execution logs for monitoring and troubleshooting.

**Project Workflow**
GitHub Repository
       ↓
Selenium Web Automation
       ↓
Download Excel Dataset
       ↓
Pandas Data Processing
       ↓
Data Validation & Cleaning
       ↓
Cleaned Excel Workbook
       ↓
SharePoint Upload
       ↓
Automation Completed

**Technologies Used**
Python
Pandas
OpenPyXL
Selenium
WebDriver Manager
Microsoft SharePoint
Office365 REST Client
GitHub
Python Logging

**Project Structure**
**project/**

 **mainn.py**
      The main controller/orchestrator of the project. It runs the complete automation pipeline in sequence: download the Excel file → clean the data → upload the cleaned file to SharePoint.
      
 **website_automation.py**
      Handles automated downloading of the Excel dataset from GitHub using Selenium. It opens Chrome, navigates to the GitHub page, finds the Excel file, clicks View raw, and downloads the file.
      
 **data_processing.py**
      Handles Excel data cleaning and validation using Pandas. It processes every worksheet, checks missing values and duplicates, removes duplicate/empty rows, standardizes column names, and creates a cleaned Excel workbook.
        
 **sharepoint_upload.py**
      Handles uploading the cleaned Excel file to Microsoft SharePoint using Office365/SharePoint client libraries and client credentials.
      
 **AdventureWorks.xlsx**
      The input Excel dataset used by the pipeline. This is the original workbook that gets downloaded and processed.
 
 **Cleaned_AdventureWorks.xlsx**
      The output Excel workbook generated after data cleaning and validation. It contains the processed worksheets and is then uploaded to SharePoint. 
      
 **automation.log**
      The log file that records the execution status of the automation, such as successful operations and errors. The Python scripts configure logging to write to this file.

