from tkinter import *
from PIL import ImageTk, Image
from bankingacc import BankingAccount
from loan import Loan
from fd import FD
from Insurance import Insurance

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

        logout_btn = Button(btn_frame, text="LOGOUT", width=22, font=("times new roman", 14, "bold"),
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
        self.app=BankingAccount(self.new_window)

    def loan_new(self):
        self.new_window=Toplevel(self.root)
        self.ap=Loan(self.new_window)

    def fd(self):
        self.new_window=Toplevel(self.root)
        self.hp=FD(self.new_window)

    def insurance(self):
        self.new_window=Toplevel(self.root)
        self.hpp=Insurance(self.new_window)






if __name__ == '__main__':
    root=Tk()
    obj=HomepageClass(root)
    root.mainloop()

