import pymysql
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
  
import phonenumbers as pn

def connect_database():
    if PhoneLabel.get()=='' or usernameEntry.get()=='' or passwordEntry.get()==''or confirmEntry.get()=='':
        messagebox.showerror('Error','All Fields are required')
    elif passwordEntry.get() !=confirmEntry.get():
        messagebox.showerror('Error','Passwords must match')
    elif check.get()==0:
        messagebox.showerror('Error','Please accept Terms and Conditions')
    #elif (not (pn.is_possible_number(PhoneLabel.get()))) :
       # messagebox.showerror('Enter a valid phone number')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='30sh12128')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue, Please Try Again')
            return
        try:
            query='create database Library'
            mycursor.execute(query)
            query='use Library'
            query='create table Librarian(Lib_Id int auto_increment primary key not null,Lib_Phone varchar(10),Lib_name varchar(20),password varchar(20) )'
            mycursor.execute(query)
        except:
            mycursor.execute('use Library')

def login_page():
    signup_window.destroy()
    import signinuser

    

signup_window=Tk()
signup_window.title('Signup Page')
signup_window.geometry('1520x800+50+50')
signup_window.resizable(False,False)
background=ImageTk.PhotoImage(file=r"C:\Users\ASTECO J292\Desktop\Library\Common.png")

bgLabel=Label(signup_window,image=background)
bgLabel.grid()

frame=Frame(signup_window,bg="white")
frame.place(x=1054,y=200)

heading=Label (frame, text='CREATE AN ACCOUNT', font=('Microsoft Yahei UI light',18,'bold'),bg='white',fg='#6B764C')
heading.grid(row=0,column=0,padx=10,pady=10)

PhoneLabel=Label(frame,text='Phone',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='#6B764C')
PhoneLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))
PhoneLabel=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='#6B764C')
PhoneLabel.grid(row=2,column=0,sticky='w',padx=25)



usernameLabel=Label(frame,text='Username',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='#6B764C')
usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))
usernameEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='#6B764C')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

passwordLabel=Label(frame,text='Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='#6B764C')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))
passwordEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='#6B764C')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)

confirmLabel=Label(frame,text='Confirm Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='#6B764C')
confirmLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))
confirmEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='#6B764C',bg='#6B764C')
confirmEntry.grid(row=8,column=0,sticky='w',padx=25)

check=IntVar()
termsandcondition=Checkbutton(frame,text='I agree to the Terms and Conditions',font=('Microsoft Yahei UI Light',9,'bold'),fg='#6B764C',bg='white',activebackground='white',activeforeground='firebrick1',cursor='hand2',variable=check)

termsandcondition.grid(row=9,column=0,pady=10,padx=15)

signupButton=Button(frame,text='Signup',font=('Open Sans',16,'bold'),bd=0,bg='#6B764C',activeforeground='white',width=17,command=connect_database)
signupButton.grid(row=10,column=0,pady=10)

alreadyaccount=Label(frame,text="Already have an account ?",font=('Open Sans','9','bold'),bg='white',fg='#6B764C')
alreadyaccount.grid(row=11,column=0,sticky='w',padx=25,pady=10)

loginButton=Button(frame,text='Log In',font=('Open Sans',9,'bold underline'),bg='white',fg='#BA8673',bd=0,cursor='hand2',activebackground='white',activeforeground='blue',command=login_page)
loginButton.place(x=170,y=404)
signup_window.mainloop()





