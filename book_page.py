import datetime
from datetime import date
from tkinter import messagebox
import booking_guide
import search_guide
#import mysql_connection
from tkinter import *
import mysql.connector as mcon
mydb = mcon.connect(host = "localhost",user = "root",passwd = "tarun@12345",database = "Parkon")
mycursor = mydb.cursor()

class Book_Slot:
    def __init__(self,root):
        self.root = root
        self.root.geometry('800x800')
        self.root.configure(bg='black')
        self.root.title('Book Slot')

        menu = Menu(root)
        self.root.config(menu=menu)
        submenu = Menu(menu)
        submenu_2 = Menu(menu)
        submenu_3 = Menu(menu)
        #submenu_4 = Menu(menu)
        menu.add_cascade(label='User Guide', menu=submenu)

        menu.add_cascade(label='Help', menu=submenu_2)
        menu.add_cascade(label='About', menu=submenu_3)
        menu.add_cascade(label='Exit Booking page', command = root.destroy)

        # Configuring Submenus ...
        submenu.add_command(label='Booking Guides', command=self.ug_book)
        submenu.add_separator()
        submenu.add_command(label='Searching Guides', command=self.ug_search)
        submenu_2.add_command(label='Common Issues', command=self.help_ci)
        submenu_2.add_separator()
        submenu_2.add_command(label='Other Issues ?', command=self.help_oi)
        submenu_3.add_command(label='About Parkon System', command=self.about)
        #submenu_4.add_command(label='Exit Booking Page', command=root.destroy)

        self.v_type = StringVar()
        self.c_name = StringVar()
        self.contact = StringVar()
        self.address = StringVar()
        self.vehicle_no = StringVar()
        self.slot_no = StringVar()

        label = Label(self.root, width=50, text=' ', bg='black').pack()
        label_ = Label(self.root, width=50, text=' ', bg='black').pack()
        label_0 = Label(self.root, text='Book slot for parking', bg='gray',fg = 'white', width=40, font=('bold', 20))
        label_0.place(x=90, y=50)
        label_0.pack()
        form_frame = Frame(self.root, bg="black")
        form_frame.place(x=100, y=400)
        form_frame.pack()

        label_1 = Label(form_frame, bg='black',fg='white', text='Customer Name', width=20, font=('bold', 20)).grid(row=0, column=0,
                                                                                                        padx=20,
                                                                                                        pady=20)
        entry_1 = Entry(form_frame, textvariable=self.c_name, relief=GROOVE, bd=2,
                        font=("times new roman", 15, "bold")).grid(row=0, column=1, padx=20, pady=20)

        label_2 = Label(form_frame, bg='black',fg='white', text='Vehicle No', width=20, font=('bold', 20)).grid(row=1, column=0,
                                                                                                     padx=20, pady=20)
        entry_2 = Entry(form_frame, textvariable=self.vehicle_no, relief=GROOVE, bd=2,
                        font=("times new roman", 15, "bold")).grid(row=1, column=1, padx=20, pady=20)

        label_3 = Label(form_frame, bg='black',fg='white', text='Contact No', width=20, font=('bold', 20)).grid(row=2, column=0,
                                                                                                     padx=20, pady=20)
        entry_3 = Entry(form_frame, relief=GROOVE, bd=2, textvariable=self.contact,
                        font=("times new roman", 15, "bold")).grid(row=2, column=1, padx=20, pady=20)

        label_wild = Label(form_frame, bg='black',fg='white', text='Vehicle Type', width=20, font=('bold', 20)).grid(row=3,
                                                                                                          column=0,
                                                                                                          padx=20,
                                                                                                          pady=20)
        entry_type = Entry(form_frame, relief=GROOVE, bd=2, textvariable=self.v_type,
                           font=("times new roman", 15, "bold")).grid(row=3, column=1, padx=20, pady=20)

        #label_wild_2 = Label(form_frame, bg='black',fg='white', text='Slot No', width=20, font=('bold', 20)).grid(row=4, column=0,
         #                                                                                              padx=20, pady=20)
        #entry_s_number = Entry(form_frame, relief=GROOVE, bd=2, textvariable=self.slot_no,
          #                     font=("times new roman", 15, "bold")).grid(row=4, column=1, padx=20, pady=20)

        label_4 = Label(form_frame, bg='black',fg='white', text='Address', width=20, font=('bold', 20)).grid(row=5, column=0,
                                                                                                  padx=20, pady=20)
        entry_4 = Entry(form_frame, relief=GROOVE, textvariable=self.address, bd=2,
                        font=("times new roman", 15, "bold")).grid(row=5, column=1, padx=20, pady=20)
        label__x = Label(self.root, width=50, text=' ', bg='black').pack()
        btn_frame = Frame(self.root, bg="black")
        btn_frame.place(x=300, y=600)
        btn_frame.pack()
        book_btn = Button(btn_frame, bg='gray', command=self.book, text='Book Slot', font=('times new roman', 20, 'bold'),
                          fg='white', width=20).grid(row=6)

    def book(self):
        name = self.c_name.get()
        v_no = self.vehicle_no.get()
        address_cust = self.address.get()
        vehicle_type = self.v_type.get()
        contact_no = self.contact.get()
        rate = 15
        mycursor.execute('select min(slot_no) from slots_availability where status="yes"')
        for i in mycursor:
            for x in i:
                s_no=x
        #s_no = self.slot_no.get()
        e_t = datetime.datetime.now()
        e_time = e_t.strftime("%H:%M:%S")
        e_date = date.today()
        mycursor.execute(
            'insert into book_slot values("{}","{}","{}","{}","{}","{}",{},"{}","{}","{}")'.format(s_no,
                                                                                                   name,
                                                                                                   v_no,
                                                                                                   contact_no,
                                                                                                   vehicle_type,
                                                                                                   address_cust,
                                                                                                   rate,
                                                                                                   e_date,
                                                                                                   e_time,
                                                                                                   0))
        mydb.commit()
        mycursor.execute('update slots_availability set status = "no" where slot_no = {}'.format(s_no))
        mydb.commit()
        messagebox.showinfo('Slot Booked', 'Slot number {} sucessfully booked by {}'.format(s_no, name))
        self.root.destroy()

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
c=Book_Slot(root)
root.mainloop()