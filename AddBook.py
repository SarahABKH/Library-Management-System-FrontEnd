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
mainpage_window.title('ADD A BOOK')
bgImage=ImageTk.PhotoImage(file=r'C:\Users\ASTECO J292\Desktop\library\Common2.png')
bgLabel=Label(mainpage_window,image=bgImage)
bgLabel.place(x=0,y=0)

frame=Frame(mainpage_window,bg="white")
frame.place(x=900,y=200)

Sign_out=Button(mainpage_window,text='SIGN OUT',bd=0,bg='#CBC4B6',activebackground='#CBC4B6' ,cursor='hand2',font=('MS Sans Serif',5,'bold'),fg='white',activeforeground='white',command=logout )
Sign_out.place(x=525,y=20)


Home=Button(mainpage_window,text='HOME',bd=0,bg='#CBC4B6',activebackground='#CBC4B6' ,cursor='hand2',font=('MS Sans Serif',5,'bold'),fg='white',activeforeground='white',command=home )
Home.place(x=1050,y=20)

ADD_BOOK=Label(mainpage_window,text='ADD A BOOK',font=('Microsoft Yahei UI Light',30,'bold'),fg='White',bg='#CBC4B6')
ADD_BOOK.place(x=710,y=20)

new_var = 10
Title=Label(frame,text='TITLE',font=('Microsoft Yahei UI Light',15,'bold'),bg='white',fg='#6B764C')
Title.grid(row=3,column=0,sticky='w',padx=5,pady=(10,0))
TitleEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',15,'bold'),fg='white',bg='#6B764C')
TitleEntry.grid(row=3,column=1,sticky='w',padx=5,pady=(10,0))

ISBN=Label(frame,text='BOOK ISBN',font=('Microsoft Yahei UI Light',15,'bold'),bg='white',fg='#6B764C')
ISBN.grid(row=5,column=0,sticky='w',padx=5,pady=(10,0))
ISBNEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',15,'bold'),fg='white',bg='#6B764C')
ISBNEntry.grid(row=5,column=1,sticky='w',padx=5,pady=(10,0))

Pub_Year=Label(frame,text='PUBLISH YEAR',font=('Microsoft Yahei UI Light',15,'bold'),bg='white',fg='#6B764C')
Pub_Year.grid(row=7,column=0,sticky='w',padx=5,pady=(10,0))
Pub_YearEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',15,'bold'),fg='white',bg='#6B764C')
Pub_YearEntry.grid(row=7,column=1,sticky='w',padx=5,pady=(10,0))

Pub_Name=Label(frame,text='PUBLISHER NAME',font=('Microsoft Yahei UI Light',15,'bold'),bg='white',fg='#6B764C')
Pub_Name.grid(row=9,column=0,sticky='w',padx=5,pady=(10,0))
Pub_YearEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',15,'bold'),fg='white',bg='#6B764C')
Pub_YearEntry.grid(row=9,column=1,sticky='w',padx=5,pady=(10,0))

Author_Name=Label(frame,text='AUTHOR',font=('Microsoft Yahei UI Light',15,'bold'),bg='white',fg='#6B764C')
Author_Name.grid(row=11,column=0,sticky='w',padx=5,pady=(10,0))
Author_NameEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',15,'bold'),fg='white',bg='#6B764C')
Author_NameEntry.grid(row=11,column=1,sticky='w',padx=5,pady=(10,0))

Category=Label(frame,text='CATEGORY',font=('Microsoft Yahei UI Light',15,'bold'),bg='white',fg='#6B764C')
Category.grid(row=13,column=0,sticky='w',padx=5,pady=(10,0))
Category_Entry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',15,'bold'),fg='white',bg='#6B764C')
Category_Entry.grid(row=13,column=1,sticky='w',padx=5,pady=(10,0))


Category=Label(frame,text='NO OF COPIES',font=('Microsoft Yahei UI Light',15,'bold'),bg='white',fg='#6B764C')
Category.grid(row=15,column=0,sticky='w',padx=5,pady=(10,0))
Category_Entry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',15,'bold'),fg='white',bg='#6B764C')
Category_Entry.grid(row=15,column=1,sticky='w',padx=5,pady=(10,0))

AddButton=Button(frame,text='ADD BOOK',font=('Open Sans',16,'bold'),bd=0,bg='#6B764C',fg='white',activeforeground='white',width=17 )
AddButton.grid(row=25,column=1,pady=10)




mainpage_window.mainloop()