from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import  Image,ImageTk
from tkinter import ttk
import mysql.connector

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
        lbl_bg4 = Button(frame, image=self.bg4,cursor="hand2",borderwidth=0)
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









if __name__ == '__main__':
    root=Tk()
    obj=Register(root)
    root.mainloop()
