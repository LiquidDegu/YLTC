from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *






def main1(*args):
    try:
        print(Ti.get())
        print(VideoID.get())
        print(Cred.get())
        print(":)")
    except ValueError:
        pass



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
Ti_entry.insert(0,"Set time interval")
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
