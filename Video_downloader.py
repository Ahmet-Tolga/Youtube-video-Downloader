from pytube import YouTube
from tkinter import *

def Download():
    video_link=link.get()
    video=YouTube(video_link)
    video=video.streams.get_highest_resolution()
    video.download()
    statu["fg"]="blue"
    statu["text"]="Video is Downloaded 😀"
def download_mp3():
    video_link=link.get()
    music=YouTube(video_link)
    t=music.streams.filter(only_audio=True).all()
    t[0].download()
    statu["fg"]="blue"
    statu["text"]="Music is Downloaded 😀"
interface=Tk()
interface.geometry("500x400")
interface.title("Youtube Video Downloader")
Label(text="Enter the Video link you wanna Download...",font=("klavika",15,"bold"),fg="red").place(x=10,y=20)
link=Entry(width=50)
link.place(x=20,y=70)
mp4_btn=Button(width=15,height=2,text="Download as mp4",bg="red",fg="white",command=Download)
mp4_btn.place(x=40,y=150)
mp3_btn=Button(text="Download as mp3",width=15,height=2,bg="blue",fg="white",command=download_mp3)
mp3_btn.place(x=200,y=150)
statu=Label(text="",fg="blue",font=("klavika",10,"bold"))
statu.place(x=40,y=220)

interface.mainloop()