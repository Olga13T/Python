import tkinter as tk
from pytube import YouTube

root = tk.Tk()
root.geometry('600x300')
root.resizable(0, 0)
root.title("download")

link = tk.StringVar()
tk.Label(root, text="Url address for video :",
         font="arial 10 bold"). place(x=100, y=50)
link_enter = tk.Entry(root, font="arial 10 bold", width = 70, textvariable=link). place(x=100, y=100)


def down_video():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    tk.Label(root, text = "sucsessfully", font= "arial 10").place(x = 35, y = 230)
    tk.Label(root, text= f"Video name: {video.title}", font = "arial 10").place(x = 35, y = 250)


tk.Button(root, text="download", font="arial 10 bold",
          bg="lightblue", command=down_video).place(x=130, y=170)

root.mainloop()
