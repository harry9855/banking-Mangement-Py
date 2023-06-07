from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import  Image,ImageTk
from tkinter import ttk
import mysql.connector
from bankingacc import BankingAccount
from loan import Loan
from fd import FD
from Insurance import Insurance

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()



class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x800+0+0")
        self.root.title("LOGIN")


        img= Image.open("E:\\python project\\images\\login.jpg")
        img = img.resize((1550, 880))
        self.bg = ImageTk.PhotoImage(img)
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relheight=1,relwidth=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=1140,y=170,width=340,height=450)

        img1=Image.open("E:\\python project\\images\\loginicon.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=1270,y=175,width=100,height=100)


        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=100,y=100)


        #labels
        #username

        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        #password
        password = lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"),show="*")
        self.txtpass.place(x=40, y=250, width=270)



        #-----Icon Image------
        img2 = Image.open("E:\\python project\\images\\username.jpg")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg2.place(x=1180, y=325, width=25, height=25)

        img3 = Image.open("E:\\python project\\images\\password.png")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg3.place(x=1180, y=395, width=25, height=25)


        #---button---
        loginbtn=Button(frame,text ="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",
                        bg="darkblue",activeforeground="white",activebackground="darkblue")
        loginbtn.place(x=110,y=300,width=120,height=35)
        #---register-----
        registerbtn = Button(frame, text="New User Register",command=self.register_windows, cursor="hand2",font=("times new roman", 10, "bold"),borderwidth=0, fg="white",bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=15,y=350, width=160)
        #----forgot----
        forgotbtn = Button(frame, text="Forgot Password", command=self.forgot_password_window,font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        forgotbtn.place(x=10, y=370, width=160)

    def register_windows(self):
        self.new_window=Toplevel(self.root)
        self.apps=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All Field Are Requried")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="HardikJain@090104",
                                           database="banking_managementdb")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                self.txtuser.get(),self.txtpass.get()
            ))

            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=HomepageClass(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

        #-----reset pass------
    def reset_pass(self):
        if self.combo_security_Q.get()=="":
            messagebox.showerror("Error", " Select the security question")
        elif self.txt_security.get()=="":
            messagebox.showerror("Error", "Please Enter the Answer")
        elif self.txtpass.get()=="":
            messagebox.showerror("Error", "Enter the new password")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="HardikJain@090104",
                                           database="banking_managementdb")
            my_cursor = conn.cursor()
            query=("select * from register where Email=%s and Security_Ques=%s and Security_Ans=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the correct answer",parent=self.root2)
            else:
                query=("update Register set password=%s where email=%s")
                values=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Congratulation","Your Password has been reset,please login",parent=self.root2)
                self.root2.destroy()


    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error"," Username field is Requried",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="HardikJain@090104",
                                           database="banking_managementdb")
            my_cursor = conn.cursor()
            query=("select * from register where Email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Please Enter The Valid Username",parent=self.root2)
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")
                l=Label(self.root2,text="Forgot Password",font=("times new roman", 15, "bold"), fg="white", bg="black")
                l.place(x=0,y=10,relwidth=1)

                security_Q = Label(self.root2, text="Security Question", font=("times new roman", 15, "bold"), fg="white",
                                   bg="black")
                security_Q.place(x=60, y=60)

                self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = (
                "Your Birth Place", "Your Girlfriend name", "your Pet Name", "Your Goals", "Your Fav Book")
                self.combo_security_Q.place(x=60, y=100, width=250)
                self.combo_security_Q.current(0)

                security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), fg="white",
                                   bg="black")
                security_A.place(x=60, y=140)

                self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.txt_security.place(x=60, y=180, width=250)

                new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), fg="white",
                                   bg="black")
                new_password.place(x=60, y=220)

                self.txt_newpass = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.txt_newpass.place(x=60, y=260, width=250)

                btn=Button(self.root2,text="Reset",font=("times new roman", 15, "bold"),fg="white",bg="green")
                btn.place(x=100,y=290)



