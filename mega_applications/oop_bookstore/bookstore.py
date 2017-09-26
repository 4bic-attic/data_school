from tkinter import *
from backend import Database

database=Database("books.db")
class Window():
    """docstring for Window."""
    def __init__(self, window):

        self.window = window
        self.window.wm_title("BookStore Widget")
        # Book labels
        l1=Label(window,text='Title')
        l1.grid(row=0,column=0)

        l2=Label(window,text='Author')
        l2.grid(row=0,column=2)

        l3=Label(window,text='Year')
        l3.grid(row=1,column=0)

        l4=Label(window,text='ISBN')
        l4.grid(row=1,column=2)

        # book details entry
        title_text=StringVar()
        e1=Entry(window, textvariable=title_text)
        e1.grid(row=0, column=1)

        author_text=StringVar()
        e2=Entry(window, textvariable=author_text)
        e2.grid(row=0, column=3)

        year_text=StringVar()
        e3=Entry(window, textvariable=year_text)
        e3.grid(row=1, column=1)

        isbn_text=StringVar()
        e4=Entry(window, textvariable=isbn_text)
        e4.grid(row=1, column=3)

        # Listbox
        list1=Listbox(window, height=6,width=35)
        list1.grid(row=2,column=0,rowspan=6,columnspan=2)
        # scrollbar
        sb1=Scrollbar(window)
        sb1.grid(row=2,column=2,rowspan=6)

        # attach scrollbar to the Listbox
        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview)

        # bind functions to event type
        list1.bind('<<ListboxSelect>>',self.get_selected_row)
        # buttons
        b1=Button(window,text="View All",width=12,command=self.view_command)
        b1.grid(row=2,column=3)

        b2=Button(window,text="Search Book ",width=12,command=self.search_command)
        b2.grid(row=3,column=3)

        b3=Button(window,text="Add Entry",width=12,command=self.add_entry_command)
        b3.grid(row=4,column=3)

        b4=Button(window,text="Update",width=12,command=self.update_command)
        b4.grid(row=5,column=3)

        b5=Button(window,text="Delete",width=12,command=self.delete_command)
        b5.grid(row=6,column=3)

        b6=Button(window,text="Close",width=12,command=window.destroy)
        b6.grid(row=7,column=3)

    def get_selected_row(self, event):
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[3])

    def view_command(self):
        list1.delete(0,END)
        for row in database.view():
            list1.insert(END,row)

    def search_command(self):
        list1.delete(0,END)
        for row in database.search(title_text.get(),
        author_text.get(),year_text.get(),isbn_text.get()):
            list1.insert(END,row)

    def add_entry_command(self):
        database.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
        list1.delete(0,END)
        list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

    def update_command(self):
        database.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())

    def delete_command(self):
        database.delete(selected_tuple[0])





window=Tk()
Window(window)
window.mainloop()
