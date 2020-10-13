from tkinter import * #import the toolkit
def testing():
    mytext="Hello guys"
    mytextbox.insert(0,mytext) #this makes sure the text is inserted into textbox
    return None
mywindow=Tk() #name the window
mywindow.title("GUI APP") #give the app a title
mywindow.geometry("300x800") #change the size
mywindow.configure(background="pink", relief="solid") #add a background colour, add a border
myLabel=Label(mywindow, text="Greetings to you all!") #myLabel is a variable name. pack spicies position. you could use configue and add row number/column
myLabel.pack() #add it after adding the label text
mytextbox=Entry(mywindow,width=30)
mytextbox.pack() #position
#a button will always need to call a function. a button comes from the button class. define ontop
mybutton=Button(mywindow,text="Click me",bg="powderblue", command=testing)
mybutton.pack()#pack it. make sure it shows up on the main window.

mywindow.mainloop()

#to place the buttons function text in the txtbox, in ur function declare a variable
