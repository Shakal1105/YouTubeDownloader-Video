from cx_Freeze import setup, Executable
import sys, tkinter.filedialog, tkinter

root = tkinter.Tk()
def setuper(base, filecompile):
    root.destroy()
    setup(
        name="UTybeLinkDownload",
        icon="shak.ico",
        version="0.11.1",
        lang='Ukraine',
        description="[Shakal] Glory to Ukraine, .ussian warship fuckyou",
        executables=[Executable(filecompile, base=base, icon="shak.ico", shortcutDir="Shakal YoutubeLoader", trademarks="Shakal", shortcutName="ShakLoaderYoutube", copyright="The Shakal")]
    )

x32_x64 = sys.platform
filecompile = tkinter.filedialog.askopenfilename(title="Файл которий в exe")



if x32_x64 == 'win32':
    base = "Win32GUI"
    setuper(base=base, filecompile=filecompile)
elif x32_x64 == "win64":
    base = "Win64GUI"
    setuper(base=base, filecompile=filecompile)
else:
    print("Error, this compile only x32 or x64 Windows")

root.mainloop()
