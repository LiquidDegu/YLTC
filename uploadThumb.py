# pip install --upgrade google-auth
# pip install --upgrade google-auth-httplib2
# pip install --upgrade google-auth-oauthlib
# pip install --upgrade google-api-python-client


# https://developers.google.com/youtube/v3/docs/thumbnails/set?apix=true#params


import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import googleapiclient.errors
from googleapiclient.http import MediaFileUpload


VIDEO_ID = 'HCbLM3iIZfI'
thumbnail_path = '/Users/fabia/Desktop/Youtube API STREAM/Bild.jpg'
credentials_path = '/Users/fabia/Desktop/Youtube API STREAM/client_secret.json'
scopes = ['https://www.googleapis.com/auth/youtube.force-ssl']                      # https://developers.google.com/youtube/v3/guides/auth/installed-apps#identify-access-scopes


flow = InstalledAppFlow.from_client_secrets_file(credentials_path, scopes)        # Get credentials and create an API client
flow.run_local_server(host='localhost', port=8080)
credentials = flow.credentials

api_service_name = 'youtube'
api_version = 'v3'
youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

try:
    request = youtube.thumbnails().set(videoId=VIDEO_ID, media_body=MediaFileUpload(thumbnail_path))
    response = request.execute()
    print(response)
except Exception as ex:
    print(f'error: {ex}')
