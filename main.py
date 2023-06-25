# from google.oauth2 import service_account


# # Load credentials
# credentials = service_account.Credentials.from_service_account_file('test-firebase-bd65c-3f0f3b5f859b.json', scopes=['https://www.googleapis.com/auth/drive'])
# 
# # Create the Drive API service
# service = build('drive', 'v3', credentials=credentials)
# # Retrieve the list of files
# results = service.files().list(pageSize=1000).execute()
# files = results.get('files', [])
# 
# # Get the count of files
# file_count = len(files)
# print("Number of files in Google Drive:", file_count)
# # Retrieve the Drive ID
# drive_id = '17nD2YFRXaGSfo72RmUhbB7t3EVF4cr-B'  # Replace with the desired Drive ID
# 
# # Retrieve the list of files in the specified Drive ID
# results = service.files().list(driveId=drive_id, pageSize=1000, includeItemsFromAllDrives=True).execute()
# files = results.get('files', [])

# Get the count of files
# file_count = len(files)
# print("Number of files in Drive ID:", file_count)

from Google import Create_Service
import pandas as pd
CLIENT_SECRET_FILE = 'client_secret_856867123910-38eakn00pfrma9cogq66r816g2ob6gb1.apps.googleusercontent.com.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
folder_id = '17nD2YFRXaGSfo72RmUhbB7t3EVF4cr-B'

query = f"parents = '{folder_id}'"
response = service.files().list(q=query).execute()
files = response.get('files')
nextPageToken = response.get('nextPageToken')

while nextPageToken:
    response = service.files().list(q=query).execute()
    files.extend(response.get('files'))
    nextPageToken = response.get('nextPageToken')
df = pd.DataFrame(files)
print(df)
