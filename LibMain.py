from tkinter import *
from PIL import ImageTk

def addbook():
    mainpage_window.destroy()
    import AddBook

def addmember():
    mainpage_window.destroy()
    import AddMember

def lendbook():
    mainpage_window.destroy()
    import LendBook

def search():
    mainpage_window.destroy()
    import Search

def returnbook():
    mainpage_window.destroy()
    import Return

def member():
    mainpage_window.destroy()
    import MemberProfile


 



mainpage_window=Tk()
mainpage_window.geometry('1520x800+50+50')
mainpage_window.resizable(0,0)
mainpage_window.title('Librarian Home Page')
bgImage=ImageTk.PhotoImage(file=r'C:\Users\ASTECO J292\Desktop\library\Common.png')
bgLabel=Label(mainpage_window,image=bgImage)
bgLabel.place(x=0,y=0)

frame=Frame(mainpage_window,bg="#BA8673")
frame.place(x=800,y=200)


AddBook_Button=Button(frame,text='ADD A BOOK',font=('Open Sans',20,'bold'),fg='white',bg='#BA8673',activeforeground='white',activebackground="#DDA38E",cursor='hand2',bd=0 ,command=addbook)
AddBook_Button.grid(row=1,column=0,padx=40,pady=20)

AddMember_Button=Button(frame,text='ADD A MEMBER ',font=('Open Sans',20,'bold'),fg='white',bg='#BA8673',activeforeground='white',activebackground="#DDA38E",cursor='hand2',bd=0,command=addmember )
AddMember_Button.grid(row=1,column=4,padx=20,pady=20)

LendBook_Button=Button(frame,text='LEND A BOOK',font=('Open Sans',20,'bold'),fg='white',bg='#BA8673',activeforeground='white',activebackground="#DDA38E",cursor='hand2',bd=0,command=lendbook )
LendBook_Button.grid(row=3,column=0,padx=40,pady=20)

Search_Button=Button(frame,text='SEARCH A BOOK',font=('Open Sans',20,'bold'),fg='white',bg='#BA8673',activeforeground='white',activebackground="#DDA38E",cursor='hand2',bd=0 ,command=search)
Search_Button.grid(row=3,column=4,padx=40,pady=20)

Return_Button=Button(frame,text='RETURN A BOOK',font=('Open Sans',20,'bold'),fg='white',bg='#BA8673',activeforeground='white',activebackground="#DDA38E",cursor='hand2',bd=0 ,command=returnbook)
Return_Button.grid(row=5,column=0,padx=40,pady=20)

Member_Button=Button(frame,text='MEMBER PROFILE',font=('Open Sans',20,'bold'),fg='white',bg='#BA8673',activeforeground='white',activebackground="#DDA38E",cursor='hand2',bd=0,command=member )
Member_Button.grid(row=5,column=4,padx=40,pady=20)









mainpage_window.mainloop()