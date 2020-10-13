


from tkinter import *


def build_gui():
    window = Tk()
    window.title("Adding Two Numbers")
    window.geometry("450x450")

    first_frame = Frame(window)
    first_frame.pack()

    second_frame = Frame(window)
    second_frame.pack()

    third_frame = Frame(window)
    third_frame.pack()

    fouth_frame = Frame(window)
    fouth_frame.pack()

    num_1 = IntVar()
    num_2 = IntVar()
    num_3 = IntVar()

    label1 = Label(first_frame, text="Please enter first number", padx="21", pady="20")
    label1.pack(side=LEFT)

    label1_entry = Entry(first_frame, textvariable=num_1)
    label1_entry.pack(side=RIGHT)

    label2 = Label(second_frame, text="Please enter second number", padx="10", pady="20")
    label2.pack(side=LEFT)

    label2_entry = Entry(second_frame, textvariable=num_2)
    label2_entry.pack(side=RIGHT)

    label3 = Label(third_frame, text="You answer: ", padx='65')
    label3.pack(side=LEFT)

    label3_entry = Entry(third_frame, textvariable=num_3)
    label3_entry.pack(side=LEFT)

    def adding():
        label3_entry.insert(0, num_1.get() + num_2.get())

    add_btn = Button(text="Add", command=adding)
    add_btn.pack(side=LEFT)

    def clear_all_num():
        label1_entry.delete(0, END)
        label2_entry.delete(0, END)
        label3_entry.delete(0, END)

    clear_button = Button(text="Clear", command=clear_all_num)
    clear_button.pack(side=LEFT)

    def exit_program():
        window.destroy()

    exit_button = Button(text="Exit", command=exit_program)
    exit_button.pack(side=LEFT)

    window.mainloop()


build_gui()
