from tkinter import *
from tkinter import filedialog
import os
from pygame import mixer

root = Tk()
frame1 = Frame(root, bg="gray")
frame2 = Frame(root, bg="gray")

audiotrack = StringVar()
musicstatus = StringVar()
no_of_song = 0
dire = ""
N = 0


def playlistsongs():
    global songs, N, dire, no_of_song
    dire = filedialog.askdirectory()
    songs = os.listdir(dire)
    no_of_song = len(songs)
    audiotrack.set(dire + "/" + songs[N])


def nextsong():
    global N, songs, dire, no_of_song
    if N != no_of_song - 1:
        N += 1
        audiotrack.set(dire + "/" + songs[N])
        play()


def lastsong():
    global N, songs, dire
    if N != 0:
        N -= 1
        audiotrack.set(dire + "/" + songs[N])
        play()


def stop():
    mixer.music.stop()
    musicstatus.set("....stop....")


def resume():
    mixer.music.unpause()
    root.btnresume.grid_remove()
    root.btnpause.grid()
    musicstatus.set("....playing....")


def volumeup():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol + 0.1)


def volumedown():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol - 0.1)


def trackpath():
    path = filedialog.askopenfilename()
    audiotrack.set(path)
    musicstatus.set("")


def play():
    p = audiotrack.get()
    mixer.music.load(p)
    mixer.music.play()
    musicstatus.set("....playing....")


def pause():
    mixer.music.pause()
    root.btnpause.grid_remove()
    root.btnresume.grid()
    musicstatus.set("....pause....")


# ******************************************************************************* All the buttons
def widgets():
    label = Label(root, text="Music Player", font=("Arial", 40, "bold"), bg="red")
    label.pack()

    labeltrack = Label(frame1, text="Select Music Track :", bd=5, font=("Arial", 20, "bold"), bg="gray")
    labeltrack.grid(row="1", column="1")

    tracksearch = Entry(frame1, bd=5, width=50, font=("Arial", 10, "bold"), textvariable=audiotrack)
    tracksearch.grid(row="1", column="2", padx=25, pady=40)

    search = Button(frame1, text="Search ", bd=5, font=("Arial", 12, "bold"), command=trackpath, bg="orange")
    search.grid(row="1", column="3")

    btnbk = Button(frame2, text="<-", border=8, font=("Arial", 10, "bold"), padx=10, bg="orange", activebackground="red",
                   activeforeground="green", command=lastsong)
    btnbk.grid(row="1", column="1", rowspan="2", padx="1")

    btnplay = Button(frame2, text="play ▶", border=8, font=("Arial", 10, "bold"), padx=6, bg="orange",
                     activebackground="red", activeforeground="green", command=play)
    btnplay.grid(row="1", column="2", rowspan="2", padx="1")

    root.btnpause = Button(frame2, text="pause ||", border=8, font=("Arial", 10, "bold"), padx=7, bg="orange",
                           activebackground="red", activeforeground="green", command=pause)
    root.btnpause.grid(row="1", column="3", rowspan="2", padx="1")

    root.btnresume = Button(frame2, text="resume ▶|", border=8, font=("Arial", 10, "bold"), padx=7, bg="orange",
                            activebackground="red", activeforeground="green", command=resume)
    root.btnresume.grid(row="1", column="3", rowspan="2", padx="1")

    root.btnresume.grid_remove()

    btnstop = Button(frame2, text="stop", border=8, font=("Arial", 10, "bold"), padx=7, bg="orange",
                     activebackground="red", activeforeground="green", command=stop)
    btnstop.grid(row="1", column="4", rowspan="2", padx="1")

    btnfor = Button(frame2, text="->", border=8, font=("Arial", 10, "bold"), padx=10, bg="orange",
                    activebackground="red", activeforeground="green", command=nextsong)
    btnfor.grid(row="1", column="5", rowspan="2", padx="1")

    status = Label(frame2, textvariable=musicstatus, bd=5, font=("Arial", 10, "bold"), bg="gray", fg="blue")
    status.grid(row="1", rowspan="2", column="6", padx="6")

    btnVolup = Button(frame2, text="Volume +", border=8, font=("Arial", 10, "bold"), padx=7, bg="orange",
                      command=volumeup, activebackground="red", activeforeground="green")
    btnVolup.grid(row="1", column="7", padx="70", pady="20")

    btnVoldn = Button(frame2, text="Volume -", border=8, font=("Arial", 10, "bold"), padx=10, bg="orange",
                      command=volumedown, activebackground="red", activeforeground="green")
    btnVoldn.grid(row="2", column="7")

    btnplaylist = Button(frame2, text="Playlist", border=8, font=("Arial", 10, "bold"), padx=10, bg="orange",
                         activebackground="red", activeforeground="green", command=playlistsongs)
    btnplaylist.grid(row="1", column="8")

    frame1.pack(side="top")
    frame2.pack(side="top")


# ******************************************************************************
root.geometry("800x400")
root.config(bg="gray")
root.title("My Music Player....")
root.resizable(False, False)
mixer.init()
widgets()

root.mainloop()