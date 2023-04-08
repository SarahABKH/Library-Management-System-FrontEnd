from tkinter import *
from PIL import ImageTk

def signup_page():
    login_window.destroy()
    import signupuser


def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)

def hide():
    openeye.config(file=r'C:\Users\ASTECO J292\Desktop\library\closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file=r'C:\Users\ASTECO J292\Desktop\library\openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)



login_window=Tk()
login_window.geometry('1520x800+50+50')
login_window.resizable(0,0)
login_window.title('Login')
bgImage=ImageTk.PhotoImage(file=r'C:\Users\ASTECO J292\Desktop\library\Common.png')


bgLabel=Label(login_window,image=bgImage)
bgLabel.grid()


frame=Frame(login_window,bg="white")
frame.place(x=1054,y=200)

heading=Label (frame, text='LOG IN', font=('Microsoft Yahei UI light',18,'bold'),bg='white',fg='#6B764C')
heading.grid(row=0,column=0,padx=10,pady=10) 


usernameLabel=Label(frame,text='Username',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='#6B764C')
usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))
usernameEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='#6B764C')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25) 
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',user_enter)

 

passwordLabel=Label(frame,text='Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='#6B764C')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))
passwordEntry=Entry(frame,width=25,font=('Microsoft Yahei UI',11,'bold'),fg='white',bg='#6B764C')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',password_enter)

 

openeye=PhotoImage(file=r'C:\Users\ASTECO J292\Desktop\library\openeye.png')
closeye=PhotoImage(file=r'C:\Users\ASTECO J292\Desktop\library\closeye.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=1320,y=350)


forgetButton=Button(frame,text='Forgot Password ?',bd=0,bg='white',activebackground='white',cursor='hand2',font=('Microsoft Yahei UI',9,'bold'),fg='#6B764C',activeforeground='#6B764C')
forgetButton.grid(row=8,column=0,sticky='w',padx=25)

loginButton=Button(frame,text='Login',font=('Open Sans',16,'bold'),fg='white',bg='#6B764C',activeforeground='white',activebackground="firebrick1",cursor='hand2',border=0,width=19)
loginButton.grid(row=10,column=0,pady=10)

signupLabel=Label(frame,text='Dont have an account ?',font=('Open Sans',9,'bold'),fg='#6B764C',bg='white')
signupLabel.grid(row=12,column=0,pady=10)

newaccountButton=Button(frame,text='Create new one',font=('Open Sans',9,'bold underline'),fg='#BA8673',bg='white',activeforeground='blue',activebackground="firebrick1",cursor='hand2',bd=0,command=signup_page)
newaccountButton.grid(row=14,column=0,pady=10)

login_window.mainloop()