from tkinter import *
from PIL import ImageTk

def user_login():
    mainpage_window.destroy()
    import signinuser

def lib_login():
    mainpage_window.destroy()
    import signinlib 

mainpage_window=Tk()
mainpage_window.geometry('1520x800+50+50')
mainpage_window.resizable(0,0)
mainpage_window.title('Library Management System')
bgImage=ImageTk.PhotoImage(file=r'C:\Users\ASTECO J292\Desktop\library\MainPage3.png')
bgLabel=Label(mainpage_window,image=bgImage)
bgLabel.place(x=0,y=0)

#AboutButton=Button(mainpage_window,text='About',bd=0,bg='#190061',activebackground='#190061' ,cursor='hand2',font=('Selima',13,'bold'),fg='white',activeforeground='white')
#AboutButton.place(x=280,y=125)
 
userlog_Button=Button(mainpage_window,text='User Log In',bd=0,bg='#CBC4B6',activebackground='#CBC4B6' ,cursor='hand2',font=('MS Sans Serif',30,'bold'),fg='white',activeforeground='white',command=user_login)
userlog_Button.place(x=1050,y=450)

liblog_Button=Button(mainpage_window,text='Librarian Log In',bd=0,bg='#CBC4B6',activebackground='#CBC4B6' ,cursor='hand2',font=('MS Sans Serif',30,'bold'),fg='white',activeforeground='white',command=lib_login)
liblog_Button.place(x=1050,y=250)

mainpage_window.mainloop()
