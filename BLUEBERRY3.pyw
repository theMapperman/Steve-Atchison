#!/usr/bin/env python
from Tkinter import *

#written by Steve Atchison Feb 20 2012

def dimlines():
    #right side
    w.create_line(620,10,620,160,fill='black',arrow=BOTH)
    w.create_text(640,75,text="1320'")
    w.create_line(620,160,620,235,fill='black',arrow=BOTH)
    w.create_text(640,200,text="660'")
    w.create_line(620,235,620,310,fill='black',arrow=BOTH)
    w.create_text(640,275,text="660'")
    w.create_line(620,310,620,610,fill='black',arrow=BOTH)
    w.create_text(640,450,text="2640'")
    #bottom
    w.create_line(10,630,310,630,fill='black',arrow=BOTH)
    w.create_text(160,620,text="2640'")
    w.create_line(310,630,460,630,fill='black',arrow=BOTH)
    w.create_text(385,620,text="1320'")
    w.create_line(460,630,535,630,fill='black',arrow=BOTH)
    w.create_text(500,620,text="660'")
    w.create_line(535,630,610,630,fill='black',arrow=BOTH)
    w.create_text(575,620,text='660')
def qqqlines():
    w.create_line(47,10,47,610,fill='orange',dash=(2,6))
    w.create_line(122,10,122,610,fill='orange',dash=(2,6))
    w.create_line(197,10,197,610,fill='orange',dash=(2,6))
    w.create_line(272,10,272,610,fill='orange',dash=(2,6))
    w.create_line(347,10,347,610,fill='orange',dash=(2,6))
    w.create_line(422,10,422,610,fill='orange',dash=(2,6))
    w.create_line(497,10,497,610,fill='orange',dash=(2,6))
    w.create_line(572,10,572,610,fill='orange',dash=(2,6))
    w.create_line(10,47,610,47,fill='orange',dash=(2,6))
    w.create_line(10,122,610,122,fill='orange',dash=(2,6))
    w.create_line(10,197,610,197,fill='orange',dash=(2,6))
    w.create_line(10,272,610,272,fill='orange',dash=(2,6))
    w.create_line(10,347,610,347,fill='orange',dash=(2,6))
    w.create_line(10,422,610,422,fill='orange',dash=(2,6))
    w.create_line(10,497,610,497,fill='orange',dash=(2,6))
    w.create_line(10,572,610,572,fill='orange',dash=(2,6))

def bluedash():
    w.create_line(85,10,85,610,fill='blue',dash=(4,4))
    w.create_line(10,85,610,85,fill='blue',dash=(4,4))
    w.create_line(10,235,610,235,fill='blue',dash=(4,4))
    w.create_line(10,310,610,310,fill='blue',dash=(4,4))
    w.create_line(235,10,235,610,fill='blue',dash=(4,4))
    w.create_line(10,385,610,385,fill='blue',dash=(4,4))
    w.create_line(10,535,610,535,fill='blue',dash=(4,4))
    w.create_line(535,10,535,610,fill='blue',dash=(4,4))
    w.create_line(385,10,385,610,fill='blue',dash=(4,4))
def labelq():
    w.create_text(150,150,text = "  NW 1/4 \n160 acres",fill='purple',font=('Helvectica','12'))
    w.create_text(150,450,text = "  SW 1/4 \n160 acres",fill='purple',font=('Helvectica','12'))
    w.create_text(450,450,text = "  SE 1/4 \n160 acres",fill='purple',font=('Helvectica','12'))
    w.create_text(450,150,text = "  NE 1/4 \n160 acres",fill='purple',font=('Helvectica','12'))
def reddash():
    w.create_line(160,10,160,610,fill='red',dash=(4,4))
    w.create_line(10,160,610,160,fill='red',dash=(4,4))
    w.create_line(10,460,610,460,fill='red',dash=(4,4))
    w.create_line(460,10,460,610,fill='red',dash=(4,4))
