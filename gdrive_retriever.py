"""
Shows basic usage of the Drive v3 API.

Creates a Drive v3 API service and prints the names and ids of the last 10 files
the user has access to.
"""
from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import os

def get_video_from_gdrive(video_name):
    # Setup the Drive v3 API
    SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
            creds = tools.run_flow(flow, store)
    service = build('drive', 'v3', http=creds.authorize(Http()))

    results = service.files().list(q="name='{0}'".format(video_name)).execute()
    items = results.get('files', [])
    print(items[0]['id'], items[0]['name'])
    return

# def print_files_in_folder(service, folder_id):
#     """Print files belonging to a folder.

#     Args:
#         service: Drive API service instance.
#         folder_id: ID of the folder to print files from.
#     """
#     page_token = None
#     while True:
#         try:
#             param = {}
#             if page_token:
#                 param['pageToken'] = page_token
#             children = service.children().list(
#                     folderId=folder_id, **param).execute()

#             for child in children.get('items', []):
#                 print('File Id: %s' % child['id'])
#             page_token = children.get('nextPageToken')
#             if not page_token:
#                 break
#         except:
#             print('An error occurred!')
#             break

        # Call the Drive v3 API
        # while True:
        #     # results = service.files().list(
        #     #     pageSize=100, fields="nextPageToken, files(id, name)").execute()
        #     results = service.files().list(q="name='AD_Research_Videos'")
        #     items = results.get('files', [])
        #     for item in items:
        #         if item['name'] == "AD_Research_Videos":
        #             return item['id']

# from __future__ import print_function
# import httplib2
# import os

# from apiclient import discovery
# from oauth2client import client
# from oauth2client import tools
# from oauth2client.file import Storage
# from apiclient import *
# from apiclient.http import MediaFileUpload

# try:
#     import argparse
#     flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
# except ImportError:
#     flags = None

# # If modifying these scopes, delete your previously saved credentials
# # at ~/.credentials/drive-python-quickstart.json
# SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'
# CLIENT_SECRET_FILE = 'client_secret.json'
# APPLICATION_NAME = 'Drive API Python Quickstart'

# def get_credentials():
#     """Gets valid user credentials from storage.

#     If nothing has been stored, or if the stored credentials are invalid,
#     the OAuth2 flow is completed to obtain the new credentials.

#     Returns:
#         Credentials, the obtained credential.
#     """
#     home_dir = os.path.expanduser('~')
#     credential_dir = os.path.join(home_dir, '.credentials')
#     if not os.path.exists(credential_dir):
#         os.makedirs(credential_dir)
#     credential_path = os.path.join(credential_dir,
#                                    'drive-python-quickstart.json')

#     store = Storage(credential_path)
#     credentials = store.get()
#     if not credentials or credentials.invalid:
#         flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
#         flow.user_agent = APPLICATION_NAME
#         if flags:
#             credentials = tools.run_flow(flow, store, flags)
#         else: # Needed only for compatibility with Python 2.6
#             credentials = tools.run(flow, store)
#         print('Storing credentials to ' + credential_path)
#     return credentials

# def main():
#     """Shows basic usage of the Google Drive API.

#     Creates a Google Drive API service object and outputs the names and IDs
#     for up to 10 files.
#     """
#     credentials = get_credentials()
#     http = credentials.authorize(httplib2.Http())
#     service = discovery.build('drive', 'v3', http=http)
        
#     file_metadata = {'name': 'driving2.mp4'}
#     media = MediaFileUpload('frontend/driving2.mp4',
#                             mimetype='video/mp4')
#     file = service.files().create(body=file_metadata,
#                                         media_body=media,
#                                         fields='id').execute()
#     print('File ID: %s' % file.get('id'))

# #    results = service.files().list(
# #        pageSize=10,fields="nextPageToken, files(id, name)").execute()
# #    items = results.get('files', [])
# #    if not items:
# #        print('No files found.')
# #    else:
# #        print('Files:')
# #        for item in items:
# #            print('{0} ({1})'.format(item['name'], item['id']))

# if __name__ == '__main__':
#     main()