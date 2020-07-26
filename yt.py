from tkinter import *
import webbrowser
def yt():
    n=e.get()
    l=n.split(".")
    l[1]=l[1]+"cp"
    url=""
    for i in l:
        k="."
        url+=i
        url+=k
    leng=len(url)
    link=url[:leng-1]
    webbrowser.open(link)
    l2=Label(m, text="Your Video is downloaded")
    l2.grid(row=2, column=1)

m=Tk()
m.title("YouTubeDownloader")
v=StringVar()
l=Label(m, text="Copy the link")
e=Entry(m)
b=Button(m, text="Download", width=25, command=yt)

l.grid(row=1, column=0)
e.grid(row=1, column=1)
b.grid(row=1, column=2)
m.mainloop()

