import io,os, tkinter.filedialog, time, urllib.request
from threading import Thread
from pytube import *
from tkinter import *
from tkinter.ttk import Combobox, Progressbar
from tkinter import messagebox
from PIL import Image, ImageTk

class YouTubeDownloader:
    def __init__(self):
        self.colors = ["white", "black", "#F2F3F4"]
        self.spisok_katshestva = []
        self.spisok_katshestva1 = ["1080p", "720p", "2048p"]
        self.sound=True
        self.video=""
        self.chpath = "C:/загрузки"
        self.zvyk = 0
        self.UIapp()

    def darkmode(self):
        self.appwindow.config(bg=self.colors[1])
        self.lab["bg"] = self.colors[1]
        self.lab["fg"] = self.colors[0]
        self.search["fg"] = self.colors[0]
        self.search["bg"] = self.colors[1]
        self.urlgetter["bg"] = self.colors[1]
        self.urlgetter["fg"] = self.colors[0]
        self.namevideo["fg"] = self.colors[0]
        self.withsong["fg"] = self.colors[0]
        self.nosound["fg"] = self.colors[0]
        self.namevideo["bg"] = self.colors[1]
        self.withsong["bg"] = self.colors[1]
        self.nosound["bg"] = self.colors[1]
        self.progresslab['bg']= self.colors[1]
        self.progresslab["fg"]=self.colors[0]
        self.pathentry["bg"] = self.colors[1]

    def lightmode(self):
        self.appwindow.config(bg=self.colors[2])
        self.lab["bg"] = self.colors[0]
        self.lab["fg"] = self.colors[1]
        self.search["fg"] = self.colors[1]
        self.search["bg"] = self.colors[0]
        self.urlgetter["bg"] = self.colors[0]
        self.urlgetter["fg"] = self.colors[1]
        self.namevideo["fg"] = self.colors[1]
        self.withsong["fg"] = self.colors[1]
        self.nosound["fg"] = self.colors[1]
        self.namevideo["bg"] = self.colors[0]
        self.withsong["bg"] = self.colors[0]
        self.nosound["bg"] = self.colors[0]
        self.progresslab['bg'] = self.colors[0]
        self.progresslab["fg"] = self.colors[1]
        self.pathentry["bg"] = self.colors[0]

    def setting(self):
        self.video = YouTube(self.urlgetter.get())
        self.namevideo["text"] = str(self.video.title)
        self.rawdata= urllib.request.urlopen(self.video.thumbnail_url).read()
        self.im = Image.open(io.BytesIO(self.rawdata)).resize((300, 150), Image.LANCZOS)
        self.image= ImageTk.PhotoImage(self.im)
        self.a["image"]=self.image
        self.filesize = self.video.streams.filter(res=self.hd.get(), progressive=self.sound, file_extension='mp4')[-1].filesize
        if self.chpath == "C:/" or self.chpath == "D:/" or len(self.chpath) == 3:
            self.pathfile = self.chpath + self.video.title.replace(",","").replace("|", "").replace(":", "").replace("#","").replace(".", "").replace("*","").replace("$","").replace("%","").replace("'","").replace("^","").replace("~", "").replace('"',"").replace("\ ".replace(" ", ""),"").replace("?","").replace("/","") + '.mp4'
        else:
            self.pathfile = self.chpath + '/' + self.video.title.replace(",","").replace("|", "").replace(":", "").replace("#","").replace(".", "").replace("*","").replace("$","").replace("%","").replace("'","").replace("^","").replace("~", "").replace('"',"").replace("\ ".replace(" ", ""),"").replace("?","").replace("/","") + '.mp4'
        self.spisok_katshestva = []
        for res in self.video.streams.filter(file_extension="mp4", progressive=True):
            self.spisok_katshestva.append(res.resolution)
        self.withsong["state"] = "normal"
        self.nosound["state"] = "normal"
        self.hd["values"]=self.spisok_katshestva
        self.hd["state"] = "normal"
        self.hd1["state"] = "normal"
        self.hd.current(1)
        self.hd1.current(0)

    def path(self):
        self.chpath = tkinter.filedialog.askdirectory(title="Папка для зберігання. Слава Україні!!!")
        self.pathentry["text"] = self.chpath
        if len(str(self.video)) > 1:
            if self.chpath == "C:/" or self.chpath == "D:/" or len(self.chpath) == 3:
                self.pathfile = self.chpath + self.video.title.replace(",","").replace("|", "").replace(":", "").replace("#","").replace(".", "").replace("*","").replace("$","").replace("%","").replace("'","").replace("^","").replace("~", "").replace('"',"").replace("\ ".replace(" ", ""),"").replace("?","").replace("/","") + '.mp4'
            else:
                self.pathfile = self.chpath + '/' + self.video.title.replace(",","").replace("|", "").replace(":", "").replace("#","").replace(".", "").replace("*","").replace("$","").replace("%","").replace("'","").replace("^","").replace("~", "").replace('"',"").replace("\ ".replace(" ", ""),"").replace("?","").replace("/","") + '.mp4'

    def previev(self):
        potok = Thread(target=self.setting, args=())
        potok.start()

    def download(self, num):
        self.hd["state"]="disabled"
        self.hd1["state"]="disabled"
        self.nosound["state"]="disabled"
        self.withsong["state"]="disabled"
        self.urlgetter["state"]="disabled"
        def n():
            try:
                self.video.streams.filter(resolution=self.hd1.get(), progressive=False, file_extension="mp4")[0].download(self.chpath)
                self.text='succes'
            except Exception:
                self.text = ''
                messagebox.showwarning(title="Не знайдено файлів", message="Відео такої якості не має на сервері YouTube для завантаження спробуйте 720p або інші.")

        if num == 11:
            self.video.streams.filter(resolution=self.hd.get(), progressive=self.sound, file_extension="mp4")[0].download(self.chpath)
            self.text = 'succes'
        elif num == 12:
            try:
                self.video.streams.filter(resolution=self.hd1.get(), progressive=False, file_extension="mp4")[1].download(self.chpath)
                self.text = 'succes'
            except IndexError:
                n()
        if self.text == "succes":
            messagebox.showinfo(title="SUCCES", message="Завантаження завершено. Насолоджуйтесь переглядом")
            self.text = " "
            self.urlgetter["state"] = "normal"
            self.progress["value"] = 0

    def progressbar(self):
        try:
            time.sleep(0.5)
            self.value = 0
            if self.hd.get() == "720p":
                self.filesize = self.video.streams.filter(res=self.hd.get(), progressive=self.sound, file_extension='mp4')[-1].filesize
            else:
                self.filesize = self.video.streams.filter(res=self.hd.get(), progressive=self.sound, file_extension='mp4')[0].filesize
            maximum = self.filesize
            self.progress["maximum"]=maximum
            while True:
                self.value=os.path.getsize(self.pathfile)
                self.progress["value"]=self.value
                self.progresslab["text"]="{:.2f} mb/{:.2f} mb".format(self.value/1024**2, maximum/1024**2)
                if self.value >= maximum:
                    self.progresslab["text"] = "{:.2f} mb/{:.2f} mb".format(maximum / 1024 ** 2, maximum / 1024 ** 2)
                    break
                time.sleep(0.3)
        except Exception as e:
            time.sleep(1)
            print(e)
            self.progressbar()

    def threads(self, num):
        self.potok = Thread(target=lambda : self.download(num=num), args=(), daemon=True)
        self.potok.start()
        self.potoktimer = Thread(target=self.progressbar, args=(), daemon=True)
        self.potoktimer.start()

    def UIapp(self):
        self.appwindow = Tk()
        self.appwindow.title("YouTube DOWNLOADER VIDEO (MADE iN Ukraine)")
        self.x = (self.appwindow.winfo_screenwidth() - self.appwindow.winfo_reqwidth()) / 4
        self.y = (self.appwindow.winfo_screenheight() - self.appwindow.winfo_reqheight()) / 2
        self.appwindow.wm_geometry("+%d+%d" % (self.x, self.y))
        ########################MENUBAR######################################
        self.menubar = Menu(self.appwindow, fg='white', bg="black")

        self.settings = Menu(self.menubar, tearoff=0, fg=self.colors[1], bg=self.colors[0])
        self.menubar.add_cascade(label="Settings", menu=self.settings)
        self.mode = Menu(self.settings, tearoff=0, fg=self.colors[1], bg=self.colors[0])
        self.mode.add_radiobutton(label='Dark', command=self.darkmode, selectcolor=self.colors[1])
        self.mode.add_radiobutton(label='Light', command=self.lightmode, selectcolor=self.colors[1])
        self.settings.add_cascade(label="Mode", menu=self.mode)
        ################################youTUBE############################
        self.lab = Label(self.appwindow, text="Вставте посилання на ютуб відео", bg=self.colors[0], fg=self.colors[1])
        self.lab.grid(columnspan=3, row=1)
        self.urlgetter = Entry(self.appwindow, width=100)
        self.urlgetter.grid(columnspan=3, row=2)
        self.search = Button(self.appwindow, text="Шукати", bg=self.colors[0], fg=self.colors[1], command=self.previev)
        self.search.grid(row=2, column=4)

        self.hd = Combobox(self.appwindow, values=self.spisok_katshestva, width=5, state="disabled")
        self.hd.grid(row=3, column=3)
        self.hd1 = Combobox(self.appwindow, values=self.spisok_katshestva1, width=5, state="disabled")
        self.hd1.grid(row=4, column=3)
        self.namevideo = Label(self.appwindow, text=" ", fg=self.colors[1], bg=self.colors[0])
        self.namevideo.grid(row=3, columnspan=2)
        self.withsong= Button(self.appwindow, text="Завантажити зі звуком", state="disabled", command=lambda : self.threads(num=11), fg=self.colors[1], bg=self.colors[0])
        self.withsong.grid(row=3, column=4)
        self.nosound = Button(self.appwindow, text="Завантажити без звуку", state="disabled", command=lambda : self.threads(num=12), fg=self.colors[1], bg=self.colors[0])
        self.nosound.grid(row=4, column=4)
        self.a = Label(self.appwindow)
        self.a.grid(row=5, columnspan=2)

        s= tkinter.ttk.Style()
        s.theme_use("clam")
        s.configure("#7FFF00.Horizontal.TProgressbar", foreground="#7FFF00", background="#7FFF00")
        self.progress = Progressbar(self.appwindow,style="#7FFF00.Horizontal.TProgressbar", orient="horizontal", value=0, maximum=100, length=400)
        self.progress.grid(row=6, columnspan=2, padx=40)
        self.progresslab = Label(self.appwindow, text="0/0", fg=self.colors[1], bg=self.colors[0])
        self.progresslab.grid(row=6,column=2)

        self.pathentry = Label(self.appwindow, text=self.chpath, bg='white', fg="red")
        self.pathentry.grid(row=0, columnspan=3)
        Button(self.appwindow, text="Шлях...", bg="yellow", fg="red", command=self.path).grid(row=0, column=3)
        ################################CONFIGSRUNNER######################
        self.appwindow.configure(bg=self.colors[2], menu=self.menubar, highlightcolor='red')
        self.appwindow.mainloop()


