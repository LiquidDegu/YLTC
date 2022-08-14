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
import numpy as np
import cv2
from cv2 import VideoCapture
from cv2 import imshow
from cv2 import imwrite
import time
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
from vidgear.gears import CamGear


a = np.array(2)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#API startup



def main1(*args):
    try:


        VIDEO_ID = VideoID.get()
        thumbnail_path = 'thumbnail.png'
        credentials_path = Cred.get()
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

    except:
        print("Error with Api startup")

        #----------------------------------------------------------------------------------------------------------------------
        #Kamera startup
    #try:
      #  cam = VideoCapture(1, cv2.CAP_DSHOW)                                                       Turned off for now (working on grabbing it directly via YT)

      #  cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
      #  cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


      #  r, img = cam.read()
           
      

    #except:
        #print("Error with Camera startup")

        #Camera function for tests
        #if r:
        #
        #    imshow("Test", img)
        #    imwrite("Test.png", img)
        #else:
        #    print("No image")












        #-----------------------------------------------------------------------------------------------------------------------------------
        #Main camera and API function

    
    try:


        i=1
        while i == 1:

            #print(int(Ti.get()))

            #r, img = cam.read()   
            # Turned off for now (implementing getting if from YT directly)                                                                                                      #take Photo


            time.sleep(int(Ti.get()))                                                                                                              #sleep for x Sec.

            stream = CamGear(
                source="https://youtu.be/4KjavYG_AEI", #YT URL
                stream_mode=True,
                logging=True 
                            ).start()
    
            time.sleep(1)
            img = stream.read()
    
            if img is None:
                print("Error with getting img")
            else:
                cv2.imwrite("thumbnail.png", img) 
                print("imwrite")
        
            stream.stop() 

                






            #if r:
            #        
            #cv2.imwrite("thumbnail.png", img)                                                                                           #save photo
            #                print("taking picture")
            #else:
            #    print("No image")

            time.sleep(5)                                                                                                               #sleep for x Sec.

            try:                                                                                                                        #Api Upload
                print("initialisiere API call")
                request = youtube.thumbnails().set(videoId=VIDEO_ID, media_body=MediaFileUpload(thumbnail_path))
                response = request.execute()
                print(response)
            except Exception as ex:
                print(f'error: {ex}')

    except:
        print("Error API call")
    




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