from pytube import YouTube
from tkinter import *

def download():
    youtube = YouTube(textLink.get())
    diretorio = textDir.get()
    diret= youtube.streams.get_highest_resolution() 
    diret.download(diretorio)
    status["text"] = 'Download completo!'

app = Tk()
app.title("YoutubeDown")
app.geometry("275x100")
app.resizable(width=False, height=False)

txtLink = Label(app, text="Link")
txtLink.grid(column=0, row=0)

textLink = Entry(app)
textLink.grid(column=1, row=0)

txtDir = Label(app, text="Pasta")
txtDir.grid(column=0, row=1)

textDir = Entry(app)
textDir.grid(column=1, row=1)

btn = Button(app, text="Baixar", command=download)
btn.grid(column=4, row=0)

status =  Label(app, text="")
status.grid(column=1, row=2)

app.mainloop()