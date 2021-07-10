from tkinter import *


def button_press(number):

    global Input
    Input = Input + str(number)
    equation_label.set(Input)


def result():

    try:
        global Input
        total = str(eval(Input))
        equation_label.set(total)
        Input = total
    except ZeroDivisionError:
        equation_label.set('Math Error')
        Input = ''
    except SyntaxError:
        equation_label.set('Syntax Error')
        Input = ''


def reset():

    global Input
    equation_label.set('')
    Input = ''


Window = Tk()
Window.title('Calculator')
Window.geometry('750x750')

Input = ''
equation_label = StringVar()

Display = Label(Window,
                textvariable=equation_label,
                font=('Gilroy', 25),
                bg='black',
                fg='green',
                width=30,
                height=3)

Display.pack()

button_frame = Frame(Window)
button_frame.pack()

input_1 = Button(button_frame,
                 text=1,
                 height=2,
                 width=5,
                 font=('Gilroy', 35),
                 bg='white',
                 command=lambda: button_press(1))
input_1.grid(row=0, column=0)

input_2 = Button(button_frame,
                 text=2,
                 height=2,
                 width=5,
                 font=('Gilroy', 35),
                 bg='white',
                 command=lambda: button_press(2))
input_2.grid(row=0, column=1)

input_3 = Button(button_frame,
                 text=3,
                 height=2,
                 width=5,
                 font=('Gilroy', 35),
                 bg='white',
                 command=lambda: button_press(3))
input_3.grid(row=0, column=2)

input_4 = Button(button_frame,
                 text=4,
                 height=2,
                 width=5,
                 font=('Gilroy', 35),
                 bg='white',
                 command=lambda: button_press(4))
input_4.grid(row=1, column=0)

input_5 = Button(button_frame,
                 text=5,
                 height=2,
                 width=5,
                 font=('Gilroy', 35),
                 bg='white',
                 command=lambda: button_press(5))
input_5.grid(row=1, column=1)

input_6 = Button(button_frame,
                 text=6,
                 height=2,
                 width=5,
                 font=('Gilroy', 35),
                 bg='white',
                 command=lambda: button_press(6))
input_6.grid(row=1, column=2)

input_7 = Button(button_frame,
                 text=7,
                 height=2,
                 width=5,
                 font=('Gilroy', 35),
                 bg='white',
                 command=lambda: button_press(7))
input_7.grid(row=2, column=0)

input_8 = Button(button_frame,
                 text=8,
                 height=2,
                 width=5,
                 font=('Gilroy', 35),
                 bg='white',
                 command=lambda: button_press(8))
input_8.grid(row=2, column=1)

input_9 = Button(button_frame,
                 text=9,
                 height=2,
                 width=5,
                 font=('Gilroy', 35),
                 bg='white',
                 command=lambda: button_press(9))
input_9.grid(row=2, column=2)

input_0 = Button(button_frame,
                 text=0,
                 height=2,
                 width=5,
                 font=('Gilroy', 35),
                 bg='white',
                 command=lambda: button_press(0))
input_0.grid(row=3, column=0)

input_decimal_point = Button(button_frame,
                             text='.',
                             height=2,
                             width=5,
                             font=('Gilroy', 35),
                             bg='white',
                             command=lambda: button_press('.'))
input_decimal_point.grid(row=3, column=1)

input_plus = Button(button_frame,
                    text='+',
                    height=2,
                    width=5,
                    font=('Gilroy', 35),
                    bg='white',
                    command=lambda: button_press('+'))
input_plus.grid(row=0, column=3)

input_minus = Button(button_frame,
                     text='-',
                     height=2,
                     width=5,
                     font=('Gilroy', 35),
                     bg='white',
                     command=lambda: button_press('-'))
input_minus.grid(row=1, column=3)

input_multiply = Button(button_frame,
                        text='*',
                        height=2,
                        width=5,
                        font=('Gilroy', 35),
                        bg='white',
                        command=lambda: button_press('*'))
input_multiply.grid(row=2, column=3)

input_divide = Button(button_frame,
                      text='/',
                      height=2,
                      width=5,
                      font=('Gilroy', 35),
                      bg='white',
                      command=lambda: button_press('/'))
input_divide.grid(row=3, column=3)

input_equal = Button(button_frame,
                     text='=',
                     height=2,
                     width=5,
                     font=('Gilroy', 35),
                     bg='white',
                     command=result)

input_equal.grid(row=3, column=2)

input_reset = Button(button_frame,
                     text='Reset',
                     height=2,
                     width=5,
                     font=('Gilroy', 35),
                     bg='white',
                     command=reset)
input_reset.grid(row=3, column=4)

Window.mainloop()
