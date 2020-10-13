from tkinter import *
window = Tk()

# Window geometry
window.title("Tk")
window.geometry('850x600')

# Set Frames
LeftTopFrame = Frame(window,bg='blue',height=800,width=700,borderwidth=2, highlightthickness="3",highlightcolor="black")
LeftTopFrame.pack(fill=X,side=LEFT)

lblInp = Label(LeftTopFrame, text='Label',font=('Tahoma', 10))
lblInp.grid(column=0,row=0)

lblIn2 = Label(LeftTopFrame, text='Label',font=('Tahoma', 10))
lblIn2.grid(column=0,row=4)

window.mainloop()



#def fahrenheit_to_celsius():
    """Convert the value for Fahrenheit to Celsius and insert the
    result into lbl_result.
    """
    fahrenheit = float(en1.get())
    celsius = (5/9) * (float(fahrenheit) - 32)
    mytexbox["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"


def celcius_to_fahrenheit():

    c_input = float(en2.get())
    fahrenheit_calc = (float(c_input - 9/5) + 32)
    mytexbox["text"]= fahrenheit_calc, 2
