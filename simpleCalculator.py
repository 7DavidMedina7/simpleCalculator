from tkinter import *
from tkinter import font
import math

root = Tk()
# Setting the title of the window
root.title("Simple Calculator")

# Creating a input box for the user
e = Entry(root, width=55, borderwidth=15)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# Function to allow user to click and store the numbers
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


# Function to clear the current input state
def button_clear():
    e.delete(0, END)


# Function to add the numbers
def button_add():
    first_number = e.get()
    global f_num
    global operation
    operation = "addition"
    f_num = float(first_number)
    e.delete(0, END)


# Function to subtract the numbers
def button_subtract():
    first_number = e.get()
    global f_num
    global operation
    operation = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)


# Function to multiply the numbers
def button_multiply():
    first_number = e.get()
    global f_num
    global operation
    operation = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)


# Function to divide the numbers
def button_divide():
    first_number = e.get()
    global f_num
    global operation
    operation = "division"
    f_num = float(first_number)
    e.delete(0, END)


# Function to do raise the power of the numbers
def button_exponent():
    first_number = e.get()
    global f_num
    global operation
    operation = "exponent"
    f_num = float(first_number)
    e.delete(0, END)


# Function to change number to negative
def button_change_sign():
    first_number = e.get()
    e.delete(0, END)
    global f_num
    f_num = float("-" + first_number)
    e.insert(0, f_num)


# Function to add a decimal point to a number
def button_decimal():
    first_number = e.get()
    e.delete(0, END)
    global f_num
    f_num = float(first_number + ".")
    e.insert(0, f_num)


# Function to calculate sin()
def button_sin():
    first_number = e.get()
    e.delete(0, END)
    global f_num
    f_num = math.sin(float(first_number))
    e.insert(0, f_num)


# Function to calculate cos()
def button_cos():
    first_number = e.get()
    e.delete(0, END)
    global f_num
    f_num = math.cos(float(first_number))
    e.insert(0, f_num)


# Function to calculate tan()
def button_tan():
    first_number = e.get()
    e.delete(0, END)
    global f_num
    f_num = math.tan(float(first_number))
    e.insert(0, f_num)


# Function to show the result
def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if operation == "addition":
        e.insert(0, f_num + float(second_number))

    if operation == "subtraction":
        e.insert(0, f_num - float(second_number))

    if operation == "multiplication":
        e.insert(0, f_num * float(second_number))

    if operation == "division":
        e.insert(0, f_num / float(second_number))

    if operation == "exponent":
        e.insert(0, f_num ** float(second_number))


# Creating the buttons for the calculator
button_1 = Button(root, text="1", padx=40, pady=20, bg="#1710ad", fg="black", command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=41, pady=20, bg="#1710ad", fg="black", command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=42, pady=20, bg="#1710ad", fg="black", command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, bg="#1710ad", fg="black", command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=41, pady=20, bg="#1710ad", fg="black", command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=42, pady=20, bg="#1710ad", fg="black", command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, bg="#1710ad", fg="black", command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=41, pady=20, bg="#1710ad", fg="black", command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=42, pady=20, bg="#1710ad", fg="black", command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=41, pady=20, bg="#1710ad", fg="black", command=lambda: button_click(0))
button_change_sign = Button(root, text="+/-", padx=34, pady=20, bg="#cdde12", fg="black", command=button_change_sign)
button_decimal = Button(root, text=".", padx=43, pady=20, bg="#cdde12", fg="black", command=button_decimal)
button_equal = Button(root, text="=", padx=40, pady=20, bg="#168c32", fg="black", command=button_equal)
button_clear = Button(root, text="CLEAR", padx=123, pady=20, bg="black", fg="#1710ad", command=button_clear)
button_add = Button(root, text="+", padx=39, pady=20, bg="#c21717", fg="black", command=button_add)
button_subtract = Button(root, text="-", padx=40, pady=20, bg="#c21717", fg="black", command=button_subtract)
button_multiply = Button(root, text="*", padx=40, pady=20, bg="#c21717", fg="black", command=button_multiply)
button_divide = Button(root, text="/", padx=40, pady=20, bg="#c21717", fg="black", command=button_divide)
button_exponent = Button(root, text="^", padx=40, pady=20, bg="#c21717", fg="black", command=button_exponent)
button_sin = Button(root, text="SIN", padx=34, pady=20, bg="#de7f1b", fg="black", command=button_sin)
button_cos = Button(root, text="COS", padx=33, pady=20, bg="#de7f1b", fg="black", command=button_cos)
button_tan = Button(root, text="TAN", padx=32, pady=20, bg="#de7f1b", fg="black", command=button_tan)

# Setting the layout of the buttons
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)
button_change_sign.grid(row=4, column=0)
button_decimal.grid(row=4, column=2)
button_sin.grid(row=5, column=0)
button_cos.grid(row=5, column=1)
button_tan.grid(row=5, column=2)
button_clear.grid(row=6, column=0, columnspan=3)

button_divide.grid(row=1, column=3)
button_multiply.grid(row=2, column=3)
button_subtract.grid(row=3, column=3)
button_add.grid(row=4, column=3)
button_exponent.grid(row=5, column=3)
button_equal.grid(row=6, column=3)

root.mainloop()
