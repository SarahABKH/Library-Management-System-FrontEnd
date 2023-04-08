from tkinter import *
from PIL import ImageTk

 

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

 

Member_Button=Button(frame,text='VIEW MEMBER PROFILE',font=('Open Sans',20,'bold'),fg='white',bg='#BA8673',activeforeground='white',activebackground="#DDA38E",cursor='hand2',bd=0,command=member )
Member_Button.grid(row=5,column=4,padx=40,pady=20)









mainpage_window.mainloop()