class Register:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x900+0+0")
        self.root.title("REGISTER")

        # ----variable------
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()


        #-----bg img-------
        img = Image.open("E:\\python project\\images\\registerbg.jpg")
        img = img.resize((1600, 900))
        self.bg = ImageTk.PhotoImage(img)
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relheight=1, relwidth=1)

        #---left img------
        img1 = Image.open("E:\\python project\\images\\tech.webp")
        img1 = img1.resize((470, 550))
        self.bg1 = ImageTk.PhotoImage(img1)
        lbl_bg1 = Label(self.root, image=self.bg1)
        lbl_bg1.place(x=50, y=130, height=550,width=470)

        # ----main frame------
        frame=Frame(self.root,bg="black")
        frame.place(x=520,y=130,width=800,height=550)

        register_lbl=Label(frame,text = "REGISTER HERE",font=("times new roman",20,"bold"),fg="white",bg="black")
        register_lbl.place(x=20,y=20)

        #--label and entry---
        #row1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),fg="white",bg="black")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,font=("times new roman",15,"bold"),textvariable=self.var_fname)
        fname_entry.place(x=50,y=130,width=250)

        lname = Label(frame, text="Last Name", font=("times new roman", 15, "bold"),fg="white",bg="black")
        lname.place(x=370, y=100)

        self.txt_lname = ttk.Entry(frame, font=("times new roman", 15, "bold"),textvariable=self.var_lname)
        self.txt_lname.place(x=370, y=130, width=250)
        #row2

        contact = Label(frame, text="Contact No.", font=("times new roman", 15, "bold"),fg="white",  bg="black")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame, font=("times new roman", 15, "bold"),textvariable=self.var_contact)
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"),fg="white",  bg="black")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame, font=("times new roman", 15, "bold"),textvariable=self.var_email)
        self.txt_email.place(x=370, y=200, width=250)



        #row3
        security_Q=Label(frame, text="Security Question", font=("times new roman", 15, "bold"),fg="white",  bg="black")
        security_Q.place(x=50, y=240)

        self.combo_security_Q=ttk.Combobox(frame,font=("times new roman",15,"bold"),state="readonly",textvariable=self.var_securityQ)
        self.combo_security_Q["values"]=("Your Birth Place","Your Girlfriend name","your Pet Name","Your Goals","Your Fav Book")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)


        security_A=Label(frame, text="Security Answer", font=("times new roman", 15, "bold"),fg="white",  bg = "black")
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(frame, font=("times new roman", 15, "bold"),textvariable=self.var_securityA)
        self.txt_security.place(x=370, y=270, width=250)

        #row4
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",  bg="black")
        pswd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(frame, font=("times new roman", 15, "bold"),textvariable=self.var_pass)
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"),fg="white", bg="black")
        confirm_pswd.place(x=370, y=310)

        self.txt_confirm_pswd = ttk.Entry(frame, font=("times new roman", 15, "bold"),textvariable=self.var_confpass)
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        #---checkButton---
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,text="I Agree The Terms and Conditions",variable=self.var_check,font=("times new roman", 15, "bold"),fg="white", bg="black",activebackground="black",activeforeground="White",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        # ----button---
        img3 = Image.open("E:\\python project\\images\\register.jpg")
        img3 = img3.resize((200, 50))
        self.bg3 = ImageTk.PhotoImage(img3)
        lbl_bg3 = Button(frame, image=self.bg3,cursor="hand2",borderwidth=0,command=self.register_data)
        lbl_bg3.place(x=40, y=440,width=200,height=50)

        img4 = Image.open("E:\python project\images\loginow.jpg")
        img4 = img4.resize((200, 50))
        self.bg4 = ImageTk.PhotoImage(img4)
        lbl_bg4 = Button(frame, image=self.bg4,command=self.return_login,cursor="hand2",borderwidth=0)
        lbl_bg4.place(x=370, y=440, width=200, height=50)


        #---function---
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="":
            messagebox.showerror("Error","All Fields Are Required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password is not same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Accept the Terms and Condition")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="HardikJain@090104",
                                          database="banking_managementdb")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User Already Exist,Please try Another Email ")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),self.var_lname.get(),self.var_contact.get(),
                    self.var_email.get(),self.var_securityQ.get(),self.var_securityA.get(),
                    self.var_pass.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucess","Register Sucessful")

    def return_login(self):
        self.root.destroy()




class HomepageClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1980x1080")
        self.root.title("Banking Management")

        # ---------Top image-----------
        img1 = Image.open("E:\\python project\\images\\pvf.jpg")
        img1 = img1.resize((1480,140),Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(img1)
        label = Label(self.root,image=self.bg,bd=4,relief=RIDGE)
        label.place(x=100,y=0,width=1480,height=140)

        #---------Logo--------------------
        img2 = Image.open('E:\\python project\\images\\kc.jpg')
        img2 = img2.resize((230,140),Image.ANTIALIAS)
        self.bg1 = ImageTk.PhotoImage(img2)
        label = Label(self.root,image=self.bg1,bd=4,relief=RIDGE)
        label.place(x=0,y=0,width=230,height=140)


        #-------Title-----------
        lbl_title=Label(self.root,text="BANKING MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),
                        bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1580,height=50)

        #-------------Main Frame----------
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        #---------Menu---------------
        lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"),
                          bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        #------Button Menu-----------
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)

        NewAcc_btn=Button(btn_frame,text="ACCOUNT",command=self.account,width=22,font=("times new roman",14,"bold"),
                        bg="black",fg="gold",bd=0,cursor="hand2")
        NewAcc_btn.grid(row=0,column=0,pady=1)

        Loan_btn = Button(btn_frame, text="LOAN",command=self.loan_new, width=22, font=("times new roman", 14, "bold"),
                          bg="black", fg="gold", bd=0, cursor="hand2")
        Loan_btn.grid(row=1, column=0,pady=1)

        Fd_btn = Button(btn_frame, text="FIX DEPOSIT", command=self.fd,width=22, font=("times new roman", 14, "bold"),
                          bg="black", fg="gold", bd=0, cursor="hand2")
        Fd_btn.grid(row=2, column=0,pady=1)

        ins_btn = Button(btn_frame, text="INSURANCE", width=22,command=self.insurance, font=("times new roman", 14, "bold"),
                          bg="black", fg="gold", bd=0, cursor="hand2")
        ins_btn.grid(row=3, column=0,pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT", command=self.return_logins,width=22, font=("times new roman", 14, "bold"),
                              bg="black", fg="gold", bd=0, cursor="hand2")
        logout_btn.grid(row=4, column=0,pady=1)

        #------Right Side Image---------------

        img2 = Image.open('E:\\python project\\images\\kc.jpg')
        img2 = img2.resize((230, 140), Image.ANTIALIAS)
        self.bg1 = ImageTk.PhotoImage(img2)
        label = Label(self.root, image=self.bg1, bd=4, relief=RIDGE)
        label.place(x=0, y=0, width=230, height=140)


        #--------------right side image--------
        img3 = Image.open("E:\\python project\\images\\img.jpg")
        img3 = img3.resize((1350, 650), Image.ANTIALIAS)
        self.bg3 = ImageTk.PhotoImage(img3)
        label = Label(main_frame, image=self.bg3, bd=4, relief=RIDGE)
        label.place(x=225, y=0, width=1350, height=650)

        #----------Bottom Left img---------------
        img4 = Image.open("C:\\Users\\hp\\Downloads\\bank.jpg")
        img4 = img4.resize((230,210), Image.ANTIALIAS)
        self.bg4 = ImageTk.PhotoImage(img4)
        label = Label(main_frame, image=self.bg4, bd=4, relief=RIDGE)
        label.place(x=0, y=225, width=230, height=210)

        img5 = Image.open("E:\\python project\\images\\insurance-producer_16.jpg")
        img5 = img5.resize((230, 190), Image.ANTIALIAS)
        self.bg5 = ImageTk.PhotoImage(img5)
        label = Label(main_frame, image=self.bg5, bd=4, relief=RIDGE)
        label.place(x=0, y=420, width=230, height=190)

    def account(self):
        self.new_window=Toplevel(self.root)
        self.apps=BankingAccount(self.new_window)

    def loan_new(self):
        self.new_window=Toplevel(self.root)
        self.ap=Loan(self.new_window)

    def fd(self):
        self.new_window=Toplevel(self.root)
        self.hp=FD(self.new_window)

    def insurance(self):
        self.new_window=Toplevel(self.root)
        self.hpp=Insurance(self.new_window)

    def return_logins(self):
        open_mains=messagebox.askyesno("YesNo","Do you want to Logout",parent=self.root)
        if open_mains>0:
                    self.root.destroy()
        else:
                    return






if __name__ == '__main__':
    main()
