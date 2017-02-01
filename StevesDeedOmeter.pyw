import sqlite3 
from Tkinter import * 

def addData(): 
    conn=sqlite3.connect('deedinfo.db') 
    cur=conn.cursor() 
    cur.execute("create table if not exists deedsort(bkpage text,grantor text,grantee text,pin text)")
 
    #Get data from GUI 
    bookpage=(thebookpage.get()) 
    seller=(theseller.get()) 
    buyer=(thegrantee.get()) 
    pin=(thepin.get()) 

    clearGUI() 

    #Inserts data into table. Make sure and use a list to insert values! very important!
    cur.execute("insert into deedsort values (?,?,?,?)",([bookpage,seller,buyer,pin]))
 
    conn.commit() #Saves the data 
       
def listData(): 
    clearGUI() 
    conn=sqlite3.connect('deedinfo.db') 
    cur=conn.cursor() 

    myrows=cur.execute("select * from deedsort") 
    for row in myrows: 
        txtwin.insert("200.0", row[0]+"\n"+"GRANTOR: "+row[1]+"\n"+"GRANTEE: "+row[2]+"\n"+"pin = "+row[3]+"\n-------------------------------------------------\n")
 
def finddeed(): 
    con=sqlite3.connect("deedinfo.db") 
    cur=con.cursor() 
    deedbookpage = thebookpage.get() 
    clearGUI() 
    cur.execute("select * from deedsort") 
    rows = cur.fetchall() 
    for row in rows: 
        if row[0]== str(deedbookpage): 
            print "\nBook and Page: ", row[0] 
            print "Grantor: ",row[1] 
            print "Grantee: ",row[2] 
            
def clearGUI(): 
    thebookpage.delete(0,END) 
    theseller.delete(0,END) 
    thegrantee.delete(0,END) 
    thepin.delete(0,END) 
     
    txtwin.delete("1.0",END) 

def listgrantor(): 
    clearGUI() 
    conn=sqlite3.connect('deedinfo.db') 
    cur=conn.cursor() 

    myrows=cur.execute("select * from deedsort") 
    for row in myrows: 
        txtwin.insert("100.0","GRANTOR :"+ row[1]+"\n-----------------------------------------------------------\n")
 
def listgrantee(): 
    clearGUI() 
    conn=sqlite3.connect('deedinfo.db') 
    cur=conn.cursor() 

    myrows=cur.execute("select * from deedsort") 
    for row in myrows: 
        txtwin.insert("100.0","GRANTEE :"+ row[2]+"\n-----------------------------------------------------------\n")

def droptable(): 
    conn=sqlite3.connect('deedinfo.db') 
    cur=conn.cursor() 
    cur.execute("DROP TABLE deedsort")

def saveit(): 
    alist = txtwin.get("1.0",END) 
    f = open("minilog.txt", "w") 
    clearGUI() 
    txtwin.insert("1.0","list saved in minlog.txt") 
    f.write(str(alist)) 
    f.close() 

def listdeeds():
    clearGUI()
    conn=sqlite3.connect('deedinfo.db')
    cur=conn.cursor()
    myrows=cur.execute("select * from deedsort")
    for row in myrows:
        txtwin.insert("100.0","Deed Number: " + row[0]+"\n-------------------------------------------------------------\n")

def removeblank():
    clearGUI()
    conn=sqlite3.connect('deedinfo.db')
    cur=conn.cursor()
    cur.execute('DELETE FROM deedsort WHERE grantor = ""')
    conn.commit() #Saves the changes!
    listData()
  
root=Tk() 
root.title('Deed organizer ') 
root.config(bg='black') 
root.geometry('800x1000') 
               
btn=Button(root,text="List table",command=listData) 
btn.pack(padx=5,pady=5) 

btn2=Button(root,text="Add to table",command=addData) 
btn2.pack(padx=5,pady=5) 

btn4=Button(root,text="List Grantors",command=listgrantor) 
btn4.pack(padx=5,pady=5) 

deedbtn=Button(root,text="List Deeds", command=listdeeds)
deedbtn.pack(padx=5,pady=5)

grantbtn=Button(root,text="List Grantees",command=listgrantee) 
grantbtn.pack(padx=5,pady=5) 

removebtn=Button(root,text="Remove Blanks", command=removeblank)
removebtn.pack(padx=5,pady=5)

labl=Label(root,text="DEED NUMBER").pack() 

thebookpage = Entry() 
thebookpage.pack() 

labl2=Label(root,text="GRANTOR").pack() 
theseller = Entry(root, width = 90) 
theseller.pack() 

labl3=Label(root,text="GRANTEE").pack() 
thegrantee=Entry(root, width=90) 
thegrantee.pack() 

lab4=Label(root,text="PIN").pack() 
thepin =Entry(root,width =40) 
thepin.pack() 
         
txtwin=Text(root,width='800',height=33,background='white') 
txtwin.pack(padx=5, pady=5) 

droptablebtn=Button(root,text="Delete Table",command=droptable) 
droptablebtn.pack(padx=5,pady=5) 

savebtn=Button(root,text="Save to text file",command=saveit) 
savebtn.pack(padx=5,pady=5) 

root.mainloop() 
