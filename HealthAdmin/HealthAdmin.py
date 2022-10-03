from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import pymysql




def click(issues):
    con=pymysql.connect(host="localhost",user="root",password="",database="healthadmin")
    cur=con.cursor()
    cur.execute("select * from problems where issue=%s",(issues,))
    rows=cur.fetchall()
    



root=Tk()
root.geometry("900x800")
root.title("Health Administrator")
root.configure(bg="crimson")
title = Label(root,text="HealthAdmin",font=('verdana',25,'bold'),bg="orange",fg="white")
title.place(x=340, y=10)

text = Label(root,text="Healthadmin is your software friend which takes care of your health and\nsuggests best reliable natural treatment for all health\n problems.It will help you to take a hygenic food and medicines.\nAnd it will help you to stay away from hospital.", font=('georgia',20,'italic'),bg="crimson",fg="yellow")
text.place(x=20, y=70)

select_problem=Label(root,text="Select Your Problem", font=('georgia',20,'bold'),bg="crimson",fg="white")
select_problem.place(x=290, y=250)

Problems = ttk.Combobox(root,width = 15, state="readonly",font=('verdana',15,'bold'))
Problems['values']=('Cold','Fever','HeadAche','Stomachpain','Vomit','loosemotion')
Problems.place(x=320,y=300)
Problems.current(0)


search=Button(root,text="Help Me",font=('verdana',10,'bold'),command=click('values'))
search.place(x=400,y=360)


solution=Label(root,text="Solution", font=('georgia',20,'bold'),bg="crimson",fg="maroon")
solution.place(x=370, y=410)

text = Text(root)


sol_text=ScrolledText(root,width=40,height=4)
sol_text['font']=('verdana',10,'bold')
sol_text.place(x=250, y=450)

clear=Button(root,text="Thank You !",font=('verdana',10,'bold'))
clear.place(x=390,y=530)




root.mainloop()