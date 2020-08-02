from tkinter import *
from tkinter import messagebox
import booking_guide
import search_guide


class Info:
    def __init__(self,root):
        self.root = root
        self.root.configure(bg='black')
        self.root.geometry('1366x768+0+0')

        menu = Menu(root)
        root.config(menu=menu)
        submenu = Menu(menu)
        submenu_2 = Menu(menu)
        submenu_3 = Menu(menu)
        submenu_4 = Menu(menu)
        menu.add_cascade(label='User Guide', menu=submenu)

        menu.add_cascade(label='Help', menu=submenu_2)
        menu.add_cascade(label='About', menu=submenu_3)
        menu.add_cascade(label='Exit Booking Guide Page',command = self.root.destroy)

        # Configuring Submenus ...
        submenu.add_command(label='Booking Guides', command=self.ug_book)
        submenu.add_separator()
        submenu.add_command(label='Searching Guides', command=self.ug_search)
        submenu_2.add_command(label='Common Issues', command=self.help_ci)
        submenu_2.add_separator()
        submenu_2.add_command(label='Other Issues ?', command=self.help_oi)
        submenu_3.add_command(label='About Parkon System', command=self.about)

        lx=Label(self.root,bg='black').pack()
        f_1 = Frame(self.root,bg = 'black',bd=0,relief = GROOVE)
        f_1.place(x=0, y=100)
        f_1.pack()
        cust_name = Label(f_1,text = 'Customer Name         ',bg='black',fg='yellow',width = 20,font = ('bold',25)).grid(row = 0,column =0,padx=20,pady=20)
        cn_info = Label(f_1,text = 'It should only contain Alphabets and not numbers. Length must be upto 50 or it would not accept the name.',bg='black',fg='yellow',font=('bold',15))
        cn_info.grid(row = 1,column =0,padx=15,pady=10)
        lab1 = Label(f_1, text='             ', bg='black', fg='white').grid(row=0, column=1, padx=50, pady=10)
        lab2 = Label(f_1, text='             ', bg='black', fg='white').grid(row=0, column=2, padx=50, pady=10)
        lab3 = Label(f_1, text='             ', bg='black', fg='white').grid(row=0, column=3, padx=50, pady=10)
        lab4 = Label(f_1, text='             ', bg='black', fg='white').grid(row=0, column=4, padx=50, pady=10)
        f = Frame(self.root, bg='black', bd=0, relief=GROOVE)
        f.place(x=0, y=100)
        f.pack()
        ip_label = Label(f, text='Input formats : ', bg='black', fg='yellow', width=20, font=('bold', 25)).grid(row=0,
                                                                                                                column=0,
                                                                                                                padx=20,
                                                                                                                pady=10)
        lab5 = Label(f, text='             ', bg='black', fg='white').grid(row=0, column=1, padx=50, pady=10)
        lab6 = Label(f, text='             ', bg='black', fg='white').grid(row=0, column=2, padx=50, pady=10)
        lab7 = Label(f, text='             ', bg='black', fg='white').grid(row=0, column=3, padx=50, pady=10)
        lab8 = Label(f, text='             ', bg='black', fg='white').grid(row=0, column=4, padx=50, pady=10)

        ip_info = Label(f,
                        text='Contact : Numeric values (10 digits),Name : Alphabets(50 max),Address : alphanumeric values.',
                        bg='black', fg='yellow', font=('bold', 15))
        ip_info_2 = Label(f,
                        text='Slot number : Numeric (3 digits max). Please do not leave any fields empty or it will throw error.',
                        bg='black', fg='yellow', font=('bold', 15))
        ip_info.grid(row=1, column=0, padx=15, pady=10)
        ip_info_2.grid(row=2, column=0, padx=15, pady=10)

        f_2 = Frame(self.root, bg='black', bd=0, relief=GROOVE)
        f_2.place(x=0, y=100)
        f_2.pack()
        time_name = Label(f_2, text='Entry Time/date     ',bg='black',fg='yellow', width=20, font=('bold', 25)).grid(row=0, column=0, padx=20,
                                                                                       pady=10)
        lab9 = Label(f_2, text='             ', bg='black', fg='white').grid(row=0, column=1, padx=50, pady=10)
        lab10 = Label(f_2, text='             ', bg='black', fg='white').grid(row=0, column=2, padx=50, pady=10)
        lab11 = Label(f_2, text='             ', bg='black', fg='white').grid(row=0, column=3, padx=50, pady=10)
        #lab12 = Label(f_2, text='             ', bg='green', fg='white').grid(row=0, column=4, padx=50, pady=10)
        t_info = Label(f_2,
                        text='No need to input it. System automatically registers the booking time and booking date.Same for Exiting.',bg='black',fg='yellow',
                        font=('bold', 15))
        t_info.grid(row=1, column=0, padx=15, pady=10)

        f_3 = Frame(self.root, bg='black', bd=0, relief=GROOVE)
        f_3.place(x=0, y=100)
        f_3.pack()
        vehicle_sizes = Label(f_3, text='Vehicle Sizes               ',bg='black',fg='yellow', width=20, font=('bold', 25)).grid(row=0, column=0, padx=20,
                                                                                             pady=10)
        lab12 = Label(f_3, text='             ', bg='black', fg='white').grid(row=0, column=1, padx=50, pady=10)
        lab13 = Label(f_3, text='             ', bg='black', fg='white').grid(row=0, column=2, padx=50, pady=10)
        lab14 = Label(f_3, text='             ', bg='black', fg='white').grid(row=0, column=3, padx=50, pady=10)
        lab15 = Label(f_3, text='             ', bg='black', fg='white').grid(row=0, column=4, padx=50, pady=10)
        size_info = Label(f_3,
                       text='Enter "Small" for : Cars and bikes, "Medium" for : SUVs , Vans , Mini Buses, "Large" for : Busses and Trucks..',bg='black',fg='yellow',
                       font=('bold', 15))
        size_info.grid(row=1, column=0,padx=16,  pady=10)
        labl=Label(self.root,bg='black').pack()

        final = Label(self.root,text = "Once you click on the Book Button , It'll redirect you back to home page.",bg='black',fg='yellow',font = ('times new roman',25,'bold'))
        final.place(x=0,y=200)
        final.pack()
        final_2 = Label(self.root, text="All the data will be stored into database.",bg='black',fg='yellow',font = ('times new roman',30,'bold'))
        final_2.place(x=0,y=300)
        final_2.pack()

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

