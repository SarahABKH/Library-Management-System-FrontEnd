from tkinter import *


class LibraryManagementSystem :
    root =Tk()
    
    def __init__(self,root):
        def nextPage():
            root.destroy()
            import page1

        def prevPage():
            root.destroy()
            import page2
            
 


        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")
        
        

        lbtitle=Label (self.root, text="Library Management System", bg= "#44318D", fg="#E98074" ,bd=20,relief=RIDGE,font= ( "Script",50,"bold"),padx=4,pady=6)
        lbtitle.pack(side=TOP,fill= X)

        label1= Label(self.root,text="Login",padx=20,pady=20,bg="#E98074",font ="Script")
        label1.pack(expand=True,fill=BOTH)

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
    

        frame =Frame(self.root,bd=12,relief=SUNKEN ,padx=20,bg="#8860D0")
        frame.place(x=0,y=130,width=1530,height=400)

        
    

       
if __name__ == "__main__" :
        root=Tk()
        obj= LibraryManagementSystem(root)
        root.mainloop()

    
    

   