def showqtr():
    #NORTH WEST 1/4
    choice = theAction.get()
    if choice == 'SE NW':     
        w.create_rectangle(160,160,310,310, fill="yellow")
        w.create_text(235,235,text = ' SE NW \n40 ac')     
        w.create_text(275,275,text = 'SE')
        w.create_text(195,195,text = 'NW')
        w.create_text(195,270,text = 'SW')
        w.create_text(275,195,text = 'NE')
        qqqlines()
    elif choice == 'NW NW':   
        w.create_rectangle(10,10,160,160,fill="yellow")
        w.create_text(85,85,text = 'NW NW \n40 ac')
        w.create_text(50,50,text = 'NW')
        w.create_text(125,50,text = 'NE')
        w.create_text(50,125,text = 'SW')
        w.create_text(125,125,text = 'SE')
        qqqlines()
    elif choice == 'NE NW':
        w.create_rectangle(160,10,310,160,fill='yellow')
        w.create_text(237,85,text = 'NE NW \n40 ac')
        w.create_text(270,50,text = 'NE')
        w.create_text(200,50,text= 'NW')
        w.create_text(200,125,text= 'SW')
        w.create_text(270,125,text= 'SE')
        qqqlines()

    elif choice == 'SW NW':
        w.create_rectangle(10,160,160,310,fill='yellow')
        w.create_text(85,235,text = 'SW NW \n40 ac')
        w.create_text(50,275,text = 'SW')
        w.create_text(125,275,text = 'SE')
        w.create_text(50,200,text = 'NW')
        w.create_text(125,200,text = 'NE')
        qqqlines()

    #NORTH EAST 1/4
    elif choice == 'SE NE':
        w.create_rectangle(460,310,610,160,fill='yellow')
        w.create_text(535,235,text = 'SE NE \n40 ac')
        w.create_text(575,200,text = 'NE')
        w.create_text(575,270,text = 'SE')
        w.create_text(500,270,text = 'SW')
        w.create_text(500,200,text = 'NW')
        qqqlines()

    elif choice == 'SW NE':
        w.create_rectangle(310,160,460,310,fill='yellow')
        w.create_text(383,235,text = 'SW NE \n40 ac')
        w.create_text(425,200,text = 'NE')
        w.create_text(425,270,text = 'SE')
        w.create_text(350,270,text = 'SW')
        w.create_text(350,200,text = 'NW')
        qqqlines()
    elif choice == 'NE NE':
        w.create_rectangle(460,10,610,160,fill='yellow')
        w.create_text(535,85,text = 'NE NE \n40 ac')
        w.create_text(575,50,text = 'NE')
        w.create_text(500,50,text = 'NW')
        w.create_text(500,125,text = 'SW')
        w.create_text(575,125,text = 'SE')
        qqqlines()
    elif choice == 'NW NE':

        w.create_rectangle(310,10,460,160,fill='yellow')
        w.create_text(383,85,text = 'NW NE \n40 ac')
        w.create_text(350,50,text= 'NW')
        w.create_text(350,125,text = 'SW')
        w.create_text(425,50,text = 'NE')
        w.create_text(425,125,text = 'SE')
        qqqlines()      

    #SOUTH EAST 1/4
    elif choice == 'SE SE':
        w.create_rectangle(460,460,610,610,fill='yellow')
        w.create_text(535,535,text = 'SE SE \n40 ac')
        w.create_text(500,500,text = 'NW')
        w.create_text(500,575,text = 'SW')
        w.create_text(575,575,text = 'SE')
        w.create_text(575,500,text = 'NE')
        qqqlines()
    elif choice == 'NW SE':
        w.create_rectangle(310,310,460,460,fill='yellow')
        w.create_text(385,385,text = 'NW SE \n40 ac')
        w.create_text(350,350,text= 'NW')
        w.create_text(425,350,text= 'NE')
        w.create_text(350,425,text= 'SW')
        w.create_text(425,425,text= 'SE')
        qqqlines()

    elif choice == 'NE SE':

        w.create_rectangle(460,310,610,460,fill='yellow')
        w.create_text(535,385,text = 'NE SE \n40 ac')
        w.create_text(575,350,text = 'NE')
        w.create_text(500,350,text = 'NW')
        w.create_text(575,425,text = 'SE')
        w.create_text(500,425,text = 'SW')
        qqqlines()

    elif choice == 'SW SE':
        w.create_rectangle(310,460,460,610,fill='yellow')
        w.create_text(385,535,text = 'SW SE \n40 ac')
        w.create_text(350,575,text = 'SW')
        w.create_text(425,575,text = 'SE')
        w.create_text(350,500,text = 'NW')
        w.create_text(425,500,text = 'NE')
        qqqlines()

    #SOUTH WEST 1/4
    elif choice == 'SW SW':
        w.create_rectangle(10,460,160,610,fill='yellow')
        w.create_text(85,535,text = 'SW SW \n40 ac')
        w.create_text(50,575,text = 'SW')
        w.create_text(125,575,text = 'SE')
        w.create_text(50,500,text = 'NW')
        w.create_text(125,500,text = 'NE')
    elif choice == 'SE SW':
        w.create_rectangle(160,460,310,610,fill='yellow')
        w.create_text(235,535,text = 'SE SW \n40 ac')
        w.create_text(200,575,text = 'SW')
        w.create_text(275,575,text = 'SE')
        w.create_text(200,500,text = 'NW')
        w.create_text(275,500,text = 'NE')
    elif choice == 'NW SW':
        w.create_rectangle(10,310,160,460,fill='yellow')
        w.create_text(85,385,text = 'NW SW \n40 ac')
        w.create_text(50,425,text = 'SW')
        w.create_text(125,425,text = 'SE')
        w.create_text(50,350,text = 'NW')
        w.create_text(125,350,text = 'NE')
    elif choice == 'NE SW':
        w.create_rectangle(160,310,310,460,fill='yellow')
        w.create_text(235,385,text = 'NE SW \n40 ac')
        w.create_text(200,425,text = 'SW')
        w.create_text(275,425,text = 'SE')
        w.create_text(200,350,text = 'NW')
        w.create_text(275,350,text = 'NE')
    bluedash()
    qqqlines()
    labelq()

