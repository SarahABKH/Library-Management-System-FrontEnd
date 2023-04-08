from tkinter import *

root=Tk()

def nextPage():
    root.destroy()
    import library

def prevPage():
    root.destroy()
    import page1
    

 

Label(
    root,
    text="This is Third page",
    padx=20,
    pady=20,
    bg='#ffbf00',
    font="Script"
    ).pack(expand=True, fill=BOTH)


Button(
    root, 
    text="Previous Page", 
    font="Script",
    command=nextPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

Button(      
    root, 
    text="Next Page", 
    font="Script",
    command=prevPage
    ).pack(fill=X, expand=TRUE, side=LEFT)
    

 
root.mainloop()