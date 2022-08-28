import os
import tkinter.filedialog
from pytube import *
from tkinter import *
from tkinter.ttk import Combobox, Progressbar
from tkinter import messagebox


class YouTubeDownloader:
    def __init__(self):
        self.colors = ["white", "black", "#F2F3F4"]
        self.spisok_katshestva = []
        self.spisok_katshestva1 = ["1080p", "720p", "2048p"]
        self.sound=True
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

    def setting(self):
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

    def previev(self):
        self.video = YouTube(self.urlgetter.get())
        self.namevideo["text"] = str(self.video.title)
        self.setting()

    def download(self, num):
        def n():
            try:
                self.video.streams.filter(resolution=self.hd1.get(), progressive=False, file_extension="mp4")[0].download(path)
                self.text='succes'
            except Exception:
                self.text = ''
                messagebox.showwarning(title="Не знайдено файлів", message="Відео такої якості не має на сервері YouTube для завантаження спробуйте 720p або інші.")
        path = tkinter.filedialog.askdirectory(title="Папка для зберігання. Слава Україні!!!")
        self.pathfile = path+'/'+self.video.title.replace("|", "").replace(":","")+'.mp4'
        self.filesize = self.video.streams.filter(res=self.hd.get(), progressive=self.sound, file_extension='mp4')[0].filesize
        if num == 11:
            self.video.streams.filter(resolution=self.hd.get(), progressive=self.sound, file_extension="mp4")[0].download(path)
            self.text = 'succes'
        elif num == 12:
            try:
                self.video.streams.filter(resolution=self.hd1.get(), progressive=False, file_extension="mp4")[1].download(path)
                self.text = 'succes'
            except IndexError:
                n()
        if self.text == "succes":
            messagebox.showinfo(title="SUCCES", message="Завантаження завершено. Насолоджуйтесь переглядом")



    # def progressnar(self):
    #     self.progress["maximum"]=self.filesize
    #     while True:
    #         self.progress["value"]=self.

    # def threads(self, num):
    #     if num == 11:
    #         self.potok = Thread(target=self.download(num=11), daemon=True)
    #         self.potok = Thread(target=self., daemon=True)
    #         self.potok.start()
    #     elif num == 12:
    #         self.potok = Thread(target=self.download(num=12), daemon=True)
    #         self.potok = Thread(target=self., daemon=True)
    #         self.potok.start()

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
        self.withsong= Button(self.appwindow, text="Завантажити зі звуком", state="disabled", command=lambda : self.download(num=11), fg=self.colors[1], bg=self.colors[0])
        self.withsong.grid(row=3, column=4)
        self.nosound = Button(self.appwindow, text="Завантажити без звуку", state="disabled", command=lambda : self.download(num=12), fg=self.colors[1], bg=self.colors[0])
        self.nosound.grid(row=4, column=4)

        self.progress = Progressbar(self.appwindow, orient="horizontal", value=50, maximum=100, length=400)
        self.progress.grid(row=4, columnspan=3)
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
    appwindow.geometry("200x80")
    appwindow.resizable(width=True, height=True)
    x = (appwindow.winfo_screenwidth() - appwindow.winfo_reqwidth()) / 2
    y = (appwindow.winfo_screenheight() - appwindow.winfo_reqheight()) / 2
    appwindow.wm_geometry("+%d+%d" % (x,y))
    appwindow.configure(bg="#85C1E9")

    Label(text="Завантажуй з Ютуб безкоштовно", bg="#85C1E9").pack()
    Button(appwindow, text="Почати", command=lambda: setting(a=2)).pack()
    Button(appwindow, text="Вийти", command=lambda: setting(a=1)).pack()

    appwindow.mainloop()


