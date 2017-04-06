#Written for Shawnee County by Steve Atchison 4/5/17
from Tkinter import *
import sqlite3
import datetime
import tkSimpleDialog

def DatabaseCreate():
  con=sqlite3.connect('ComboRequest.db')
  cur=con.cursor()
  cur.execute("create table if not exists requesttable(date text,requestor text,Phonenumber text,Email text,Address text,pin text,pin2 text,pin3 text, reason text)")

def getToday():
  today=datetime.date.today()
  string_date = today.strftime('%m/%d/%Y')
  theDateEntry.delete(0,END)#Clear the entry box
  theDateEntry.insert(0,string_date)

def addDatatoTable():
  DatabaseCreate()
  #get data from GUI
  date=theDateEntry.get()
  person=requestorEntry.get()
  phonenumb=PhonenumberEntry.get()
  theEmail=EmailEntry.get()
  Address=AddressEntry.get()
  PIN=PidEntry.get()
  PIN2=PidEntry2.get()
  PIN3=PidEntry3.get()
  theReason=ReasonWindow.get("1.0",END)
  #add data to database
  con=sqlite3.connect('ComboRequest.db')
  cur=con.cursor()
  cur.execute("INSERT INTO requesttable VALUES(?,?,?,?,?,?,?,?,?)",([date,person,phonenumb,theEmail,Address,PIN,PIN2,PIN3,theReason]))
  con.commit()
  cleargui()

def cleargui():
  theDateEntry.delete(0,END)
  requestorEntry.delete(0,END)
  PhonenumberEntry.delete(0,END)
  EmailEntry.delete(0,END)
  AddressEntry.delete(0,END)
  PidEntry.delete(0,END)
  PidEntry2.delete(0,END)
  PidEntry3.delete(0,END)
  ReasonWindow.delete("1.0",END)

def listdata():
  cleargui()
  removeBlanks()
  connect = sqlite3.connect("ComboRequest.db")
  cur=connect.cursor()
  thedata = cur.execute("SELECT * FROM requesttable")
  for row in thedata:
    ReasonWindow.insert("100.0",row[0]+" - "+row[1]+" - "+row[2]+" - "+row[3]+" - "+row[4]+ " - "+ row[5]+" - "+row[6]+" - "+row[7]+ " - "+ row[8]+"\n")

def removeBlanks():
  con=sqlite3.connect("ComboRequest.db")
  cur=con.cursor()
  cur.execute("delete from requesttable where requestor = '';")
  con.commit()
def finddocument():
  cleargui()
  thePIN=tkSimpleDialog.askstring("Find Document","Parcel ID?")
  con=sqlite3.connect('ComboRequest.db')
  cur=con.cursor()
  comrequest = cur.execute("SELECT * from requesttable WHERE pin = ?;",([thePIN]))
  for row in comrequest:
    ReasonWindow.insert("100.0","Date: "+row[0]+"\n"
                        +"Requestor: "+row[1]+"\n"
                        +"Phone number: "+row[2]+"\n"
                        +"Email: "+row[3]+"\n"
                        +"Property Address: "+row[4]+"\n"
                        +"PIN: "+row[5]+"\n"
                        +"PIN: "+row[6]+"\n"
                        +"PIN: "+row[7]+"\n"
                        +"Reason for Combination: "+row[8]+"\n")

def deleterecord():
  removeBlanks()
  cleargui()
  thePin=tkSimpleDialog.askstring("Enter parcel ID","Record to remove?")
  con=sqlite3.connect('ComboRequest.db')
  cur=con.cursor()
  cur.execute("DELETE FROM requesttable WHERE PIN = ?;",([thePin]))
  con.commit()
              
root=Tk()
root.title("Combination of Tax Parcels Request")
root.geometry('750x650')

window=Toplevel(root,background='blue')


theDateLabel=Label(root,text= "Date:").pack()
theDateEntry=Entry(root)
theDateEntry.pack(padx=5,pady=5)

requestorLable=Label(root,text="REQUESTOR: ").pack()
requestorEntry=Entry(root)
requestorEntry.pack(padx=5,pady=5)

PhonenumberLabel=Label(root,text="Phone Number: ").pack()
PhonenumberEntry=Entry(root)
PhonenumberEntry.pack(padx=5,pady=5)

EmailLabel=Label(root,text="Email:").pack()
EmailEntry=Entry(root)
EmailEntry.pack(padx=5,pady=5)

AddressLabel=Label(root,text="Property Address: ").pack()
AddressEntry=Entry(root)
AddressEntry.pack(padx=5,pady=5)

PidLabel=Label(root,text="PID or QuickRef ID: ").pack()
PidEntry=Entry(root)
PidEntry.pack(padx=5,pady=5)

PidLabel2=Label(root,text="PID or QuickRef ID: ").pack()
PidEntry2=Entry(root)
PidEntry2.pack(padx=5,pady=5)

PidLabel3=Label(root,text="PID or QuickRef ID: ").pack()
PidEntry3=Entry(root)
PidEntry3.pack(padx=5,pady=5)

ReasonLabel=Label(root,text="Reason for Combination ").pack()
ReasonWindow=Text(root,width='90',height=12, background='white')
ReasonWindow.pack(padx=5,pady=5)

saveButton=Button(window,text="SAVE",command=addDatatoTable)
saveButton.pack()

findbutton=Button(window,text="Find using PIN",command=finddocument)
findbutton.pack(padx=5,pady=5)

deleteButton=Button(window,text="Remove record",command=deleterecord)
deleteButton.pack(padx=5,pady=5)

today=Button(window,text="Add todays date",command=getToday)
today.pack(padx=5,pady=5)
root.mainloop()
