#test 
# https://developers.google.com/youtube/v3
# https://developers.google.com/youtube/v3/docs/thumbnails/set
# https://developers.google.com/youtube/v3/getting-started
# 10000 units per day / 50 per Change               200 per Day [every 2 minutes?!?]





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
import cv2
from cv2 import VideoCapture
from cv2 import imshow
from cv2 import imwrite
import time
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#API startup



def main1(*args):
    try:


        VIDEO_ID = 'VideoID'
        thumbnail_path = '/Users/fabia/Desktop/Youtube API STREAM/Youtube-Livestream/thumbnail.png'
        credentials_path = '/Users/fabia/Desktop/Youtube API STREAM/client_secret.json'
        scopes = ['https://www.googleapis.com/auth/youtube.force-ssl']                      # https://developers.google.com/youtube/v3/guides/auth/installed-apps#identify-access-scopes


        flow = InstalledAppFlow.from_client_secrets_file(credentials_path, scopes)        # Get credentials and create an API client
        flow.run_local_server(host='localhost', port=8080)
        credentials = flow.credentials

        api_service_name = 'youtube'
        api_version = 'v3'
        youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

#try:                                                                                                                        #Api Upload for tests
#    request = youtube.thumbnails().set(videoId=VIDEO_ID, media_body=MediaFileUpload(thumbnail_path))
#    response = request.execute()
#    print(response)
#except Exception as ex:
#    print(f'error: {ex}')



#----------------------------------------------------------------------------------------------------------------------
#Kamera startup

        cam = VideoCapture(1, cv2.CAP_DSHOW)

        cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


        r, img = cam.read()



#Camera function for tests
#if r:
#
#    imshow("Test", img)
#    imwrite("Test.png", img)
#else:
#    print("No image")












#-----------------------------------------------------------------------------------------------------------------------------------
#Main camera and API function

        time.sleep(20)


        i=1
        while i == 1:


            r, img = cam.read()                                                                                                         #take Photo

            time.sleep(12)                                                                                                              #sleep for x Sec.

            if r:

                imwrite("thumbnail.png", img)                                                                                           #save photo
#                print("taking picture")
            else:
                print("No image")

            time.sleep(5)                                                                                                               #sleep for x Sec.

            try:                                                                                                                        #Api Upload
                print("initialisiere API call")
                request = youtube.thumbnails().set(videoId=VIDEO_ID, media_body=MediaFileUpload(thumbnail_path))
                response = request.execute()
                print(response)
            except Exception as ex:
                print(f'error: {ex}')

    except:
        print("Error in main1")




def stop(*args):
    try:
        i = 2
    except:
        print("Error in the Stop function")

















root = Tk()
root.title("Thumbnail Changer")

 



mainframe = ttk.Frame(root, padding="3 3 15 15")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

Ti = StringVar()
Ti_entry = ttk.Entry(mainframe, width=14, textvariable=Ti)
Ti_entry.insert(0,"Set time Inervall")
Ti_entry.grid(column=3, row=1, sticky=(W,E))



ttk.Button(mainframe, text="Start", command=main1).grid(column=3, row=3, sticky=E)
ttk.Button(mainframe, text="Stop", command=stop).grid(column=1, row=3, sticky=W)




VideoID = StringVar()
VideoID_entry = ttk.Entry(mainframe, width=14, textvariable=VideoID)
VideoID_entry.insert(0, "Video ID")
VideoID_entry.grid(column=1, row=1, sticky=(N,W))



Cred = StringVar()
Cred_entry = ttk.Entry(mainframe, width=20, textvariable=Cred)
Cred_entry.grid(column=1, row=2, sticky=(S,W))
def browsefunc():
    filename =askopenfilename(filetypes=(("json files","*.json"),("All files","*.*")))
    Cred_entry.insert(0, filename)
ttk.Button(mainframe, text="Browse Files", command=browsefunc).grid(column=2, row=2)




# Polish (CSS)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
VideoID_entry.focus()


root.mainloop()