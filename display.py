from tkinter import *

window = Tk()



# Add labels
lbl1 = Label(window, text='Name: ')
lbl1.grid(row=0, column=0)
lbl2 = Label(window, text='Author: ')
lbl2.grid(row=0, column=2)
lbl3 = Label(window, text='Price: ')
lbl3.grid(row=1, column=0)
lbl4 = Label(window, text='ISBN: ')
lbl4.grid(row=1, column=2)



# Add Entry
entrybox1 = Entry(window)
entrybox1.grid(row=0, column=1)
entrybox2 = Entry(window)
entrybox2.grid(row=0, column=3)
entrybox3 = Entry(window)
entrybox3.grid(row=1, column=1)
entrybox4 = Entry(window)
entrybox4.grid(row=1, column=3)

# Add Textbox
textbox1 = Text(window, height=15, width=40)
textbox1.grid(row=3, column=0, columnspan=3)
textbox1.configure(background='#4D4D4D')

# Add button
frame1 = Frame(window)
button1 = Button(frame1, text="Find")
button1.grid(row=3, column=1)
button1.config(width= 15, height=2)
button2 = Button(frame1, text="Add")
button2.grid(row=4, column=1)
button2.config(width= 15, height=2)
button3 = Button(frame1, text="Delete")
button3.grid(row=5, column=1)
button3.config(width= 15, height=2)
button4 = Button(frame1, text="Update")
button4.grid(row=6, column=1)
button4.config(width= 15, height=2)
button5 = Button(frame1, text="Close")
button5.grid(row=7, column=1)
button5.config(width= 15, height=2)
frame1.grid(row=3, column=3)

window.mainloop()