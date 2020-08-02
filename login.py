import mysql_connection
from tkinter import *
from tkinter import messagebox
#from PIL import ImageTk
import home
class Login_Screen:
    def __init__(self,root):
        self.root = root
        self.root.configure(background="white")
        self.root.title("Park-On Admin Login")
        self.root.geometry("600x400+0+0")

        # using images ;
        #self.bg_icon = ImageTk.PhotoImage(file = "bg_img.jpeg")

        # variables :
        self.uname = StringVar()
        self.password = StringVar()

        #bg_label = Label(self.root,bd=0,image = self.bg_icon).pack()

        title = Label(self.root, text = "Login Here ...", font = ("times new roman",40,"bold"),fg="black",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth = 1)
        Login_frame = Frame(self.root,bg="white")
        Login_frame.place(x=0,y=100)
        #logolbl = Label(Login_frame,image = self.logo_icon).grid(row=0,column=0,pady=20)
        lbluser = Label(Login_frame,text = "Username",font = ("times new roman",20,"bold")).grid(row=0,column=0,padx=20,pady=20)
        txtusername = Entry(Login_frame,bd=5,textvariable = self.uname,relief=GROOVE,font=("times new roman",20,"bold")).grid(row=0,column=1,padx=20,pady=20)
        lblpassword = Label(Login_frame, text="Password", font=("times new roman", 20, "bold")).grid(row=1, column=0,
                                                                                                 padx=20,pady=20)
        txtpassword = Entry(Login_frame, bd=5,textvariable = self.password, relief=GROOVE, font=("times new roman", 20, "bold")).grid(row=1,
                                                                                                         column=1,
                                                                                                         padx=20,
                                                                                                         pady=20)
        log_btn = Button(Login_frame,text = "Login",command = self.login, width = 15,font=("times new roman", 20, "bold"),bg="black",fg="red").grid(row=2,column=1,pady=10)

    def login(self):
        val = mysql_connection.login(self.uname.get(),self.password.get())
        if val==1:
            messagebox.showinfo("Welcome","Hi there Mr. Admin, Hope you have a nice day...")
            self.root.destroy()
            root = Tk()
            c = home.Home_page(root)
            root.mainloop()
        else:
            messagebox.showerror('Wrong credentials ', 'You have entered wrong credentials , please try again')




root = Tk()
obj = Login_Screen(root)
root.mainloop()