def convertfunctions():#This is the convert window
    def clearent1():
        ent1.delete(0,END)

    def rodtoft():
        theRods = ent1.get()
        ftinrd = round(float(theRods)*16.5,2)     
        print(ftinrd)
        textwin2.insert('1.0',str(theRods)+' Rods = '+str(ftinrd)+' feet \n')
        clearent1()

    def chtoft():
        theChains=ent1.get()
        theft=round(float(theChains)*66,2)
        print(theft)
        textwin2.insert('1.0',str(theChains)+' chains = '+ str(theft)+' feet \n')
        clearent1()
    def acretosqft():
        theacres=float(ent1.get())
        sqft=((theacres * 43560))
        textwin2.insert('1.0',ent1.get() + ' acres = ' +  str(sqft) +' sq ft \n')
        clearent1()
    def sqfttoacres():
        theacres=float(ent1.get())/43560
        textwin2.insert('1.0',ent1.get() + ' sq feet = ' + str(round(theacres,2)) + ' acres\n')
        clearent1()

#CONVERT MENU     
    top2=Toplevel(root)
    top2.geometry('275x200')
    top2.config(bg='orange')
    convertrdbtn=Button(top2,text='Rods to Feet',command=rodtoft)
    convertrdbtn.pack()
    convertchainbtn=Button(top2,text='Chains to Feet',command=chtoft)
    convertchainbtn.pack()
    acressqftbtn=Button(top2,text='Acres to sq ft',command=acretosqft)
    acressqftbtn.pack()
    sqfttoacres=Button(top2,text='Sq ft to Acres',command=sqfttoacres)
    sqfttoacres.pack()
    ent1= Entry(top2)
    ent1.pack()
    textwin2=Text(top2)
    textwin2.pack()
def unknown(): #This is the find unknownside window
    def clearGUI():
        knownside.delete(0,END)
        acres.delete(0,END)     
    def calcit():
        unknownside= (float(acres.get())*float(43560))/float(knownside.get())
        textwin.delete('1.0',END) #clear the text widget before adding new text
        textwin.insert('1.0','Acres = '+ acres.get()+'\nknown side = '+ knownside.get()+ '\nUnknown side = ' + str(round(unknownside,2))+'\n')
        clearGUI()
    top=Toplevel(root)
    top.geometry('250x175')
    top.config(bg='green')
    lbl = Label(top,text='Known side')
    lbl.pack()
    knownside = Entry(top)
    knownside.pack()
    lbl2= Label(top,text='Acres')
    lbl2.pack()
    acres = Entry(top)
    acres.pack()
    calcbtn = Button(top,text='Calc',command= calcit)
    calcbtn.pack()
    textwin = Text(top)
    textwin.pack()

def clear(): #Covers the graphics with new graphics.
    w.create_rectangle(10,10,310,310, fill="white")
    w.create_rectangle(10,610,310,310, fill="white")
    w.create_rectangle(310,310,610,610, fill="white")
    w.create_rectangle(310,10,610,310, fill="white")
    bluedash()
    reddash()
    labelq()
    qqqlines()
    dimlines()
