import instaloader
from tkinter import *
window=Tk()
# add widgets here

L1 = Label(window,text="User Name")
L1.pack( side = LEFT)
L1.place(x=50, y=150)

name_var= StringVar()

window.title('Instagram Profile Downloader')
lbl=Label(window, text="Instagram Profile Downloader", fg='red', font=("Helvetica", 16))

name_entry = Entry(window,textvariable = name_var, font=('calibre',10,'normal'))
name_entry.place(x=120, y=150)

Button=Button(window, text="Generate",command=lambda: code() )
Button.place(x=50, y=180)

def code():
    
    dp = name_var.get()
    ig = instaloader.Instaloader()

    ig.download_profile(dp, profile_pic_only=True)
    name_var.set("")


lbl.place(x=108, y=50)
window.geometry("500x400")
window.mainloop()
