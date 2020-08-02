import os
from tkinter import messagebox
import booking_guide
import search_guide
import datetime
from datetime import date
from tkinter import *
import mysql.connector as mcon

mydb = mcon.connect(host = "localhost",user = "root",passwd = "tarun@12345",database = "Parkon")
mycursor = mydb.cursor()

class Exiting:
    def __init__(self,window):
        self.window=window
        self.window.geometry('750x500')
        self.window.configure(bg='black')

        menu = Menu(self.window)
        self.window.config(menu=menu)
        submenu = Menu(menu)
        submenu_2 = Menu(menu)
        submenu_3 = Menu(menu)
        menu.add_cascade(label='User Guide', menu=submenu)

        menu.add_cascade(label='Help', menu=submenu_2)
        menu.add_cascade(label='About', menu=submenu_3)
        menu.add_cascade(label='Exit This Page', command = self.window.destroy)

        # Configuring Submenus ...
        submenu.add_command(label='Booking Guides', command=self.ug_book)
        submenu.add_separator()
        submenu.add_command(label='Searching Guides', command=self.ug_search)
        submenu_2.add_command(label='Common Issues', command=self.help_ci)
        submenu_2.add_separator()
        submenu_2.add_command(label='Other Issues ?', command=self.help_oi)
        submenu_3.add_command(label='About Parkon System', command=self.about)

        self.v_no = StringVar()
        self.amount = StringVar()
        self.slot_no = StringVar()

        vehicle_label = Label(self.window, text="Vehicle No.",bg='black',fg='white',font=('times new roman',20,'bold')).grid(row=0, column=0, padx=50, pady=50)
        vehicle_entry = Entry(self.window, textvariable=self.v_no, bd=2,width = 40).grid(row=0, column=1, padx=50, pady=20)
        slot_label = Label(self.window, text="Enter Slot Number ",bg='black',fg='white',font=('times new roman',20,'bold')).grid(row=1, column=0, padx=20, pady=20)
        slot_entry = Entry(self.window, textvariable=self.slot_no, bd=2,width = 40).grid(row=1, column=1, padx=20, pady=20)
        book_btn = Button(self.window,command = self.exiter, bg='gray', text='Free Slot',
                          font=('times new roman', 30, 'bold'), fg='white', width=10).grid(row=4,column=1,padx=40)
        amount_label = Label(self.window, text="Amount (rate = 15 per hour)",bg='black',fg='white',font=('times new roman',20,'bold')).grid(row=3, column=0, padx=10, pady=50)
        amount_entry = Entry(self.window, textvariable=self.amount, bd=2,width = 40).grid(row=3, column=1, padx=50, pady=20)

    def exiter(self):
        et = datetime.datetime.now()
        self.date =date.today()
        self.exit_time = et.strftime("%H:%M:%S")
        self.vehicle_no = self.v_no.get()
        self.slot_number = self.slot_no.get()
        self.bill_amount = self.amount.get()
        # slot_no,cname,vehicle_no,contact,vehicle_size,address,rate,date,entry,exit_time
        mycursor.execute('update book_slot set exit_time = "{}" where vehicle_no = "{}" AND slot_no = "{}" AND date = "{}"'.format(self.exit_time,self.vehicle_no,self.slot_number,self.date))
        mydb.commit()
        mycursor.execute(
            'UPDATE slots_availability SET status = "yes" where slot_no = {}'.format(self.slot_number))
        mydb.commit()

        #filename = tempfile.mkdtemp(".doc")
        #sequence = []
        savefile = open ('C:/Users/Tarun/PycharmProjects/first/bill.txt','w').write(" Parkon Parking Management Solutions\n Vehicle No : {}\n Slot No : {}\n Bill AMount : {}\n".format(self.vehicle_no,self.slot_number,self.bill_amount))

        os.startfile('C:/Users/Tarun/PycharmProjects/first/bill.txt')
        messagebox.showerror('Notification',"Slot sucessfully freed")
        self.window.destroy()

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
        messagebox.showinfo("Having other issues ", "You can mail us at : raynold_tarun@gmail.com")

root=Tk()
c=Exiting(root)
root.mainloop()


