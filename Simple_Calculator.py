import math
import os
from tkinter import *

win = Tk()

# Calculate the screen width and height
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

# Calculate the window width and height
win_width = 570
win_height = 600

# Calculate the x and y coordinates to center the window
x_coordinate = (screen_width - win_width) // 2
y_coordinate = (screen_height - win_height) // 2

# Set the window geometry to determine the size and position
win.geometry(f'{win_width}x{win_height}+{x_coordinate}+{y_coordinate}')

# Disable the ability to resize the window in both directions
win.resizable(False, False)

# Set the title of the window
win.title("Simple_Calculator")

# Load the icon for the window from the specified file path
icon_path = os.path.join("../ICONS", "calculator.gif")
win_icon = PhotoImage(file=icon_path)

# Set the window icon using the loaded image
win.iconphoto(False, win_icon)

# Set the background color of the window to white
win.configure(bg="#ffffff")


equ = "" #intialize Val of equ before set functions updates it


def show(val): # show function (when i click a button he will use this to update the Label with the val excpet = and F
    global equ
    equ += val
    Label4Result.config(text=equ)

def clear(): # function to clear and C button will use it as a command
    global equ
    equ = ""
    Label4Result.config(text=equ)

def calculate(): #eval keyword for function Evaluate and retrun the result for operations and expressions
    global equ
    result = ""
    if equ != "":
        try:
            result = eval(equ)
        except Exception as e:
            result = "Error"
        equ = str(result)
    Label4Result.config(text=result)

#factorial function
def calculate_factorial():
    global equ

 #statmen for overvalue
    try:
        number = int(equ)
        if number > 99:
            Label4Result.config(text="High Input", font=('Google Sans', 20))
        else:
            result = math.factorial(number)
            equ = str(result)
            Label4Result.config(text=result)
    except ValueError:
        Label4Result.config(text="Value Error", font=('Google Sans', 20))


#function for keybind backspace
def backspace():
    global equ
    equ = equ[:-1]
    Label4Result.config(text=equ)

#Label for Result
Label4Result = Label(win, width=25, height=2, text="", bg="#ffffff", font=('Google Sans', 30))
Label4Result.pack()

#buttons

Button(win, text="C", width=5, height=1, font=("GoogleSans", 30, 'bold'), bd=1, fg="#fff", bg="#182028", command=lambda: clear()).place(x=10, y=100)
Button(win, text="/", width=5, height=1, font=("GoogleSans", 30, 'bold'), bd=1, fg="#fff", bg="#182028", command=lambda: show('/')).place(x=150, y=100)
Button(win, text="F", width=5, height=1, font=("GoogleSans", 30, 'bold'), bd=1, fg="#fff", bg="#182028", command=calculate_factorial).place(x=290, y=100)
Button(win, text="*", width=5, height=1, font=("GoogleSans", 30, 'bold'), bd=1, fg="#fff", bg="#182028", command=lambda: show('*')).place(x=430, y=100)
Button(win, text="7", width=5, height=1, font=("GoogleSans", 30, 'bold'), bd=1, fg="#fff", bg="#182028", command=lambda: show('7')).place(x=10, y=200)
Button(win, text="8", width=5, height=1, font=("GoogleSans", 30, 'bold'), bd=1, fg="#fff", bg="#182028", command=lambda: show('8')).place(x=150, y=200)
Button(win, text="9", width=5, height=1, font=("GoogleSans", 30, 'bold'), bd=1, fg="#fff", bg="#182028", command=lambda: show('9')).place(x=290, y=200)
Button(win, text="-", width=5, height=1, font=("GoogleSans", 30, 'bold'), bd=1, fg="#fff", bg="#182028", command=lambda: show('-')).place(x=430, y=200)
Button(win, text="4", width=5, height=1, font=("GoogleSans", 30, 'bold'), bd=1, fg="#fff", bg="#182028", command=lambda: show('4')).place(x=10, y=300)
Button(win, text="5", width=5, height=1, font=("GoogleSans", 30, 'bold'), bd=1, fg="#fff", bg="#182028", command=lambda: show('5')).place(x=150, y=300)
Button(win, text="6", width=5, height=1, font=("GoogleSans", 30, 'bold'), bd=1, fg="#fff", bg="#182028", command=lambda: show('6')).place(x=290, y=300)
Button(win, text="+", width=5, height=1, font=("GoogleSans", 30, 'bold'), bd=1, fg="#fff", bg="#182028", command=lambda: show('+')).place(x=430, y=300)
Button(win, text="1", width=5, height=1, font=("GoogleSans", 30, 'bold'), bd=1, fg="#fff", bg="#182028", command=lambda: show('1')).place(x=10, y=400)
Button(win, text="2", width=5, height=1, font=("GoogleSans", 30, 'bold'), bd=1, fg="#fff", bg="#182028", command=lambda: show('2')).place(x=150, y=400)
Button(win, text="3", width=5, height=1, font=("GoogleSans", 30, 'bold'), bd=1, fg="#fff", bg="#182028", command=lambda: show('3')).place(x=290, y=400)
Button(win, text="0", width=11, height=1, font=("GoogleSans", 30, 'bold'), bd=1, fg="#fff", bg="#182028", command=lambda: show('0')).place(x=10, y=500)
Button(win, text=".", width=5, height=1, font=("GoogleSans", 30, 'bold'), bd=1, fg="#fff", bg="#182028", command=lambda: show('.')).place(x=290, y=500)
Button(win, text="=", width=5, height=3, font=("GoogleSans", 30, 'bold'), bd=1, fg="#fff", bg="#E37824", command=calculate).place(x=430, y=400)



#keybinds

win.bind('7', lambda event: show('7'))
win.bind('8', lambda event: show('8'))
win.bind('9', lambda event: show('9'))
win.bind('4', lambda event: show('4'))
win.bind('5', lambda event: show('5'))
win.bind('6', lambda event: show('6'))
win.bind('1', lambda event: show('1'))
win.bind('2', lambda event: show('2'))
win.bind('3', lambda event: show('3'))
win.bind('0', lambda event: show('0'))
win.bind('/', lambda event: show('/'))
win.bind('*', lambda event: show('*'))
win.bind('-', lambda event: show('-'))
win.bind('+', lambda event: show('+'))
win.bind('.', lambda event: show('.'))
win.bind('<Return>', lambda event: calculate())
win.bind('<BackSpace>', lambda event: backspace())
win.bind('c', lambda event: clear())
win.bind('ؤ', lambda event: clear())
win.bind('C', lambda event: clear())
win.bind('f', lambda event: calculate_factorial())
win.bind('ؤ', lambda event: clear())
win.bind('F', lambda event: calculate_factorial())
win.bind('ب', lambda event: calculate_factorial())

win.mainloop()