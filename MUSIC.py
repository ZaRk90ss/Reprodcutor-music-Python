from tkinter import ttk
from tkinter import *
from tkinter import messagebox, filedialog
from pygame import mixer
import os

go = Tk()
go.title("MUSIC REPRODUCTOR")
go.minsize(420, 260)
go.maxsize(420, 260)
go.config(background="white")
mixer.init()

#IMAGES
#YOU WOULD PUT YOUR DIR FILE IMAGE
file_upload = PhotoImage(file=r"HERE YOUR DIR")
play_icon = PhotoImage(file=r"HERE YOUR DIR")
pause_icon = PhotoImage(file=r'HERE YOUR DIR')

####################################################################################################################################################################################################################

def add_song():
    song = filedialog.askopenfilename(initialdir='audio/',
                                    title='Choose a song', 
                                    filetypes=(("mp3 Files", "*.mp3"), ))
    currentFile = StringVar()
    currentFile.set(os.path.basename(song))
    name_music.config(textvariable=currentFile)
    name_music.place(x=30, y=50)
    mixer.music.load(song)
    mixer.music.play()

def unpause_music():
    mixer.music.unpause()
    play_button.configure(image=play_icon,command=pause_music)
    play_button.place(x=370, y=468)

def pause_music():
    mixer.music.pause()
    play_button.configure(image= pause_icon,command=unpause_music)
    play_button.place(x=370 ,y=468)

def change_volume(x):
    mixer.music.set_volume(volume.get())
    current_volume = mixer.music.get_volume()
    volume_numb.config(text=current_volume * 100)

def change_black():
    go.config(background="black")

name_music = Entry(go, background="white", border=0, borderwidth=0, font=("arial", 14), width=29)
name_music.place(x=30, y=50)

choose = Button(go, image= file_upload, command=add_song, border=0, borderwidth=0, background="white", activebackground="white")
choose.place(x=150, y=114)

play_button = Button(go, image= play_icon, border=0, borderwidth=0, bg="white", activebackground="white", command=pause_music)
play_button.place(x=80, y=110)

volume = ttk.Scale(go, value=1, from_=0, to=1, orient=HORIZONTAL, length=180, command=change_volume)
volume.place(x=220, y=130)
volume.set(0)

volume_numb = Label(go, text="0", font=("arial", 14), background="white")
volume_numb.place(x=290, y=100)

change_color = Button(go, text="Change background color", command=change_black)
change_color.place(x=20, y=180)

go.mainloop()

#;)