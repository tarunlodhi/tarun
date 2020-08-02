from tkinter import *
import os
from tkinter import messagebox
import booking_guide
from pandas import DataFrame
import search_guide
from PIL import ImageTk,Image

class Home_page:
    def __init__(self,root):
        root.geometry('1366x768+0+0')
        #Menu Code :
        root.configure(bg='black')
        menu = Menu(root)
        root.config(menu=menu)
        submenu = Menu(menu)
        submenu_2 = Menu(menu)
        submenu_3 = Menu(menu)
        submenu_4 = Menu(menu)
        menu.add_cascade(label = 'User Guide',menu= submenu)

        menu.add_cascade(label='Help', menu=submenu_2)
        menu.add_cascade(label='About', menu=submenu_3)
        menu.add_cascade(label = 'Logout',menu=submenu_4)

        #Configuring Submenus ...
        submenu.add_command(label='Booking Guides', command=self.ug_book)
        submenu.add_separator()
        submenu.add_command(label='Searching Guides', command=self.ug_search)
        submenu_2.add_command(label='Common Issues', command=self.help_ci)
        submenu_2.add_separator()
        submenu_2.add_command(label='Other Issues ?', command=self.help_oi)
        submenu_3.add_command(label='About Parkon System', command=self.about)
        submenu_4.add_command(label='Logout and Exit',command = root.destroy)

        title = Label(root, text="Welcome To Park-On Parking Solutions ...", font=("times new roman", 55, "bold"),
                      fg="black", bd=10, relief=GROOVE).pack()

        frm = Label(root,text = 'Your One stop destination for Parking Solutions...',font=("times new roman",38,'bold'),fg='white',bg='black',bd=10,relief = GROOVE).pack()
        lab = Label(root,text = '',bg='black').pack()
        tag_frame = Frame(root,bg='gray',bd=10,relief=GROOVE)
        tag_frame.place(x=150,y=50)
        tag_frame.pack()

        bike_label = Label(tag_frame, text='Bikes', font=('bold', 30), bg='gray', fg='white', bd=2).grid(row=0, column=0,
                                                                                                 padx=30, pady=30)
        car_label = Label(tag_frame,text = 'Cars',font = ('bold',30),bg='gray',fg='white',bd=2).grid(row=0,column=1,padx=100,pady=30)
        suv_label = Label(tag_frame, text='SUVs', font=('bold', 30), bg='gray', fg='white', bd=2).grid(row=0, column=2,
                                                                                                 padx=100, pady=30)
        trucks_label = Label(tag_frame, text='Trucks', font=('bold', 30), bg='gray', fg='white', bd=2).grid(row=0, column=3,
                                                                                                 padx=100, pady=30)
        buses_label = Label(tag_frame, text='Buses', font=('bold', 30), bg='gray', fg='white', bd=2).grid(row=0, column=4,
                                                                                                 padx=100, pady=30)
        lab2 = Label(root, text='', bg='black').pack()

        frm = Label(root, text='You can Park them all.Keep track of them and all the charges too..',
                    font=("times new roman", 35, 'bold'), fg='white', bg='black', bd=10, relief=GROOVE).pack()
        #self.bg_image = ImageTk.PhotoImage(file="bg_img.jpeg")
        bg_label = Label(root, bd=0, bg='black').pack()
        bg_label_2 = Label(root, bd=0, bg='black').pack()

        ops_frame = Frame(root, bg="black")
        ops_frame.place(x=500, y=900)
        ops_frame.pack()

        book_btn = Button(ops_frame, text="Book Slot",command = self.book_page, width=15, font=("times new roman", 20, "bold"), bg="black",
                          fg="red").grid(row=0, column=0, padx=30, pady=120)
        exit_btn = Button(ops_frame, text="Free an occupied slot",command = self.vehicle_exit_page, width=20, font=("times new roman", 20, "bold"),
                          bg="black", fg="red").grid(row=0, column=1, padx=30, pady=20)
        search_btn = Button(ops_frame, text="Search ",command = self.search, width=15, font=("times new roman", 20, "bold"), bg="black",
                            fg="red").grid(row=0, column=2, padx=30, pady=20)

    def book_page(self):
        os.startfile('C:/Users/Tarun/PycharmProjects/carparkingsolution/dist/book_page.exe')

    def vehicle_exit_page(self):
        os.startfile('C:/Users/Tarun/PycharmProjects/carparkingsolution/dist/vehicle_exit.exe')
    def search(self):
        os.startfile('C:/Users/Tarun/PycharmProjects/carparkingsolution/dist/search_page.exe')

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

'''root = Tk()
c=Home_page(root)
root.mainloop()'''