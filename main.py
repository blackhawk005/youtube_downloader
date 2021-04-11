from tkinter import *
from tkinter import ttk

yt_link = ""
button_row = ""
window_2 = Tk()
def submit():
    yt_link = link_entry.get()
    window.destroy()
    window_2.mainloop()

window = Tk()
window.title("Youtube downloader")
window.geometry('500x300')
window.configure(background = "white")
n = StringVar()

link = Label(window ,text = "Enter your link here", justify=LEFT)
link_entry = Entry(window)
link.grid(row = 0,column = 0, padx = 10, pady = 25)
link_entry.grid(row = 1,column = 1)
button1 = Button(window, text="Submit", command=submit)
button1.grid(row=1, column=2)

for i in range(2, 4):
    x = Label(window, text=i, justify=LEFT)
    x.grid(row = i, column = 1)
    button_row = str(i)

print(button_row)
window.mainloop()


window_2.title("Youtube downloader 2")
window_2.geometry('500x300')
window_2.configure(background = "white")
linker = Label(window_2 ,text = "Enter your link here", justify=LEFT)
linker.grid(row = 0,column = 0, padx = 10, pady = 25)