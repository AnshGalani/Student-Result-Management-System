import imp
from logging import root
from tkinter import*
from tkinter import ttk,messagebox
from tokenize import String
from PIL import Image,ImageTk
import sqlite3
class ReportClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Managemeny System")
        self.root.geometry("1350x575+80+175")
        self.root.config(bg="white")
        self.root.focus_force()
        
        #=======================Title================================
        
        title=Label(self.root,text="View Student Result",font=('goudy old style',20,"bold"),bg="orange",fg="#060606").place(x=10,y=15,width=1330,height=50)

        #================Search=========================
        
        self.var_search=StringVar()
        self.var_id=""
        
        lbl_search=Label(self.root,text="Search By Roll No.",font=("goudy old style",20,"bold"),bg="white").place(x=330,y=100)
        txt_search=Entry(self.root,textvariable=self.var_search,font=("goudy old style",20,),bg="lightyellow").place(x=570,y=100,width=150)
        
        btn_search=Button(self.root,text="Search",command=self.search,font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2").place(x=730,y=100,width=100,height=35)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15,"bold"),bg="gray",fg="white",cursor="hand2").place(x=850,y=100,width=100,height=35)
        
        #===================Result Labels===============================
        
        lbl_roll=Label(self.root,text="Roll No.",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=200,y=230,width=150,height=50)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=350,y=230,width=150,height=50)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=500,y=230,width=150,height=50)
        lbl_mark=Label(self.root,text="Mark Obtained",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=650,y=230,width=150,height=50)
        lbl_full=Label(self.root,text="Total Mark",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=800,y=230,width=150,height=50)
        lbl_per=Label(self.root,text="Percentage",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=950,y=230,width=150,height=50)

        #===============Result Show in Table===================
        
        self.roll=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.roll.place(x=200,y=280,width=150,height=50)
        self.name=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.name.place(x=350,y=280,width=150,height=50)
        self.course=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.course.place(x=500,y=280,width=150,height=50)
        self.mark=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.mark.place(x=650,y=280,width=150,height=50)
        self.full=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.full.place(x=800,y=280,width=150,height=50)
        self.per=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.per.place(x=950,y=280,width=150,height=50)

        #====================Button Delete===========================
        
      
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15,"bold"),bg="red",fg="white",cursor="hand2").place(x=570,y=400,width=150,height=35)

#==============================================================================================================================

    #===============================Search=====================================
    
    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Roll No. Should be Required",parent=self.root)
            else: 
                cur.execute(f"select * from result where roll=?",(self.var_search.get(),))
                row=cur.fetchone()
                if row!=None:    
                    self.var_id=row[0]
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.mark.config(text=row[4])
                    self.full.config(text=row[5])
                    self.per.config(text=row[6])
                else:
                    messagebox.showerror("Error","No Record Found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")
            
    #==========================Delete=============================
    
    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_id=="":
                messagebox.showerror("Error","Search Student Result First",parent=self.root)
            else:
                cur.execute("select * from result where rid=?",(self.var_id,))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Student result",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete",parent=self.root)
                    if op==True:
                        cur.execute("delete from result where rid=?",(self.var_id,))
                        con.commit()
                        messagebox.showinfo("Delete","Result Deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")   
            
    #==================Clear=========================
    
    def clear(self):
        self.var_id=""
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.mark.config(text="")
        self.full.config(text="")
        self.per.config(text="")
        self.var_search.set("")

if __name__=="__main__":
    root=Tk()
    obj=ReportClass(root)
    root.mainloop()