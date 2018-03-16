from tkinter import *
from db import DB

op = DB()
window = Tk()
window.wm_title("Book-Search by Devashish")
window.resizable(0,0)
#window.wm_iconbitmap('./book.png')

def get_selected_row(event):
    try:
        global cur_tuple
        index = lb.curselection()[0]
        cur_tuple = lb.get(index)
        entrybox1.delete(0, END)
        entrybox2.delete(0, END)
        entrybox3.delete(0, END)
        entrybox4.delete(0, END)
        entrybox1.insert(END, cur_tuple[1])
        entrybox2.insert(END, cur_tuple[2])
        entrybox3.insert(END, cur_tuple[3])
        entrybox4.insert(END, cur_tuple[4])
    except:
        pass


def clear_all():
    entrybox1.delete(0, END)
    entrybox2.delete(0, END)
    entrybox3.delete(0, END)
    entrybox4.delete(0, END)


def findbook():
    lb.delete(0, END)

    name = name_text.get()
    author = author_text.get()
    year = year_text.get()
    ISBN = ISBN_text.get()

    try:
        res = op.search(name, author, year, ISBN)
        for cur in res:
            lb.insert(END, cur)
        else:
            lb.insert(END, "No Data")
    except Exception as ex:
        lb.insert(END, ex.args)

    clear_all()


def findById(id):
    data = op.search_by_id(id)

    if len(data) < 0:
        return "No Data Found"
    else:
        return data[0]


def findall():
    lb.delete(0, END)

    try:
        res = op.view()

        for cur in res:
            lb.insert(END, cur)
        else:
            lb.insert(END, "No Data")
    except Exception as ex:
        lb.insert(END, ex.args)

    clear_all()


def add():
    lb.delete(0, END)
    name = name_text.get()
    author = author_text.get()
    year = year_text.get()
    isbn = ISBN_text.get()

    try:
        op.insert(name, author, year, isbn)
    except Exception as ex:
        lb.insert(END, ex.args)

    lb.insert(END,(name, author, year, isbn) )
    clear_all()


def delete():
    op.delete(cur_tuple[0])
    findall()
    clear_all()


def update():
    name = name_text.get()
    author = author_text.get()
    year = year_text.get()
    isbn = ISBN_text.get()
    op.update(cur_tuple[0], name, author, year, isbn)
    data = findById(cur_tuple[0])
    lb.delete(0, END)
    lb.insert(END, data)
    clear_all()


def close():
    pass


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