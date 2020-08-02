from tkinter import *
from tkinter import messagebox
import booking_guide
import search_guide


class Info:
    def __init__(self,root):
        self.root = root
        self.root.configure(bg = 'black')
        self.root.geometry('1366x768+0+0')

        menu = Menu(root)
        self.root.config(menu=menu)
        submenu = Menu(menu)
        submenu_2 = Menu(menu)
        submenu_3 = Menu(menu)
        #submenu_4 = Menu(menu)
        menu.add_cascade(label='User Guide', menu=submenu)

        menu.add_cascade(label='Help', menu=submenu_2)
        menu.add_cascade(label='About', menu=submenu_3)
        menu.add_cascade(label='Exit Search Page', command = self.root.destroy)

        # Configuring Submenus ...
        submenu.add_command(label='Booking Guides', command=self.ug_book)
        submenu.add_separator()
        submenu.add_command(label='Searching Guides', command=self.ug_search)
        submenu_2.add_command(label='Common Issues', command=self.help_ci)
        submenu_2.add_separator()
        submenu_2.add_command(label='Other Issues ?', command=self.help_oi)
        submenu_3.add_command(label='About Parkon System', command=self.about)

        f_1 = Frame(self.root, bg='black', bd=0, relief=GROOVE)
        f_1.place(x=0, y=0)
        f_1.pack()

        method = Label(f_1,text = 'Methods for Searching',bg='black',fg='white',font = ('bold',40)).grid(row=0,column=0,padx=20,pady=20)
        lab1 = Label(f_1,text = '                                                            ',bg='black').grid(row=0,column=1,padx=20,pady=20)
        labx = Label(f_1, text='                                                            ', bg='black').grid(row=0,
                                                                                                                column=3,
                                                                                                                padx=20,
                                                                                                                pady=20)
        lab2 = Label(f_1,text = '                                                            ',bg='black').grid(row=0, column=2, padx=20, pady=20)
        m_1 = Label(f_1,text = "1. Search By Vehicle Number (Individual)",bg='black',fg='green' , font=('bold',20)).grid(row=1,column=0,padx=0,pady=20)
        lab3 = Label(f_1, text='                                                            ',bg='black').grid(row=1, column=1,
                                                                                                    padx=20, pady=20)
        lab4 = Label(f_1, text='                                                            ',bg='black').grid(row=1, column=2,
                                                                                                    padx=20, pady=20)
        laby = Label(f_1, text='                                                            ', bg='black').grid(row=1,
                                                                                                                column=4,
                                                                                                                padx=20,
                                                                                                                pady=20)
        labz = Label(f_1, text='                                                            ', bg='black').grid(row=1,
                                                                                                                column=5,
                                                                                                                 padx=20,
                                                                                                                pady=20)

        m_2 = Label(f_1, text="2. Search By Date(YYYY-MM-DD) (All :)",bg='black',fg='green', font=('bold', 20)).grid(row=2, column=0, padx=50, pady=20)

        title = Label(self.root , text = 'Method 1',bg='black',fg='white',font = ('bold',40))
        title.pack()
        lab = Label(self.root,bg='black').pack()
        m_1_info = Label(self.root,text = 'By using Vechile Number you can search record of certain individual.',bg='black',fg = 'yellow',font = ('bold',20)).pack()
        m1_extra = Label(self.root,text = 'Information includes : Name,Address,Contact , Entry and Exit Time.',bg='black',fg='yellow',font = ('bold',20)).pack()

        lab2 = Label(self.root, bg='black').pack()

        tx = Label(self.root,text = 'Method 2',bg='black',fg='white',font = ('bold',40)).pack()
        lab3 = Label(self.root, bg='black').pack()
        m_2_info = Label(self.root, text='By using Date you can search all record of certain date.',bg='black',fg='red',
                         font=('bold', 20)).pack()
        m2_extra = Label(self.root, text='Information fetched : It will display all the registries on given date.',bg='black',fg='red',
                         font=('bold', 20)).pack()

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
