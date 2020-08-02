import os
from tkinter import messagebox
import booking_guide
import search_guide
from tkinter import *
import mysql.connector as mcon

mydb = mcon.connect(host = "localhost",user = "root",passwd = "tarun@12345",database = "Parkon")
mycursor = mydb.cursor()

class Search:
    def __init__(self,root):
        self.window = root
        self.window.geometry('800x400')
        self.window.title('Search Record')
        self.window.configure(bg='black')
        self.v_entry_var = StringVar()
        self.d_entry_var = StringVar()

        menu = Menu(root)
        root.config(menu=menu)
        submenu = Menu(menu)
        submenu_2 = Menu(menu)
        submenu_3 = Menu(menu)
        menu.add_cascade(label='User Guide', menu=submenu)

        menu.add_cascade(label='Help', menu=submenu_2)
        menu.add_cascade(label='About', menu=submenu_3)
        menu.add_cascade(label='Exit Search Page',command = self.window.destroy)

        # Configuring Submenus ...
        submenu.add_command(label='Booking Guides', command=self.ug_book)
        submenu.add_separator()
        submenu.add_command(label='Searching Guides', command=self.ug_search)
        submenu_2.add_command(label='Common Issues', command=self.help_ci)
        submenu_2.add_separator()
        submenu_2.add_command(label='Other Issues ?', command=self.help_oi)
        submenu_3.add_command(label='About Parkon System', command=self.about)

        self.vehicle_label = Label(self.window,bg='black', text="Vehicle No.",fg='white',font=('times new roman',20,'bold')).grid(row=0, column=0, padx=20, pady=20)
        self.vehicle_entry = Entry(self.window, textvar=self.v_entry_var, bd=2,width = 40).grid(row=0, column=1, padx=20, pady=20)
        self.date_label = Label(self.window, text="Enter Date ",fg='white',font=('times new roman',20,'bold'),bg='black').grid(row=1, column=0, padx=20, pady=20)
        self.date_entry = Entry(self.window, textvariable=self.d_entry_var, bd=2,width = 40).grid(row=1, column=1, padx=20, pady=20)
        self.search_btn_1 = Button(self.window, command=self.search_by_vehicle_no, text="Search Record",font=('bold',20),fg='red',bg='black').grid(row=0, column=2, padx=20,
                                                                                               pady=20)
        self.search_btn_2 = Button(self.window, command=self.search_by_date, text="Search Record",fg='red',bg='black',font=('bold',20)).grid(row=1, column=2, padx=20,
                                                                                         pady=20)
        self.lbl = Label(self.window, bg='black').grid(row=2, column=0)
        #self.listbox = Listbox(self.window, width=60, bd=2).grid(row=3, column=0, columnspan=8)
        self.x_lbl = Label(self.window, bg='black').grid(row=4, column=0)
        # clear_btn = Button(window,text = 'Reset',width=15).grid(row=5,column=1,rowspan=2)

    def search_by_vehicle_no(self):
        val = self.v_entry_var.get()
        query = 'select*from book_slot where vehicle_no = "{}"'.format(val)
        mycursor.execute(query)
        c=[]
        for i in mycursor:
            c.append(str(i))
        savefile = open('C:/Users/Tarun/PycharmProjects/first/bill.txt', 'w').write('{}'.format(str(c)))
        os.startfile('C:/Users/Tarun/PycharmProjects/first/bill.txt')


    def search_by_date(self):
        date = self.d_entry_var.get()
        query = 'select*from book_slot where date = "{}"'.format(date)
        mycursor.execute(query)
        c=[]
        for i in mycursor:
            for x in i:
                c.append(x)
        savefile = open('C:/Users/Tarun/PycharmProjects/first/bill.txt', 'w').write('{}'.format(str(c)))
        os.startfile('C:/Users/Tarun/PycharmProjects/first/bill.txt')
    def ug_book(self):
        root = Tk()
        c=booking_guide.Info(root)
        root.mainloop()

    def ug_search(self):
        root = Tk()
        c=search_guide.Info(root)
        root.mainloop()


    def about(self):
        messagebox.showinfo('About Parkon System',"Parkon Parking Solutions is an simplistic yet an effective tool for managing parking space and traffic. It provides with features to book slot, exit and searching of records and it has very easy maintainance. Guess what No more complex UI or training needed to use this software. It is very simple and user friendly. Anyone with knowledge of computer can use it. It is very secure and no data will be lost. Hope you have great experience")
    def help_ci(self):
        messagebox.showinfo('Common Issues','1. Incorrect credentials : Username / Password must be wrong.\n Solution : Rewrite with correct credentials.\n\n2.No Details are being stored.\n Solution : This situation occurs only when some component got uninstalled accidently. Make sure you have all the requirements of software fulfilled and all components are installed.\n\n3.No search result.\n Solution : Credentials entered must be wrong. Check and try again\n\n4.Other issues ?\n Solution : Check out other issues in Help>Other Issues. You can also request tech support or tech assistant visits.')

    def help_oi(self):
        messagebox.showinfo("Having other issues , You can mail us at : raynold_tarun@gmail.com")
#os.startfile('',"print")

root=Tk()
c=Search(root)
root.mainloop()
