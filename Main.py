# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 02:27:04 2020

@author: Piyush Chanchal
@EMail id: piyush.chanchal@hotmail.com
"""

from tkinter import Tk
from tkinter.filedialog import *
from tkinter.filedialog import askdirectory
import pandas as pd
import os
from tkinter import ttk

def validation(flag,ErrFirstCSVObjExist,ErrSecondCSVObjExist,ErrOutPathObj):
    flag=1
    ############First csv path validation
    if FirstCSVPathEntry.get()=="":
        global ErrFirstCSV
        ErrFirstCSV = Text(root,height=0,width=35,bg='#333333',bd=0,fg='red')
        ErrFirstCSV.grid(row=4,column=0,sticky=W)
        ErrFirstCSV.insert(END,'*Path of FirstCSV file can not be empty')
        flag=0
        ErrFirstCSVObjExist=0
    elif ErrFirstCSVObjExist==0:
        ErrFirstCSV.destroy()
        ############Second csv path validation
    if SecondCSVPathEntry.get()=="":
        global ErrSecondCSV
        ErrSecondCSV = Text(root,height=0,width=35,bg='#333333',bd=0,fg='red')
        ErrSecondCSV.grid(row=7,column=0,sticky=W)
        ErrSecondCSV.insert(END,'*Path of SecondCSV file can not be empty')
        flag=0
        ErrSecondCSVObjExist=0
    elif ErrSecondCSVObjExist==0:
        ErrSecondCSV.destroy()
    ##########Output path validation
    if OutputPathEntry.get()=="":
        global ErrOutPath
        ErrOutPath = Text(root,height=0,width=35,bg='#333333',bd=0,fg='red')
        ErrOutPath.grid(row=10,column=0,sticky=W)
        ErrOutPath.insert(END,'*Path of Output Directory can not be empty')
        flag=0
        ErrOutPathObj=0
    elif ErrOutPathObj==0:
        ErrOutPath.destroy()
    return flag,ErrFirstCSVObjExist,ErrSecondCSVObjExist,ErrOutPathObj



class Validation:
  global ErrFirstCSVObjExist
  global ErrSecondCSVObjExist
  global ErrOutObjExist
  global ErrOutNameObjExist
  def __init__(self):
      self.flag=1
  def FirstCSVPathVal(self):
    global ErrFirstCSVObjExist
    if ErrFirstCSVObjExist==0:
        global ErrFirstCSV
        ErrFirstCSV = Text(root,height=0,width=35,bg='#333333',bd=0,fg='red')
        ErrFirstCSV.grid(row=4,column=0,sticky=W)
        ErrFirstCSV.insert(END,'*Path of CSV file can not be empty')
        self.flag=0
        self.ErrFirstCSVObjExist=1
  def SecondCSVPathVal(self):
    global ErrSecondCSVObjExist
    if ErrSecondCSVObjExist==0:
        global ErrSecondCSV
        ErrSecondCSV = Text(root,height=0,width=35,bg='#333333',bd=0,fg='red')
        ErrSecondCSV.grid(row=7,column=0,sticky=W)
        ErrSecondCSV.insert(END,'*Path of CSV file can not be empty')
        self.flag=0
        self.ErrSecondCSVObjExist=1
  def OutPathVal(self):
    global ErrOutObjExist
    if ErrOutObjExist==0:
        global ErrOut
        ErrOut = Text(root,height=0,width=35,bg='#333333',bd=0,fg='red')
        ErrOut.grid(row=10,column=0,sticky=W)
        ErrOut.insert(END,'*Output path can not be empty')
        self.flag=0
        self.ErrOutObjExist=1
  def OutNameVal(self):
    global ErrOutNameObjExist
    if ErrOutNameObjExist==0:
        global ErrOutName
        ErrOutName = Text(root,height=0,width=35,bg='#333333',bd=0,fg='red')
        ErrOutName.grid(row=13,column=0,sticky=W)
        ErrOutName.insert(END,'*Output File name can not be blank')
        self.flag=0
        self.ErrOutNameObjExist=1
       
       
       
       
########CSV merge function
def Merge():
    global ErrFirstCSVObjExist
    global ErrSecondCSVObjExist
    global ErrOutObjExist
    global ErrOutNameObjExist
    global JoinTypeName

   
    Val = Validation()
    ########First CSV validation
    if FirstCSVPathEntry.get()=="":
        if ErrFirstCSVObjExist==1:
            ErrFirstCSV.destroy()
        ErrFirstCSVObjExist=0
        Val.FirstCSVPathVal()
        ErrFirstCSVObjExist=Val.ErrFirstCSVObjExist
    elif ErrFirstCSVObjExist==1:
        ErrFirstCSV.destroy()

    ########Second CSV validation
    if SecondCSVPathEntry.get()=="":
        if ErrSecondCSVObjExist==1:
            ErrSecondCSV.destroy()
        ErrSecondCSVObjExist=0
        Val.SecondCSVPathVal()
        ErrSecondCSVObjExist=Val.ErrSecondCSVObjExist
    elif ErrSecondCSVObjExist==1:
        ErrSecondCSV.destroy()

    ########Output path validation
    if OutputPathEntry.get()=="":
        if ErrOutObjExist==1:
            ErrOut.destroy()
        ErrOutObjExist=0
        Val.OutPathVal()
        ErrOutObjExist=Val.ErrOutObjExist
    elif ErrOutObjExist==1:
        ErrOut.destroy()
       
       
       
    #####Output file name validation
    if OutFileNameEntry.get()=="":
        if ErrOutNameObjExist==1:
            ErrOutName.destroy()
        ErrOutNameObjExist=0
        Val.OutNameVal()
        ErrOutNameObjExist=Val.ErrOutNameObjExist
    elif ErrOutNameObjExist==1:
        ErrOutName.destroy()
       
       
    flag = Val.flag

    if flag==1:
        FirstCSV_DF = pd.read_csv(FirstCSVPathEntry.get())
        SecondCSV_DF = pd.read_csv(SecondCSVPathEntry.get())
        if JoinTypeName=="":
            JoinTypeName = "outer"
        if KeyColName=="":
            MergedDF = pd.merge(FirstCSV_DF,SecondCSV_DF,how=JoinTypeName)
        elif not(KeyColName==""):
            MergedDF = pd.merge(FirstCSV_DF,SecondCSV_DF,on=str(KeyColName),how=str(JoinTypeName))
        MergedDF.to_csv(str(OutputDir)+"\\"+str(OutFileNameEntry.get())+".csv",index=False)
        messagebox.showinfo(title="Merged Successful", message="CSV files has been merged and saved in the output Directory.")

           
# This function will be used to take First CSV as input
def openFirstCSV_file():
    global FirstCSVPath
    file = askopenfile(mode ='r', filetypes =[('CSV Files', '*.csv')])
    if file is not None:
        FirstCSVPathEntry.insert(END,file.name)
        FirstCSVPath=file.name
       
# This function will be used to take Second CSV as input
def openSecondCSV_file():
    global SecondCSVPath
    file = askopenfile(mode ='r', filetypes =[('CSV Files', '*.csv')])
    if file is not None:
        SecondCSVPathEntry.insert(END,file.name)
        SecondCSVPath=file.name


# This function will be used to take output CSV file full path
def openOut_file():
    global OutputDir
    file = askdirectory()
    if file is not None:
        OutputPathEntry.insert(END,file)
        OutputDir=file
       
       
def KeyName():
    global KeyColName
    KeyNameWin = Toplevel(root)
    path_file = os.path.dirname(os.path.realpath(__file__))
    IconImg = PhotoImage(file=str(path_file)+"\\"+"Images\Key.png")
    KeyNameWin.iconphoto(False,IconImg)
    BgColor='#333333'
    BgColorOth='#737373'
    TxtFont="Arial Narrow"
    KeyNameWin.title("Enter Key")
    KeyNameWin.configure(bg=BgColor)
    LblKey = Label(KeyNameWin,text="KEY COLUMN NAME\n(common in both CSVs)")
    LblKey.grid(row=0,column=0,columnspan =2)
    global InKey
    InKey = Entry(KeyNameWin)
    if not(KeyColName==""):
        InKey.insert(END,KeyColName)
    InKey.grid(row=1,column=0)
    KeySbmt = Button(KeyNameWin,text="Submit",command=FnKeySbmt)
    KeySbmt.grid(row=2,column=0)
   
    KeyNameWin.mainloop()


def FnKeySbmt():
    global KeyColName
    KeyColName = InKey.get()

       
def JoinType():
    global JoinTypeName
    JoinTypeWin = Toplevel(root)
    path_file = os.path.dirname(os.path.realpath(__file__))
    IconImg = PhotoImage(file=str(path_file)+"\\"+"Images\Join.png")
    JoinTypeWin.iconphoto(False,IconImg)
    JoinTypeWin.title("Specify Join Type")
    BgColor='#333333'
    BgColorOth='#737373'
    TxtFont="Arial Narrow"
    JoinTypeWin.configure(bg=BgColor)
    LblJoinType = Label(JoinTypeWin,text="        Specify Join Type         ")
    LblJoinType.grid(row=0,column=0,columnspan=2)
    global ListJoinType
    ListJoinType = ttk.Combobox(JoinTypeWin)
    ####Adding drop down list for Join Type
    ListJoinType['values']=('Left','Right','Outer/Full','Inner')
    if JoinTypeName=="Left" or JoinTypeName=="left": JoinTypeVal=0
    if JoinTypeName=="Right" or JoinTypeName=="right": JoinTypeVal=1
    if JoinTypeName=="Outer" or JoinTypeName=="outer": JoinTypeVal=2
    if JoinTypeName=="Inner" or JoinTypeName=="inner": JoinTypeVal=3
    if JoinTypeName=="":
        ListJoinType.current(2)
    else:
        ListJoinType.current(JoinTypeVal)
    ListJoinType.grid(row=1,column=0)
    BtnSbmtJoinType = Button(JoinTypeWin,text="Submit",command=FnJoinType)
    BtnSbmtJoinType.grid(row=2,column=0)
   
    JoinTypeWin.mainloop()
   
   
def FnJoinType():
    global JoinTypeName
    JoinTypeName = ListJoinType.get()
    if JoinTypeName =="Outer/Full":
        JoinTypeName = "outer"
    if JoinTypeName =="Inner":
        JoinTypeName = "inner"
    if JoinTypeName =="Left":
        JoinTypeName = "left"
    if JoinTypeName =="Right":
        JoinTypeName = "right"
       
       

##########About/Help option
def about():
   AbtWin = Toplevel(root)
   AbtWin.overrideredirect(1)
   AbtWin.configure(bg="#ffffff")
    ######Message about developer
   Msg = Message(AbtWin, text="This application is developed using TKinter and pandas library of Python by 'Piyush Chanchal'. It can be used to merge two csv files. In case of any concern, please contact to email id Piyush.Chanchal@hotmail.com",bg='#000000',fg='#ffffff')
   Msg.pack()
   OKBtn= Button(AbtWin,text='OK',width=10,command=AbtWin.destroy,bg='#00A4EF',fg='#ffffff')
   OKBtn.pack()
   AbtWin.mainloop()
   
   
       
       


root = Tk()

BgColor='#333333'
BgColorOth='#737373'
TxtFont="Arial Narrow"

#########Current file directory
dir_path = os.path.dirname(os.path.realpath(__file__))
photo = PhotoImage(file = str(dir_path) + "\\" + "Images\Icon.png")
root.iconphoto(False, photo)
root.title("Merge CSV files")



root.geometry("390x450")
root.minsize(390,450)
root.maxsize(390,450)

root.configure(bg=BgColor)


############Menu section
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu, tearoff=False)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Load first CSV', command=openFirstCSV_file)
filemenu.add_command(label='Load second CSV', command=openSecondCSV_file)
filemenu.add_command(label='Select Output Directory', command=openOut_file)
filemenu.add_command(label='Exit', command=root.destroy)
ExportMenu = Menu(menu, tearoff=False)
menu.add_cascade(label='Merge', menu=ExportMenu)
ExportMenu.add_command(label='Merge',command=Merge)
OptionsMenu = Menu(menu, tearoff=False)
menu.add_cascade(label='Options', menu=OptionsMenu)
OptionsMenu.add_command(label='Key Column name',command=KeyName)
OptionsMenu.add_command(label='Join Type',command=JoinType)
helpmenu = Menu(menu, tearoff=False)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About',command=about)
##############End of menu section


#########Header label of app
Header = Label(root, text="     Merge two CSVs into one ...", font=(TxtFont, 20, "bold"),bg=BgColor,fg="#00A4EF")
Header.grid(row=0,column=0)



#######First CSV input section
EmptyRow1 = Label(root,text="",bg=BgColor)
EmptyRow1.grid(row=1,column=0)

FirstCSVPath = Label(root, text="Full path of First CSV file                          ",font=(TxtFont,15),padx=0,pady=0,bg=BgColor,fg="#ffffff")
FirstCSVPath.grid(row=2, column=0)

FirstCSVPathValue = StringVar()
FirstCSVPathEntry = Entry(root, textvariable=FirstCSVPathValue,width=50,bg='#ffffff',fg='#00A4EF')
FirstCSVPathEntry.grid(row=3, column=0)

btn1 = Button(root, text ='Browse...', command = lambda:openFirstCSV_file(),bg='#00A4EF',fg='#ffffff')
btn1.grid(row=3, column=1)
#######End of first CSV input section





#######Second CSV input section
EmptyRow2 = Label(root,text="",bg=BgColor)
EmptyRow2.grid(row=4,column=0)

SecondCSVPath = Label(root, text="  Full path of Second CSV file                     ",font=(TxtFont,15),bg=BgColor,fg="#ffffff",padx=0,pady=0)
SecondCSVPath.grid(row=5, column=0)


SecondCSVPathValue= StringVar()
SecondCSVPathEntry = Entry(root, textvariable=SecondCSVPathValue,width=50,bg='#ffffff',fg='#00A4EF')
SecondCSVPathEntry.grid(row=6, column=0)

btn2 = Button(root, text ='Browse...', command = lambda:openSecondCSV_file(),bg='#00A4EF',fg='#ffffff')
btn2.grid(row=6, column=1)
#######End of Second CSV input section




#####Output Directory input section
EmptyRow3 = Label(root,text="",bg=BgColor)
EmptyRow3.grid(row=7,column=0)


OutputPath = Label(root, text="Select output CSV file directory                ",font=(TxtFont,15),bg=BgColor,fg="#ffffff",padx=0,pady=0)
OutputPath.grid(row=8, column=0)

OutputPathValue = StringVar()
OutputPathEntry = Entry(root, textvariable=OutputPathValue,width=50,bg='#ffffff',fg='#00A4EF')
OutputPathEntry.grid(row=9, column=0)

btn3 = Button(root, text ='Browse...', command = lambda:openOut_file(),bg='#00A4EF',fg='#ffffff')
btn3.grid(row=9, column=1)
#####End of output Directory input section







##############Ouput CSV file name input section
EmptyRow4 = Label(root,text="",bg=BgColor)
EmptyRow4.grid(row=10,column=0)


OutFileName = Label(root, text="Output CSV file name                            ",font=(TxtFont,15),bg=BgColor,fg="#ffffff",padx=0,pady=0)
OutFileName.grid(row=11, column=0)

OutFileNameValue = StringVar()
OutFileNameEntry = Entry(root, textvariable=OutFileNameValue,width=50,bg='#ffffff',fg='#00A4EF')
OutFileNameEntry.grid(row=12, column=0)
##############End of ouput CSV file name input section




#############Empty rows in main window
EmptyRow4 = Label(root,text="",bg=BgColor)
EmptyRow4.grid(row=13,column=0)

EmptyRow5 = Label(root,text="",bg=BgColor)
EmptyRow5.grid(row=14,column=0)


ErrFirstCSVObjExist=0
ErrSecondCSVObjExist=0
ErrOutObjExist=0
ErrOutNameObjExist=0
global KeyColName
KeyColName=""
global JoinTypeName
JoinTypeName = ""
   
btn4 = Button(root, text ='               Merge                        ', font=("Arial", 10, "bold"),padx=50,pady=10,bg="#00A4EF",fg="#ffffff",activebackground=BgColorOth,command = lambda:Merge())
btn4.grid(row=15, column=0)


root.mainloop()