#START OF OBJECT MOVING 660x330
def createrect():
    w.create_rectangle(10,85,85,47,fill='',tag='rectangle',dash='5',width=3)
    qqqlines()  
def deleterect():
    w.delete('rectangle')
    createrect()
def movedown():  
    w.move('rectangle',0,37.5)
def moveright():
    w.move('rectangle',37.5,0)
def moveleft():
    w.move('rectangle',-37.5,0)
def moveup():
    w.move('rectangle',0,-37.5)               

def objectmenu():
    top3=Toplevel(root)
    top3.geometry('150x175')
    top3.config(bg='red')
    alabel=Label(top3,text='660x330')
    alabel.pack()
    downbtn=Button(top3,text='SOUTH',command=movedown)
    downbtn.pack()
    rightbtn=Button(top3,text='EAST',command=moveright)
    rightbtn.pack()
    leftbtn=Button(top3,text='WEST',command=moveleft)
    leftbtn.pack()
    upbtn=Button(top3,text='NORTH',command=moveup)
    upbtn.pack()
    newbtn=Button(top3,text='new',command=deleterect)
    newbtn.pack()
    deleterect()
    createrect()
#END OF OBJECT MOVING 660x330 and START OF 330X660 MENU  

def createrect330by660():
    w.create_rectangle(47,10,10,85,fill='',tag='halfrectangle',dash='5',width=3)
    qqqlines()  
def menu330by660():
    top4=Toplevel(root)
    top4.geometry('150x175')
    top4.config(bg='blue')
    alabel=Label(top4,text='330x660')
    alabel.pack()
    downbtn=Button(top4,text='SOUTH',command=movehalfdown)
    downbtn.pack()
    rightbtn=Button(top4,text='EAST',command=movehalfright)
    rightbtn.pack()
    leftbtn=Button(top4,text='WEST',command=movehalfleft)
    leftbtn.pack()
    upbtn=Button(top4,text='NORTH',command=movehalfup)
    upbtn.pack()
    newbtn=Button(top4,text='new',command=deletehalfrect)
    newbtn.pack()
def deletehalfrect():
    w.delete('halfrectangle')
    createrect330by660()
def movehalfdown():  
    w.move('halfrectangle',0,37.5)
def movehalfright():
    w.move('halfrectangle',37.5,0)
def movehalfleft():
    w.move('halfrectangle',-37.5,0)
def movehalfup():
    w.move('halfrectangle',0,-37.5)
def gomenu():
    userchoice=theobject.get()
    if userchoice=='660x330':
        objectmenu()    
    elif userchoice=='330x660':
        menu330by660()
        createrect330by660()

root=Tk()
root.title('SNCO GIS')
root.config(bg='blue')
w = Canvas(root, width=670, height=650,bg='light green')
w.pack()
w.create_rectangle(10,10,310,310, fill="white")
w.create_rectangle(10,610,310,310, fill="white")
w.create_rectangle(310,310,610,610, fill="white")
w.create_rectangle(310,10,610,310, fill="white")
bluedash()
reddash()
qqqlines()
labelq()
dimlines()               

unknownsidebutton=Button(root,text='Unknown Side',command=unknown,bg='purple')
unknownsidebutton.pack(side='right')
theAction = StringVar()
theAction.set(None)
menuitem = ['SE NW','NW NW','NE NW','SW NW','--------','SE NE','SW NE','NE NE','NW NE','---------',
            'SE SE','NW SE','NE SE','SW SE','--------','SW SW','SE SW','NW SW','NE SW']

OptionMenu(root,theAction,*menuitem).pack(side='left')
gobtn = Button(root,text="Draw",command= showqtr,bg='yellow')
gobtn.pack(side ='left')

clearbtn=Button(root,text='clear all graphics',command= clear,bg='green')
clearbtn.pack(padx=16,pady=2,side='left')

convertbtn = Button(root,text='Convert',command=convertfunctions,bg='purple')
convertbtn.pack(padx=3,pady=5,side='right')
aframe = Frame()
aframe.pack(padx=16,pady=3,side='right')

startdrawobjectbtn=Button(aframe,text='go',command=gomenu)
startdrawobjectbtn.pack(side='right')

theobject=StringVar()
theobject.set('None')
whattodraw=OptionMenu(aframe,theobject,'660x330','330x660').pack(side='right')

root.mainloop()
