from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.client_credential import ClientCredential

SITE_URL = " "
CLIENT_ID = " "
CLIENT_SECRET = " "

ctx = ClientContext(SITE_URL).with_credentials(
    ClientCredential(CLIENT_ID, CLIENT_SECRET)
)

folder = ctx.web.get_folder_by_server_relative_url("Shared Documents")

with open("Cleaned_AdventureWorks.xlsx", "rb") as file:
    folder.upload_file(
        "Cleaned_AdventureWorks.xlsx",
        file.read()
    ).execute_query()

print("File uploaded successfully.")