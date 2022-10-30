from pytube import YouTube
import tkinter
from tkinter import Label
from tkinter import *
from tkinter import messagebox
import moviepy.editor as mp
import os





maindir = os.path.dirname(__file__)
#print(maindir)
Files_D = os.path.join(maindir, "downloads")
#print(Files_D)

#### funtion
def D_video():
    link = entry_text.get()
    video = YouTube(link,)
    download = video.streams.get_highest_resolution()
    download.download("downloads")
    messagebox.showinfo("info","The video has been downloaded successfully")





def D_audio():
    link = entry_text.get()
    audio = YouTube(link)
    download = audio.streams.get_lowest_resolution()
    #print(audio.streams[0].title + ".mp4")
    flag = download.download(output_path=Files_D)

    base, ext= os.path.splitext(flag)
    base = base + ".mp4"
    clip = mp.VideoFileClip(base)
    clip.audio.write_audiofile(base + ".mp3")
    clip.close()
    os.remove(base)
    messagebox.showinfo("info","Your Audio has been downloaded successfully")
           
   



####
main = tkinter.Tk()
main.title("Basic youtube downloader")
main.geometry("450x330")
#####



##### load image
#photo = PhotoImage(file="photo.png")
#layout = Label(main, image=photo, bd=0)
#layout.grid(row=0, column=0)
######



######
etiqueta = Label(main, text="Paste the URL here!")
etiqueta.pack()

######

#####
entry_text = Entry(main, width=60)
entry_text.pack()
######

######
button_Video = Button(main,text="Download Video",command=D_video)
button_Video.pack()

button_Audio = Button(main,text="Download Audio",command=D_audio)
button_Audio.pack()

#######

##### load image
photo = PhotoImage(file="photo.png")
layout = Label(main, image=photo, bd=0)
layout.pack()
######
info = Label(main, text="video/audio is gonna be downloaded in /basic_youtube_downloader/downloads\nthe program will freeze while it downloads.")
info.pack()
main.mainloop()