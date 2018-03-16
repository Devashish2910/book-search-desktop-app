from tkinter import *
from db import DB

op = DB()
window = Tk()
window.wm_title("Book-Search by Devashish")
window.resizable(0,0)
#window.wm_iconbitmap('./book.png')


# Add labels
lbl1 = Label(window, text='Name: ')
lbl1.grid(row=0, column=0)
lbl2 = Label(window, text='Author: ')
lbl2.grid(row=0, column=2)
lbl3 = Label(window, text='Year: ')
lbl3.grid(row=1, column=0)
lbl4 = Label(window, text='ISBN: ')
lbl4.grid(row=1, column=2)



# Add Entry
name_text = StringVar()
entrybox1 = Entry(window, textvariable=name_text)
entrybox1.grid(row=0, column=1)
author_text = StringVar()
entrybox2 = Entry(window, textvariable=author_text)
entrybox2.grid(row=0, column=3)
year_text = StringVar()
entrybox3 = Entry(window,textvariable=year_text)
entrybox3.grid(row=1, column=1)
ISBN_text = StringVar()
entrybox4 = Entry(window, textvariable=ISBN_text)
entrybox4.grid(row=1, column=3)

# Add Listbox
lb = Listbox(window, height=15, width=40)
lb.grid(row=2, column=0, rowspan=6, columnspan=2)
lb.configure(background='#DCDCDC')
lb.bind('<<ListboxSelect>>', get_selected_row)

# Add Scrollbar
sb = Scrollbar(window, orient=VERTICAL)
sb.grid(row=2, column=2, rowspan=3)
lb.configure(yscrollcommand=sb.set)
sb.configure(command=lb.yview)

# Add button
frame1 = Frame(window)
button0 = Button(frame1, text="Search a Book", command=findbook)
button0.grid(row=2, column=3)
button0.config(width= 15, height=2)
button1 = Button(frame1, text="View All", command=findall)
button1.grid(row=3, column=3)
button1.config(width= 15, height=2)
button2 = Button(frame1, text="Add a Book", command=add)
button2.grid(row=4, column=3)
button2.config(width= 15, height=2)
button3 = Button(frame1, text="Delete Selected", command=delete)
button3.grid(row=5, column=3)
button3.config(width= 15, height=2)
button4 = Button(frame1, text="Update Selected", command=update)
button4.grid(row=6, column=3)
button4.config(width= 15, height=2)
button5 = Button(frame1, text="Close", command=close)
button5.grid(row=7, column=3)
button5.config(width= 15, height=2)
frame1.grid(row=2, column=3)

window.mainloop()