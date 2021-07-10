from time import *
from tkinter import *


def update():

    time_string = strftime('%I:%M:%S %p')
    time_display.config(text=time_string)

    day_string = strftime('%A')
    day_display.config(text=day_string)

    date_string = strftime('%B %d, %Y')
    date_display.config(text=date_string)

    window.after(500, update)


window = Tk()
frame = Frame(bg='black')

time_display = Label(frame, font=('Gilroy', 60), bg='black', fg='green')
time_display.pack()

day_display = Label(frame, font=('GIlroy', 45), bg='black', fg='green')
day_display.pack()

date_display = Label(frame, font=('Gilroy', 50), bg='black', fg='green')
date_display.pack()

frame.pack()

window.title('Clock')
update()

window.mainloop()
