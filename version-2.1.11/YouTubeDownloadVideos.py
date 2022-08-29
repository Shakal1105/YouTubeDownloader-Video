from pytube import *
import time, threading
import os
from tkinter import Tk, Button
from tkinter.ttk import Progressbar

class A:
    def __init__(self):
        self.yt = YouTube("https://www.youtube.com/watch?v=8QHIkcacP8g")
        self.sizeyt= self.yt.streams.filter(resolution="720p", progressive=False)[0].filesize
        self.path= "D:/загрузки/"+str(self.yt.title.replace("|", "").replace(":","")) + ".mp4"
        td = threading.Thread(target=self.Threads,args=())
        td.start()
        root = Tk()
        Button(root, text="download", command=self.rhe).pack()
        self.progress = Progressbar(root, value=0, maximum=self.sizeyt, length=300)
        self.progress.pack()
        root.mainloop()
    def rhe(self):
        td = threading.Thread(target=self.download, args=())
        td.start()

    def download(self):
        self.yt.streams.filter(resolution="720p", progressive=False)[0].download("D:\загрузки")

    def Threads(self):
        try:
            print("non")
            timer=0
            maxtimer = self.sizeyt
            while True:
                self.progress["value"] = timer
                if timer >= maxtimer:
                    print("all")
                    break
                timer = os.path.getsize(self.path)
                print(timer, '/', maxtimer)
                time.sleep(1)
        except Exception:
            time.sleep(3)
            self.Threads()
            pass




A()
