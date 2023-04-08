from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
def home():
    mainpage_window.destroy()
    import LibMain


def logout():
    mainpage_window.destroy()
    import signinlib

mainpage_window=Tk()
mainpage_window.geometry('1520x800+50+50')
mainpage_window.resizable(0,0)
mainpage_window.title('LEND A BOOK')
bgImage=ImageTk.PhotoImage(file=r'C:\Users\ASTECO J292\Desktop\library\Common2.png')
bgLabel=Label(mainpage_window,image=bgImage)
bgLabel.place(x=0,y=0)

frame=Frame(mainpage_window,bg="white")
frame.place(x=900,y=200)

Sign_out=Button(mainpage_window,text='SIGN OUT',bd=0,bg='#CBC4B6',activebackground='#CBC4B6' ,cursor='hand2',font=('MS Sans Serif',5,'bold'),fg='white',activeforeground='white',command=logout )
Sign_out.place(x=525,y=20)


Home=Button(mainpage_window,text='HOME',bd=0,bg='#CBC4B6',activebackground='#CBC4B6' ,cursor='hand2',font=('MS Sans Serif',5,'bold'),fg='white',activeforeground='white',command=home )
Home.place(x=1050,y=20)

ADD_BOOK=Label(mainpage_window,text='LEND A BOOK',font=('Microsoft Yahei UI Light',30,'bold'),fg='White',bg='#CBC4B6')
ADD_BOOK.place(x=700,y=40)

Book_Id=Label(frame,text='BOOK ID',font=('Microsoft Yahei UI Light',15,'bold'),bg='white',fg='#6B764C')
Book_Id.grid(row=3,column=0,sticky='w',padx=5,pady=(10,0))
Book_Id=Entry(frame,width=30,font=('Microsoft Yahei UI Light',15,'bold'),fg='white',bg='#6B764C')
Book_Id.grid(row=3,column=1,sticky='w',padx=5,pady=(10,0))

Member_Id=Label(frame,text='MEMBER ID',font=('Microsoft Yahei UI Light',15,'bold'),bg='white',fg='#6B764C')
Member_Id.grid(row=5,column=0,sticky='w',padx=5,pady=(10,0))
Member_Id=Entry(frame,width=30,font=('Microsoft Yahei UI Light',15,'bold'),fg='white',bg='#6B764C')
Member_Id.grid(row=5,column=1,sticky='w',padx=5,pady=(10,0))

 

 

AddButton=Button(frame,text='LEND BOOK',font=('Open Sans',16,'bold'),bd=0,bg='#6B764C',fg='white',activeforeground='white',width=17 )
AddButton.grid(row=25,column=1,pady=10)

 


  


mainpage_window.mainloop()