if __name__ == "__main__":
    def setting(a):
        if a == 1:
            appwindow.quit()
        elif a == 2:
            appwindow.destroy()
            YouTubeDownloader()
    appwindow = Tk()
    appwindow.wm_title("Config_Window(Зроблено в Україні)")
    appwindow.geometry("300x160")
    appwindow.resizable(width=True, height=True)
    x = (appwindow.winfo_screenwidth() - appwindow.winfo_reqwidth()) / 2
    y = (appwindow.winfo_screenheight() - appwindow.winfo_reqheight()) / 2
    appwindow.wm_geometry("+%d+%d" % (x,y))
    appwindow.configure(bg="#85C1E9")

    Label(appwindow, text="Слава Україні - Героям слава", fg = "Yellow", bg="Blue", width=300, font="TimesNewRoman").pack()
    Label(appwindow, text="Glory to Ukraine - Hero Glory", fg = "Blue", bg="Yellow", width=300, font="TimesNewRoman").pack()

    Label(appwindow, text="Завантажуй з Ютуб безкоштовно\n використовуй англійську розкладку", bg="#85C1E9").pack()
    Button(appwindow, text="Почати", command=lambda: setting(a=2)).pack()
    Button(appwindow, text="Вийти", command=lambda: setting(a=1)).pack()

    appwindow.mainloop()
