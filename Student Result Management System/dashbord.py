import imp
from logging import root
from tkinter import*
from PIL import Image,ImageTk
from course import CourseClass
from student import StudentClass
from result import ResultClass
from report import ReportClass
from tkinter import messagebox
import os
from PIL import Image,ImageTk,ImageDraw
from datetime import*
import time
from math import*
import sqlite3

class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Managemeny System")
        self.root.geometry("1530x790+0+0")
        self.root.config(bg="white")
        
        #============icons==================
        
        self.logo_dash=ImageTk.PhotoImage(file="images/logo_p.png")
        
        #==========title===================
        
        title=Label(self.root,text="Student Result Management System",image=self.logo_dash,padx=10,compound=LEFT,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
    
        #====================Menu================
        
        M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=15,y=70,width=1500,height=80)
        
        btn_course=Button(M_Frame,text="Course",command=self.add_course,font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",).place(x=20,y=5,width=220,height=40)
        btn_student=Button(M_Frame,text="Student",command=self.add_student,font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",).place(x=260,y=5,width=220,height=40)
        btn_result=Button(M_Frame,text="Result",command=self.add_result,font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",).place(x=500,y=5,width=220,height=40)
        btn_view=Button(M_Frame,text="View Student Result",command=self.add_report,font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",).place(x=750,y=5,width=220,height=40)
        btn_logout=Button(M_Frame,text="Logout",command=self.logout,font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",).place(x=1000,y=5,width=220,height=40)
        btn_exit=Button(M_Frame,text="Exit",command=self.exit_,font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",).place(x=1250,y=5,width=220,height=40)
        
        #=============Content Window==============
        
        self.bg_img=Image.open("images/bg.png")
        self.bg_img=self.bg_img.resize((920,470),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        
        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=580,y=155,width=920,height=470)
        
        #==============Update Details==========
        
        self.lbl_course=Label(self.root,text="Total Course\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=580,y=635,width=300,height=100)
        
        self.lbl_student=Label(self.root,text="Total Student\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
        self.lbl_student.place(x=890,y=635,width=300,height=100)
        
        self.lbl_result=Label(self.root,text="Total Result\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white")
        self.lbl_result.place(x=1200,y=635,width=300,height=100)
        
        #===============Clock===========================
            
        self.lbl=Label(self.root,text="\nAnsh Galani",font=("Book Antiqua",25,"bold"),compound=BOTTOM,bg="#081923",fg="white",bd=0)
        self.lbl.place(x=10,y=160,height=570,width=550)
        
        self.working()
        
        #==========footer===================
        
        footer=Label(self.root,text="SRMS-Student Result Management System\nContact Us for any Technical Issue: anshgalani@yahoo.com",font=("times new roman",13),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
        self.update_details()
#======================================================================================================================== 
    
    def update_details(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")
            
            cur.execute("select * from student")
            cr=cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")
            
            cur.execute("select * from result")
            cr=cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{str(len(cr))}]")
            
            self.lbl_course.after(200,self.update_details)
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")
            
    
    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
        
        hr=(h/12)*360
        min_=(m/60)*360
        sec=(s/60)*360
        self.clock_image(hr,min_,sec)
        self.img=ImageTk.PhotoImage(file="clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)
    
    def clock_image(self,hr,min_,sec_):
        clock=Image.new("RGB",(400,400),(8,25,35))
        draw=ImageDraw.Draw(clock)
        
        #==========For Clock Image=================
        
        bg=Image.open("images/c.png")
        bg=bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))
        
        #==Formula To Rotate the AntiClock
        # angle_in_radians = angle_in_degress * math.pi/160
        # line_length =100
        #centry_x=250
        #centry_y=250
        #end_x = center_x - line_length * math.cos(angle_in_radians)
        #end_y = center_y - line_length * math.cos(angle_in_radians)
        
        #============Hour Line Image==============
        origin=200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="#DF005E",width=4)
        
        #============Min Line Image==============
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="white",width=3)
        
        #============Sec Line Image==============
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="yellow",width=2)
        
        #=============Circle==================
        draw.ellipse((195,195,210,210),fill="#1AD5D5")
        
        clock.save("clock_new.png")
    
    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)
        
    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=StudentClass(self.new_win)
        
    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ResultClass(self.new_win)
    
    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ReportClass(self.new_win)
    
    def logout(self):
        op=messagebox.askyesno("Confirm","Do You Really want to logout",parent=self.root)
        if op==True:
          self.root.destroy()
          os.system("python login.py")  
          
    def exit_(self):
        op=messagebox.askyesno("Confirm","Do You Really want to Exit",parent=self.root)
        if op==True:
          self.root.destroy()
    
    
if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()