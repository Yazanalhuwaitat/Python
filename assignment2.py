from tkinter import *
import tkinter as tk
import pandas as pd
from tabulate import tabulate
import tkinter.messagebox
root=Tk()
root.title('Book Library')
root.geometry("500x400")

#read excel file
data= pd.read_excel("books.xlsx")
data.to_excel("books.xlsx",index=False)

text=pd.read_excel("books.xlsx",usecols=["id","title"])
tabulate(text,headers=text.columns)
text100=tabulate(text,showindex=False,headers=text.columns,colalign=("left",))



#lists
idlist= data['id'].tolist()
titlelist= data['title'].tolist()
authorlist= data['author'].tolist()
copylist= data['no copies'].tolist()
pricelist= data['price'].tolist()



#functions
def com():
    T.insert(INSERT,text100)
        
def call():
    flag=False
    if user1.get().count(' ')==len(user1.get()):
        tkinter.messagebox.showinfo('book id','Please enter book id number')
    for i in range(0,len(idlist)):
        if int(user1.get())==idlist[i]:
            text1.config(text=titlelist[i],fg="red")
            text2.config(text=authorlist[i],fg="red")
            text3.config(text=copylist[i],fg="red")
            text4.config(text=pricelist[i],fg="red")
            flag=True
            break
    if flag==False:
        tkinter.messagebox.showerror('book id','Invalid book id number')



#menubar
menubar = Menu(root)

file = Menu(menubar,tearoff=0)  
file.add_command(label="New")
file.add_command(label="Save")
file.add_separator()   
file.add_command(label="Exit", command=root.destroy)  
menubar.add_cascade(label="File", menu=file)  

edit = Menu(menubar,tearoff=0)   
edit.add_command(label="Copy")
edit.add_separator()  
edit.add_command(label="Paste")  
menubar.add_cascade(label="Edit", menu=edit)  
   
root.config(menu=menubar)



#labels
A=Label(text="Explore Books",font=("Arial",25))
A.grid(row=0,column=1)

B1=Label(text="Enter Book Id")
B1.grid(row=1,sticky=W)

B2=Label(text="Book Title")
B2.grid(row=2,sticky=W)

B3=Label(text="Book Author")
B3.grid(row=3,sticky=W)

B4=Label(text="No. of Copies")
B4.grid(row=4,sticky=W)

B5=Label(text="Book Price")
B5.grid(row=5,sticky=W)



#entry
user1=Entry(root,width=3)
user1.grid(row=1,column=1,sticky=W)



#buttons
lb1=Button(root,text="Search",relief=RAISED,command=call,bg="gray",fg="white")
lb1.grid(row=1,column=1,sticky=W,padx=50)

lb2=Button(root,text="View all",relief=RAISED,command=com,bg="gray",fg="white")
lb2.grid(row=1,column=1,sticky=E,padx=50)



#text
text1 = Label(root, text="")
text1.grid(row=2,column=1,sticky=W)

text2 = Label(root, text="")
text2.grid(row=3,column=1,sticky=W)

text3 = Label(root, text="")
text3.grid(row=4,column=1,sticky=W)

text4 = Label(root, text="")
text4.grid(row=5,column=1,sticky=W)

T=Text(root,width=50,height=14)
T.grid(row=6,column=1,sticky=W)

root.mainloop()
