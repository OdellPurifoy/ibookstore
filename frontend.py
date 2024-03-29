from tkinter import *
import backend

def get_selected_row(event):
    try:
        global selected_tuple
        index = list_box.curselection()[0]
        selected_tuple = list_box.get(index)

        entry1.delete(0, END)
        entry1.insert(END, selected_tuple[1])

        entry2.delete(0, END)
        entry2.insert(END, selected_tuple[2])

        entry3.delete(0, END)
        entry3.insert(END, selected_tuple[3])

        entry4.delete(0, END)
        entry4.insert(END, selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list_box.delete(0, END)
    for row in backend.view_data():
        list_box.insert(END, row)

def search_command():
    list_box.delete(0, END)
    for row in backend.search_data(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list_box.insert(END, row)

def insert_command():
    backend.insert_data(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list_box.delete(0, END)
    list_box.insert(END,(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def update_command():
    backend.update_data(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())

def delete_command():
    backend.delete_data(selected_tuple[0])


window = Tk()

#title
window.wm_title("iBookStore")

#labels
label1 = Label(window, text="Title")
label1.grid(row=0, column=0)

label2 = Label(window, text="Author")
label2.grid(row=0, column=2)

label3 = Label(window, text="Year")
label3.grid(row=1, column=0)

label4 = Label(window, text="ISBN")
label4.grid(row=1, column=2)

#entries
title_text = StringVar()
entry1 = Entry(window, textvariable=title_text)
entry1.grid(row=0, column=1)

author_text = StringVar()
entry2 = Entry(window, textvariable=author_text)
entry2.grid(row=0, column=3)

year_text = StringVar()
entry3 = Entry(window, textvariable=year_text)
entry3.grid(row=1, column=1)

isbn_text = StringVar()
entry4 = Entry(window, textvariable=isbn_text)
entry4.grid(row=1, column=3)

list_box = Listbox(window, heigh=6, width=35)
list_box.grid(row=2, column=1, rowspan=6, columnspan=1)

scroll_bar = Scrollbar(window)
scroll_bar.grid(row=2, column=2, rowspan=6)

list_box.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=list_box.yview)

list_box.bind('<<ListboxSelect>>', get_selected_row)

button1 = Button(window, text="View All", width=12, command=view_command)
button1.grid(row=2, column=3)

button2 = Button(window, text="Search", width=12, command=search_command)
button2.grid(row=3, column=3)

button3 = Button(window, text="Add Entry", width=12, command=insert_command)
button3.grid(row=4, column=3)

button4 = Button(window, text="Update Entry", width=12, command=update_command)
button4.grid(row=5, column=3)

button5 = Button(window, text="Delete Entry", width=12, command=delete_command)
button5.grid(row=6, column=3)

button6 = Button(window, text="Close", width=12, command=window.destroy)
button6.grid(row=7, column=3)


window.mainloop()
