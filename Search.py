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
mainpage_window.title('SEARCH A BOOK')
bgImage=ImageTk.PhotoImage(file=r'C:\Users\ASTECO J292\Desktop\library\Common2.png')
bgLabel=Label(mainpage_window,image=bgImage)
bgLabel.place(x=0,y=0)

frame=Frame(mainpage_window,bg="white")
frame.place(x=900,y=200)

Sign_out=Button(mainpage_window,text='SIGN OUT',bd=0,bg='#CBC4B6',activebackground='#CBC4B6' ,cursor='hand2',font=('MS Sans Serif',5,'bold'),fg='white',activeforeground='white', command=logout )
Sign_out.place(x=525,y=20)


Home=Button(mainpage_window,text='HOME',bd=0,bg='#CBC4B6',activebackground='#CBC4B6' ,cursor='hand2',font=('MS Sans Serif',5,'bold'),fg='white',activeforeground='white',command=home )
Home.place(x=1050,y=20)

ADD_BOOK=Label(mainpage_window,text='SEARCH A BOOK',font=('Microsoft Yahei UI Light',30,'bold'),fg='White',bg='#CBC4B6')
ADD_BOOK.place(x=650,y=20)



options = [
    "ISBN",
    "Title",
    "Publisher Name",
    "Author" 
]

clicked = StringVar()
clicked.set( "Search by :" )

drop = OptionMenu( mainpage_window , clicked , *options )
drop.config(bg = "#8F9D67",font=('Microsoft Yahei UI Light',15,'bold'),fg="white")
drop.place(x=1050,y=200)

NAMEEntry=Entry(mainpage_window,width=30,font=('Microsoft Yahei UI Light',15,'bold'),fg='white',bg='#8F9D67')
NAMEEntry.place(x=1050,y=250)

SearchButton=Button(mainpage_window,text='SEARCH FOR BOOK',font=('Microsoft Yahei UI Light',16,'bold'),bd=0,bg='#8F9D67',fg='white',activeforeground='white',width=17 )
SearchButton.place(x=1050,y=300)









mainpage_window.mainloop()