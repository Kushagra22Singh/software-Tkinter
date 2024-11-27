from tkinter import *                                   #
from tkinter import ttk                                #
from tkinter.ttk import Progressbar             #
from turtle import*                                     #
import turtle                                              #           
import time as t                                       #                                         importing required libraries 
from PIL import ImageTk,Image,ImageSequence  #
from tkinter import messagebox                 #
from tkinter.font import Font                     #
from math import *                                   #
from datetime import datetime                  #
import pygame                                         #
import mysql.connector as c                     #
import prettytable                                     #
import numpy                                           #
import geopy                                            #
import random                                           #
import pyodbc                                           #
import matplotlib.pyplot as plt                  #

pygame.mixer.init()

con=c.connect(host='localhost',user='root',passwd='argahsuk@hgnis',database='trial')
cursor=con.cursor()
def kush():
    global root
    root=Tk()
    root.configure(bg='cyan')
    root.title('KUSHAGRA')
    root.geometry('1000x1000')
    img=ImageTk.PhotoImage(Image.open(r"c:\gui\res.jpg"))
    my_label=Label(image=img)
    my_label.pack()
    btn1=Button(root,text='open_new_widow',command=popup,font=('Times',20),bg='lime')
    btn2=Button(root,text='close_all_windows',command=lambda: root.destroy(),font=('Times',20),bg='red')
    btn1.place(x=150,y=500)
    btn2.place(x=600,y=500)
##    btn3=Button(root,text='RATE MY APP',font=('Times',15),bg='pink',command=rate).place(x=600,y=600)
    btn4=Button(root,text='OPEN ADMIN SETTINGS',command=popup,font=('Mistral',20),bg='lemonchiffon').place(x=330,y=600)
    root.mainloop()

def admin():
    global scr7
    scr7=Toplevel()
    scr7.configure(bg='cyan')
    scr7.geometry('500x500')
    lbl_1=Label(scr7,text="ADMIN SETTINGS OPTIONS",font=('Helvatica',20),bg='lime').pack()
    btn_1=Button(scr7,text='REVIEW RATINGS',command=rew_rat,font=('Helvatica',20),bg='lemonchiffon').place(x=10,y=100)
    btn_01=Button(scr7,text='REVIEW GRAPHICAL ANALYTICS',command=plt_rev,font=('Helvatica',20),bg='lemonchiffon').place(x=300,y=100)
    btn_2=Button(scr7,text='REVIEW ORDER HISTORY',command=ord_his,font=('Helvatica',20),bg='lemonchiffon').place(x=10,y=200)
    btn_02=Button(scr7,text='REVIEW GRAPHICAL ANALYTICS',command=plt_ord,font=('Helvatica',20),bg='lemonchiffon').place(x=400,y=200)
    btn_2=Button(scr7,text='REVIEW CARD DETAILS',command=car_det,font=('Helvatica',20),bg='lemonchiffon').place(x=10,y=300)
    btn_3=Button(scr7,text='SEARCH RECORDS VIA FOOD NAME',command=search,font=('Helvatica',20),bg='lemonchiffon').place(x=10,y=400)


    scr7.mainloop()



def rew_rat():
    scr7.destroy()
    global scr8
    scr8=Toplevel()
    scr8.configure(bg='cyan')

    main_frame=Frame(scr8)
    main_frame.pack(fill=BOTH,expand=1)

    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

    my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    second_frame=Frame(my_canvas)
    
    my_canvas.create_window((0,0),window=second_frame,anchor="nw")
    
    a_p=['rating','review','used_at_time']
    d=prettytable.PrettyTable(a_p)
    
    cursor.execute("select * from software_4")
    myresult=cursor.fetchall()
    for i in myresult:
        list_1=[i[0],i[1],i[2]]
        d.add_row(list_1)
    label=Label(second_frame,text=d,font=('Times',20)).pack()
    con.commit

    scr8.mainloop()
    
def ord_his():
    scr7.destroy()
    global scr9
    scr9=Toplevel()
    scr9.configure(bg='magenta')
    scr9.geometry('1330x1500')
    
    main_frame=Frame(scr9)
    main_frame.pack(fill=BOTH,expand=1)

    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

    my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    second_frame=Frame(my_canvas)
    
    my_canvas.create_window((0,0),window=second_frame,anchor="nw")
    
    
    a_p=['food_code','food_name','members_seleceted','beverages','glasses_selected','adjustments','salad','soup','pickle','soda']
    d=prettytable.PrettyTable(a_p)
    
    cursor.execute("select * from software_2")
    myresult=cursor.fetchall()
    for i in myresult:
        list_1=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]]
        d.add_row(list_1)
    label=Label(second_frame,text=d,font=('Times',20),bg='pink').pack()
    con.commit

    scr9.mainloop()

def car_det():
    scr7.destroy()
    global scr10
    scr10=Toplevel()
    scr10.configure(bg='lemonchiffon')

    main_frame=Frame(scr10)
    main_frame.pack(fill=BOTH,expand=1)

    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

    my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    second_frame=Frame(my_canvas)
    
    my_canvas.create_window((0,0),window=second_frame,anchor="nw")

    a_p=['card_number','expiry_month','expiry_date','phone_number','address','near_by_landmark']
    d=prettytable.PrettyTable(a_p)
    
    cursor.execute("select * from software_3")
    myresult=cursor.fetchall()
    for i in myresult:
        list_1=[i[0],i[1],i[2],i[3],i[4],i[5]]
        d.add_row(list_1)
    label=Label(second_frame,text=d,font=('Times',20)).pack()
    con.commit


    scr10.mainloop()
    
def plt_rev():
##    normalize=False
    r_1=[]
    cursor.execute("select * from software_4")
    myresult=cursor.fetchall()
    for i in myresult:
        r_1.append(i[0])
    x=[r_1.count(5),r_1.count(4),r_1.count(3),r_1.count(2),r_1.count(1)]
    lbl=['EXCELLENT','V-GOOD','GOOD','ITs OK','NOT SO GOOD']
    col=['cyan','magenta','gold','pink','lemonchiffon']
    plt.title('RATINGS OF SOFTWARE')
    plt.pie(x,labels=lbl,colors=col,autopct='%1.1f%%')
    plt.legend(loc='lower center')
    plt.show()

def plt_ord():
    r_1=[]
    cursor.execute("select * from software_2")
    myresult=cursor.fetchall()
    for i in myresult:
        r_1.append(i[0])
##    print(r_1)
    x=[r_1.count(1),r_1.count(2),r_1.count(3),r_1.count(4),r_1.count(5),r_1.count(6),r_1.count(7),r_1.count(8),r_1.count(9),r_1.count(10),r_1.count(11),r_1.count(12),r_1.count(13),r_1.count(14),r_1.count(15),r_1.count(16),r_1.count(17),r_1.count(18),r_1.count(19),r_1.count(20)]
    lbl=['CHOLE','CHICKEN','BIRYANI','GERMAN MEAT','LAMB MEAT','MALFO','FISH CURRY','OPA','RISSOTO','RAULADE','FALAFEL','PANEER PAKODA','SAMOSA','ALOO TIKKI','SNACKS','ITALIAN','PANI PURI','FRENCH FRIES','APPLE JUICE','ORANGE JUICE']
    col=['cyan','magenta','gold','pink','lemonchiffon','blue','red','yellow','orange','green','lime','navy','black','purple','brown','indigo','lavender','azure','aqua']
    plt.title('FOOD ITEMS ORDERED')
##    plt.pie(x,labels=lbl,autopct='%1.1f%%')
    plt.xlabel('NAME OF FOOD ITEMS')
    plt.ylabel('NUMBER OF TIMES ORDERED')
    plt.bar(range(len(x)),x)
    plt.xticks(range(len(x)),lbl,rotation='vertical')
    plt.legend(loc='right')
    plt.show()

def search():
    scr7.destroy()
    global scr11
    global e_01
    scr11=Toplevel()
    scr11.configure(bg='navy')
##    scr11.geometry('500x500')
    lbl_1=Label(scr11,text='SEARCH RECORDS',font=('Times',20),bg='lime').pack()
    lbl_2=Label(scr11,text='ENTER FOOD NAME TO BE SEARCHED',font=('Times',20),bg='lime').place(x=10,y=40)
    e_01=Entry(scr11,font=('Helvatica',20))
    e_01.place(x=580,y=40)
    btn=Button(scr11,text='SEARCH WITHIN RECORDS',command=search_1,font=('Times',20),bg='lime').place(x=200,y=100)

    scr11.mainloop()

    
################                                              ERROR HAS TO BE FUCKED TILL IT's LAST BREATH                                             #######

def search_1():
    l_0=[]
    k_0=[]
    a_0=[]
    cursor.execute("select food_name from software_2")
    my=cursor.fetchall()
    for i in my:
        l_0.append(i)
    for i in range(len(l_0)):
        k1=list(l_0[i])
        k_0.append(k1)
    for i in range(len(k_0)):
        a_0.append(k_0[i][0])
    if e_01.get() in ['CHOLE','CHICKEN','BIRYANI','GERMAN MEAT','LAMB MEAT','MALFO','FISH CURRY','OPA','RISSOTO','RAULADE','FALAFEL','PANEER PAKODA','SAMOSA','ALOO TIKKI','SNACKS','ITALIAN','PANI PURI','FRENCH FRIES','APPLE JUICE','ORANGE JUICE']:
        if e_01.get() in a_0:
            global scr12
            scr12=Toplevel()
            scr12.geometry('500x500')
            scr12.configure(bg='pink')
            lbl=Label(scr12,text='THE RECORDS ARE FOUND AS FOLLOWS',font=('Helvatica',25)).pack()
            main_frame=Frame(scr12)
            main_frame.pack(fill=BOTH,expand=1)

            my_canvas=Canvas(main_frame)
            my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

            my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
            my_scrollbar.pack(side=RIGHT,fill=Y)

            my_canvas.configure(yscrollcommand=my_scrollbar.set)
            my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

            second_frame=Frame(my_canvas)
            
            my_canvas.create_window((0,0),window=second_frame,anchor="nw")
            
            
            a_p=['food_code','food_name','members_seleceted','beverages','glasses_selected','adjustments','salad','soup','pickle','soda']
            d=prettytable.PrettyTable(a_p)
            
            cursor.execute("select * from software_2 where food_name='"+e_01.get()+"'")
            myresult=cursor.fetchall()
            for i in myresult:
                list_1=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]]
                d.add_row(list_1)
            label=Label(second_frame,text=d,font=('Times',20),bg='pink').pack()
            con.commit
            scr11.destroy()
            scr12.mainloop()
        else:
            scr12=Toplevel()
            scr12.geometry('500x500')
            scr12.configure(bg='pink')
            lbl=Label(scr12,text='THE RECORDS ARE FOUND AS FOLLOWS',font=('Helvatica',25)).pack()
            lbl_1=Label(scr12,text="NO RECORDS FOUND DURING THE SEARCH",font=('Helvatica',25)).pack()
            scr11.destroy()
            scr12.mainloop()
            
    else:
        messagebox.showwarning('SEARCH','PLEASE ENTER CORRECT FOOD NAME')
    
    

    
def poop():
    uname=e1.get()
    password=e2.get()
    if uname=='' and password=='':
        messagebox.showwarning('LOGIN','WELCOME TO OUR SOFTWARE')
        first()                                                   
##        messagebox.showwarning('LOGIN','INPUT FIELD IS EMPTY')
    elif uname=='a' and password=='a':
        admin()
    else:
        messagebox.showwarning('LOGIN','UNAUTHORISED ACCESS DENIED')
    
        
def popup():
    nov=Toplevel()
    nov.geometry('370x150')
    nov.configure(bg='pink')
    global e1
    global e2
##    img1=ImageTk.PhotoImage(Image.open(r"c:\gui\blue.png"))
##    my_label1=Label(nov,image=img1)
    e1=Entry(nov,width=20,fg='blue')
    l1=Label(nov,text=' ENTER YOUR NAME::',font=('Times',12)).grid(row=0,column=0,padx=20,pady=10)
    e1.grid(row=0,column=1)
    l2=Label(nov,text='ENTER PASSWORD::',font=('Times',12)).grid(row=1,column=0)
    e2=Entry(nov,width=20,show='*',fg='red')
    e2.grid(row=1,column=1)

    b1=Button(nov,text='CONFIRM',command=poop,font=('Times',15))
    b1.grid(row=2,column=1,pady=20)


def fifth():
    octo=Toplevel()
    octo.geometry('1500x1500')
    octo.configure(bg='indigo')
    img12=ImageTk.PhotoImage(Image.open(r"c:\gui\chole2.png"))
    my_label12=Label(octo,image=img12)
    img13=ImageTk.PhotoImage(Image.open(r"c:\gui\chicken2.png"))
    my_label13=Label(octo,image=img13)
    global chi
    chi=260
    img14=ImageTk.PhotoImage(Image.open(r"c:\gui\biryani3.png"))
    my_label14=Label(octo,image=img14)
    global bir
    bir=240
    img15=ImageTk.PhotoImage(Image.open(r"c:\gui\germam1.png"))
    my_label15=Label(octo,image=img15)
    global ger
    ger=360
    img16=ImageTk.PhotoImage(Image.open(r"c:\gui\lamb_meat1.png"))
    my_label16=Label(octo,image=img16)
    global lam
    lam=100
    img17=ImageTk.PhotoImage(Image.open(r"c:\gui\malfo1.png"))
    my_label17=Label(octo,image=img17)
    global mal
    mal=560
    img18=ImageTk.PhotoImage(Image.open(r"c:\gui\fish2.png"))
    my_label18=Label(octo,image=img18)
    global fis
    fis=764
    img19=ImageTk.PhotoImage(Image.open(r"c:\gui\opa1.png"))
    my_label19=Label(octo,image=img19)
    global opa
    opa=523
    img20=ImageTk.PhotoImage(Image.open(r"c:\gui\risotto1.png"))
    my_label20=Label(octo,image=img20)
    global ris
    ris=934
    img21=ImageTk.PhotoImage(Image.open(r"c:\gui\roulade1.png"))
    my_label21=Label(octo,image=img21)
    global rou
    rou=342
    my_label22=Label(octo,text='CHOLE KULCHE',font=('Western',12),padx=10,pady=10,bg="magenta")
    my_label23=Label(octo,text='CHICKEN',padx=10,pady=10,bg="yellow")
    my_label24=Label(octo,text='BIRYANI',padx=10,pady=10,bg="cyan")
    my_label25=Label(octo,text='GERMAN MEAT',padx=10,pady=10,bg="red")
    my_label26=Label(octo,text='LAMB MEAT',padx=10,pady=10,bg="green")
    my_label27=Label(octo,text='MALFO',padx=10,pady=10,bg="gold")
    my_label28=Label(octo,text='FISH CURRY',padx=10,pady=10,bg="navy")
    my_label29=Label(octo,text='OPA',padx=10,pady=10,bg="lime")
    my_label30=Label(octo,text='RISOTTO',padx=10,pady=10,bg="lemonchiffon")
    my_label31=Label(octo,text='ROULADE',padx=10,pady=10,bg="orange")
    Label(octo,text='160/-',font=('Times',15),padx=5,pady=5).place(x=205,y=255)
    Label(octo,text='260/-',font=('Times',15),padx=5,pady=5).place(x=425,y=255)
    Label(octo,text='240/-',font=('Times',15),padx=5,pady=5).place(x=725,y=255)
    Label(octo,text='360/-',font=('Times',15),padx=5,pady=5).place(x=1035,y=255)
    Label(octo,text='100/-',font=('Times',15),padx=5,pady=5).place(x=1285,y=255)
    Label(octo,text='1',font=('Times',15),padx=5,pady=5).place(x=205,y=295)
    Label(octo,text='2',font=('Times',15),padx=5,pady=5).place(x=425,y=295)
    Label(octo,text='3',font=('Times',15),padx=5,pady=5).place(x=725,y=295)
    Label(octo,text='4',font=('Times',15),padx=5,pady=5).place(x=1035,y=295)
    Label(octo,text='5',font=('Times',15),padx=5,pady=5).place(x=1285,y=295)

    Label(octo,text='560/-',font=('Times',15),padx=5,pady=5).place(x=185,y=600)
    Label(octo,text='764/-',font=('Times',15),padx=5,pady=5).place(x=425,y=600)
    Label(octo,text='523/-',font=('Times',15),padx=5,pady=5).place(x=715,y=600)
    Label(octo,text='934/-',font=('Times',15),padx=5,pady=5).place(x=1015,y=600)
    Label(octo,text='342/-',font=('Times',15),padx=5,pady=5).place(x=1275,y=600)
    Label(octo,text='6',font=('Times',15),padx=5,pady=5).place(x=185,y=640)
    Label(octo,text='7',font=('Times',15),padx=5,pady=5).place(x=425,y=640)
    Label(octo,text='8',font=('Times',15),padx=5,pady=5).place(x=715,y=640)
    Label(octo,text='9',font=('Times',15),padx=5,pady=5).place(x=1015,y=640)
    Label(octo,text='10',font=('Times',15),padx=5,pady=5).place(x=1275,y=640)    
    
    tn11=Button(octo,text='BACK',command=lambda: octo.destroy(),bg="red")
    
    tn12=Button(octo,text='PROCEED',bg='cyan',command=chole_1)
    tn13=Button(octo,text='PROCEED',bg='cyan',command=chole_1)
    tn14=Button(octo,text='PROCEED',bg='cyan',command=chole_1)
    tn15=Button(octo,text='PROCEED',bg='cyan',command=chole_1)
    tn16=Button(octo,text='PROCEED',bg='cyan',command=chole_1)
    tn17=Button(octo,text='PROCEED',bg='cyan',command=chole_1)
    tn18=Button(octo,text='PROCEED',bg='cyan',command=chole_1)
    tn19=Button(octo,text='PROCEED',bg='cyan',command=chole_1)
    tn20=Button(octo,text='PROCEED',bg='cyan',command=chole_1)
    tn21=Button(octo,text='PROCEED',bg='cyan',command=chole_1)
    
    my_label12.grid(row=0,column=0)
    my_label13.grid(row=0,column=1)
    my_label14.grid(row=0,column=2)
    my_label15.grid(row=0,column=3)
    my_label16.grid(row=0,column=4)
    my_label22.grid(row=1,column=0)
    my_label23.grid(row=1,column=1)
    my_label24.grid(row=1,column=2)
    my_label25.grid(row=1,column=3)
    my_label26.grid(row=1,column=4)
    my_label27.grid(row=4,column=0)
    my_label28.grid(row=4,column=1)
    my_label29.grid(row=4,column=2)
    my_label30.grid(row=4,column=3)
    my_label31.grid(row=4,column=4)    
    my_label17.grid(row=3,column=0)
    my_label18.grid(row=3,column=1)
    my_label19.grid(row=3,column=2)
    my_label20.grid(row=3,column=3)
    my_label21.grid(row=3,column=4)
    tn12.grid(row=2,column=0,padx=10,pady=10)
    tn13.grid(row=2,column=1)
    tn14.grid(row=2,column=2)
    tn15.grid(row=2,column=3)
    tn16.grid(row=2,column=4)
    tn17.grid(row=5,column=0,padx=10,pady=10)
    tn18.grid(row=5,column=1)
    tn19.grid(row=5,column=2)
    tn20.grid(row=5,column=3)
    tn21.grid(row=5,column=4)

    tn11.grid(row=6,column=0)
    octo.mainloop()
    
def chole_1():
    global ch
    ch=160
    global scr1
    global r
    global s
    global w
    global x
    global z
    global k1
    global u
    global a
    global e3
    
    scr1=Toplevel()
    scr1.geometry('450x570')
    scr1.configure(bg='lime')
    
    r=StringVar()
    s=StringVar()
    w=StringVar()
    x=StringVar()
    z=StringVar()
    k1=StringVar()
    u=StringVar()
    a=StringVar()
    
    k1.set('SINGLE')
    a.set('BEER')
    u.set('1')
    r.set('YES')
    s.set('YES')
    w.set('YES')
    x.set('YES')
    z.set('YES')
    

##    global r6
##    global r7
##    global r8
##    global r9
##    global r10
    Label(scr1,text='ENTER FOOD CODE:',font=('Western',15),bg='darkorange').grid(row=0,column=0)
    e3=Entry(scr1,width=10,font=('Helvetica',15))
    e3.grid(row=0,column=1)
##    img22=ImageTk.PhotoImage(Image.open(r"c:\gui\chole5.png"))
##    my_label22=Label(scr1,image=img22).grid(row=0,column=0,padx=5,pady=5)
        
    my_label32=Label(scr1,text='SELECT NO. OF MEMBERS',font=('Western',10),bg='darkorange').grid(row=1,column=0,padx=5)
    my_label33=Label(scr1,text='COMPLEMENTRY BEVERAGES',font=('Western',10),bg='darkorange').grid(row=2,column=0,padx=5)
    my_label34=Label(scr1,text='NO. OF GLASSES',font=('Western',10),bg='darkorange').grid(row=3,column=0,padx=5)
    my_label35=Label(scr1,text='ADJUSTMENTS',font=('Western',10),bg='darkorange').place(x=60,y=320)
    my_label36=Label(scr1,text='SALAD',font=('Western',10),bg='darkorange').place(x=60,y=360)
    my_label37=Label(scr1,text='SOUP',font=('Western',10),bg='darkorange').place(x=60,y=400)
    my_label38=Label(scr1,text='PICKLE',font=('Western',10),bg='darkorange').place(x=60,y=440)
    my_label39=Label(scr1,text='SODA',font=('Western',10),bg='darkorange').place(x=60,y=480)
##    salad, soup, pickle, soda, cheese,spicy  
    drop1=OptionMenu(scr1,k1,'JOINT FAMILY','PACK OF FOUR','SINGLE','COUPLE').grid(row=1,column=1,padx=5)
    drop2=OptionMenu(scr1,a,'BEER','JUICE','WHISKEY','VODKA','RUM','WINE').grid(row=2,column=1,padx=5)
    drop3=OptionMenu(scr1,u,'1','2','3','4','5','6').grid(row=3,column=1,padx=5)
    r1=Radiobutton(scr1,text='more cheesy',variable=r,value='YES',font=('Times',12)).place(x=200,y=320)
    r2=Radiobutton(scr1,text='more spicy',variable=r,value='NO',font=('Times',12)).place(x=330,y=320)
    r3=Radiobutton(scr1,text='YES',variable=s,value='YES',font=('Times',12)).place(x=200,y=360)
    r4=Radiobutton(scr1,text='NO',variable=s,value='NO',font=('Times',12)).place(x=330,y=360)
    r5=Radiobutton(scr1,text='YES',variable=w,value='YES',font=('Times',12)).place(x=200,y=400)
    r6=Radiobutton(scr1,text='NO',variable=w,value='NO',font=('Times',12)).place(x=330,y=400)
    r7=Radiobutton(scr1,text='YES',variable=x,value='YES',font=('Times',12)).place(x=200,y=440)
    r8=Radiobutton(scr1,text='NO',variable=x,value='NO',font=('Times',12)).place(x=330,y=440)
    r9=Radiobutton(scr1,text='YES',variable=z,value='YES',font=('Times',12)).place(x=200,y=480)
    r10=Radiobutton(scr1,text='NO',variable=z,value='NO',font=('Times',12)).place(x=330,y=480)
    btn=Button(scr1,text='PROCEED TO PAY',font=('Times',10),bg='cyan',padx=10,pady=10,command=third_1).place(x=170,y=520)
##    btn1=Button(scr1,text='CONTINUE',command=photo).place(x=5,y=50)
    scr1.mainloop()


    
##############################        ch=160         #####################################################




def third_1():
    global jul
    jul=Toplevel()
    jul.geometry('550x500')
    jul.configure(bg='red')
    global k
    global e
    global str_out
    global drop1
    k=StringVar()
    
    k.set('DISCOUNT')
    
    my_label40=Label(jul,text='SELECT PAYMENT METHOD',font=('Western',15),bg='orange').pack()
    my_label45=Label(jul,text='YOUR BILL BEFORE DISCOUNT :',font=('Western',15),bg='orange').place(x=5,y=35)
    if e3.get()=='1':
        my_label46=Label(jul,text='160',font=('Western',15),bg='orange').place(x=350,y=35)
    elif e3.get()=='2':
        my_label46=Label(jul,text='260',font=('Western',15),bg='orange').place(x=350,y=35)
    elif e3.get()=='3':
        my_label46=Label(jul,text='240',font=('Western',15),bg='orange').place(x=350,y=35)
    elif e3.get()=='4':
        my_label46=Label(jul,text='360',font=('Western',15),bg='orange').place(x=350,y=35)
    elif e3.get()=='5':
        my_label46=Label(jul,text='100',font=('Western',15),bg='orange').place(x=350,y=35)
    elif e3.get()=='6':
        my_label46=Label(jul,text='560',font=('Western',15),bg='orange').place(x=350,y=35)
    elif e3.get()=='7':
        my_label46=Label(jul,text='764',font=('Western',15),bg='orange').place(x=350,y=35)
    elif e3.get()=='8':
        my_label46=Label(jul,text='523',font=('Western',15),bg='orange').place(x=350,y=35)
    elif e3.get()=='9':
        my_label46=Label(jul,text='934',font=('Western',15),bg='orange').place(x=350,y=35)
    elif e3.get()=='10':
        my_label46=Label(jul,text='342',font=('Western',15),bg='orange').place(x=350,y=35)
    elif e3.get()=='11':
        my_label46=Label(jul,text=ch,font=('Western',15),bg='orange').place(x=350,y=35)
    elif e3.get()=='12':
        my_label46=Label(jul,text='260',font=('Western',15),bg='orange').place(x=350,y=35)
    elif e3.get()=='13':
        my_label46=Label(jul,text='240',font=('Western',15),bg='orange').place(x=350,y=35)
    elif e3.get()=='14':
        my_label46=Label(jul,text='360',font=('Western',15),bg='orange').place(x=350,y=35)
    elif e3.get()=='15':
        my_label46=Label(jul,text='100',font=('Western',15),bg='orange').place(x=350,y=35)
    elif e3.get()=='16':
        my_label46=Label(jul,text='560',font=('Western',15),bg='orange').place(x=350,y=35)
    elif e3.get()=='17':
        my_label46=Label(jul,text='764',font=('Western',15),bg='orange').place(x=350,y=35)
    elif e3.get()=='18':
        my_label46=Label(jul,text='523',font=('Western',15),bg='orange').place(x=350,y=35)
    elif e3.get()=='19':
        my_label46=Label(jul,text='934',font=('Western',15),bg='orange').place(x=350,y=35)
    elif e3.get()=='20':
        my_label46=Label(jul,text='342',font=('Western',15),bg='orange').place(x=350,y=35)
    elif e3.get()=='':
        messagebox.showwarning('FOOD CODE','FOOD CODE BOX HAS TO BE FILLED')
    else:
        messagebox.showwarning('FOOD CODE','PLEASE ENTER CORRECT CODE')
##    my_label46=Label(jul,text=ch,font=('Western',15),bg='orange').place(x=350,y=35)
    my_label47=Label(jul,text='APPLY DISCOUNT COUPOUN :',font=('Helvitica',15),bg='orange').place(x=5,y=70)
    drop1=OptionMenu(jul,k,'25 % OFF ON FIRST ORDER','40 % OFF IF BILL PAID BY UPI ID','60 % OFF IF TAKEN NO ADJUSTMENT').place(x=350,y=70)
    my_label48=Label(jul,text='APPLY COUPOUN  CODE:',font=('Helvitica',15),bg='orange').place(x=5,y=105)
    e=Entry(jul,width=10,font=('Helvitica',15))
    e.place(x=350,y=105)
    btn=Button(jul,text='CALCULATE FINAL AMOUNT',font=('Times',12),command=calculate,padx=10,pady=10,bg='greenyellow').place(x=150,y=150)
    
    btn1=Button(jul,text='UPI ID',font=('Times',12),command=upi,padx=10,pady=10,bg='aqua').place(x=10,y=430)
    btn2=Button(jul,text='CASH ON DELIVERY',font=('Times',12),command=cod,padx=10,pady=10,bg='aqua').place(x=150,y=430)
    btn3=Button(jul,text='CARD',font=('Times',12),command=card,padx=10,pady=10,bg='aqua').place(x=390,y=430)
    
##    tn4=Button(jul,text='BACK',command=lambda: jul.destroy())
##    tn6=Button(jul,text='FORWARD',command=fourth)
##    tn4.pack()
##    tn6.pack()
    jul.mainloop()



def calculate():
    if '25' in k.get() and e.get()=='KUSH':
        my_label51=Label(jul,text='YOU GOT AN 25 % DICOUNT FROM KUSHAGRA ',font=('Helvitica',15),bg='orange').place(x=5,y=210)
        my_label51=Label(jul,text='GOT AN ADDITIONAL DISCOUNT OF 10 %',font=('Helvitica',15),bg='orange').place(x=5,y=270)
        ch=160-(160*(1/4)+160*(1/10))
        chi=260-(260*(1/4)+260*(1/10))
        bir=240-(240*(1/4)+240*(1/10))
        ger=360-(360*(1/4)+360*(1/10))
        lam=100-(100*(1/4)+100*(1/10))
        mal=560-(560*(1/4)+560*(1/10))
        fis=764-(764*(1/4)+764*(1/10))
        opa=523-(523*(1/4)+523*(1/10))
        ris=934-(934*(1/4)+934*(1/10))
        rou=342-(342*(1/4)+342*(1/10))
    elif '25' in k.get() and e.get()=='':
        my_label51=Label(jul,text='YOU GOT AN 25 % DICOUNT FROM KUSHAGRA ',font=('Helvitica',15),bg='orange').place(x=5,y=210)
        my_label51=Label(jul,text='YOU HAVENT USED ANY COUPOUN CODE',font=('Helvitica',15),bg='orange').place(x=5,y=270)
        ch=160-(160*(1/4))
        chi=260-(260*(1/4))
        bir=240-(240*(1/4))
        ger=360-(360*(1/4))
        lam=100-(100*(1/4))
        mal=560-(560*(1/4))
        fis=764-(764*(1/4))
        opa=523-(523*(1/4))
        ris=934-(934*(1/4))
        rou=342-(342*(1/4))
    elif '40' in k.get()  and e.get()=='KUSH':
        my_label51=Label(jul,text='YOU GOT AN 40 % DICOUNT FROM KUSHAGRA ',font=('Helvitica',15),bg='orange').place(x=5,y=210)
        my_label51=Label(jul,text='GOT AN ADDITIONAL DISCOUNT OF 10 %',font=('Helvitica',15),bg='orange').place(x=5,y=270)
        ch=160-(160*(2/5)+160*(1/10))
        chi=260-(260*(2/5)+260*(1/10))
        bir=240-(240*(2/5)+240*(1/10))
        ger=360-(360*(2/5)+360*(1/10))
        lam=100-(100*(2/5)+100*(1/10))
        mal=560-(560*(2/5)+560*(1/10))
        fis=764-(764*(2/5)+764*(1/10))
        opa=523-(523*(2/5)+523*(1/10))
        ris=934-(934*(2/5)+934*(1/10))
        rou=342-(342*(2/5)+342*(1/10))
    elif '40' in k.get()  and e.get()=='':
        my_label51=Label(jul,text='YOU GOT AN 40 % DICOUNT FROM KUSHAGRA ',font=('Helvitica',15),bg='orange').place(x=5,y=210)
        my_label51=Label(jul,text='YOU HAVENT USED ANY COUPOUN CODE',font=('Helvitica',15),bg='orange').place(x=5,y=270)
        ch=160-(160*(2/5))
        chi=260-(260*(2/5))
        bir=240-(240*(2/5))
        ger=360-(360*(2/5))
        lam=100-(100*(2/5))
        mal=560-(560*(2/5))
        fis=764-(764*(2/5))
        opa=523-(523*(2/5))
        ris=934-(934*(2/5))
        rou=342-(342*(2/5))
    elif '60' in k.get()  and e.get()=='KUSH':
        my_label51=Label(jul,text='YOU GOT AN 60 % DICOUNT FROM KUSHAGRA ',font=('Helvitica',15),bg='orange').place(x=5,y=210)
        my_label51=Label(jul,text='GOT AN ADDITIONAL DISCOUNT OF 10 %',font=('Helvitica',15),bg='orange').place(x=5,y=270)
        ch=160-(160*(3/5)+160*(1/10))
        chi=260-(260*(3/5)+260*(1/10))
        bir=240-(240*(3/5)+240*(1/10))
        ger=360-(360*(3/5)+360*(1/10))
        lam=100-(100*(3/5)+100*(1/10))
        mal=560-(560*(3/5)+560*(1/10))
        fis=764-(764*(3/5)+764*(1/10))
        opa=523-(523*(3/5)+523*(1/10))
        ris=934-(934*(3/5)+934*(1/10))
        rou=342-(342*(3/5)+342*(1/10))
    elif '60' in k.get()  and e.get()=='':
        my_label51=Label(jul,text='YOU GOT AN 60 % DICOUNT FROM KUSHAGRA ',font=('Helvitica',15),bg='orange').place(x=5,y=210)
        my_label51=Label(jul,text='YOU HAVENT USED ANY COUPOUN CODE',font=('Helvitica',15),bg='orange').place(x=5,y=270)
        ch=160-(160*(3/5))
        chi=260-(260*(3/5))
        bir=240-(240*(3/5))
        ger=360-(360*(3/5))
        lam=100-(100*(3/5))
        mal=560-(560*(3/5))
        fis=764-(764*(3/5))
        opa=523-(523*(3/5))
        ris=934-(934*(3/5))
        rou=342-(342*(3/5))
    else:
        my_label51=Label(jul,text='YOU HAVENT GOT ANY DISCOUNT',font=('Helvitica',15),bg='orange').place(x=5,y=210)
        my_label51=Label(jul,text='YOU HAVENT USED ANY COUPOUN CODE',font=('Helvitica',15),bg='orange').place(x=5,y=270)
        ch=160
        chi=260
        bir=240
        ger=360
        lam=100
        mal=560
        fis=764
        opa=523
        ris=934
        rou=342

    if e3.get()=='1':
        my_label50=Label(jul,text=ch,font=('Helvitica',15),bg='orange').place(x=350,y=340)
    elif e3.get()=='2':
        my_label50=Label(jul,text=chi,font=('Helvitica',15),bg='orange').place(x=350,y=340)
    elif e3.get()=='3':
        my_label50=Label(jul,text=bir,font=('Helvitica',15),bg='orange').place(x=350,y=340)
    elif e3.get()=='4':
        my_label50=Label(jul,text=ger,font=('Helvitica',15),bg='orange').place(x=350,y=340)
    elif e3.get()=='5':
        my_label50=Label(jul,text=lam,font=('Helvitica',15),bg='orange').place(x=350,y=340)
    elif e3.get()=='6':
        my_label50=Label(jul,text=mal,font=('Helvitica',15),bg='orange').place(x=350,y=340)
    elif e3.get()=='7':
        my_label50=Label(jul,text=fis,font=('Helvitica',15),bg='orange').place(x=350,y=340)
    elif e3.get()=='8':
        my_label50=Label(jul,text=opa,font=('Helvitica',15),bg='orange').place(x=350,y=340)
    elif e3.get()=='9':
        my_label50=Label(jul,text=ris,font=('Helvitica',15),bg='orange').place(x=350,y=340)
    elif e3.get()=='10':
        my_label50=Label(jul,text=rou,font=('Helvitica',15),bg='orange').place(x=350,y=340)
    elif e3.get()=='11':
        my_label50=Label(jul,text=ch,font=('Helvitica',15),bg='orange').place(x=350,y=340)
    elif e3.get()=='12':
        my_label50=Label(jul,text=chi,font=('Helvitica',15),bg='orange').place(x=350,y=340)
    elif e3.get()=='13':
        my_label50=Label(jul,text=bir,font=('Helvitica',15),bg='orange').place(x=350,y=340)
    elif e3.get()=='14':
        my_label50=Label(jul,text=ger,font=('Helvitica',15),bg='orange').place(x=350,y=340)
    elif e3.get()=='15':
        my_label50=Label(jul,text=lam,font=('Helvitica',15),bg='orange').place(x=350,y=340)
    elif e3.get()=='16':
        my_label50=Label(jul,text=mal,font=('Helvitica',15),bg='orange').place(x=350,y=340)
    elif e3.get()=='17':
        my_label50=Label(jul,text=fis,font=('Helvitica',15),bg='orange').place(x=350,y=340)
    elif e3.get()=='18':
        my_label50=Label(jul,text=opa,font=('Helvitica',15),bg='orange').place(x=350,y=340)
    elif e3.get()=='19':
        my_label50=Label(jul,text=ris,font=('Helvitica',15),bg='orange').place(x=350,y=340)
    elif e3.get()=='20':
        my_label50=Label(jul,text=rou,font=('Helvitica',15),bg='orange').place(x=350,y=340)
    else:
        my_label50=Label(jul,text='fuck off',font=('Helvitica',15),bg='orange').place(x=350,y=340)
    
    my_label49=Label(jul,text='THE FINAL CALCULATED AMOUNT:',font=('Helvitica',15),bg='orange').place(x=5,y=340)
    
def third_2():
    global scr3
    scr3=Toplevel()
    scr3.config(bg='aqua')
    scr3.geometry('500x500')
    
        



def upi():
    global scr2
    global e4
    global e5
    global e6
    global e7
    
    scr2=Toplevel()
    scr2.geometry('600x220')
    scr2.configure(bg='pink')
    my_label41=Label(scr2,text='ENTER YOUR ACCOUNT NUMBER::',font=('Western',15),bg='yellow').place(x=10,y=10)
    my_label42=Label(scr2,text='ENTER YOUR CCV::',font=('Western',15),bg='yellow').place(x=10,y=40)
    my_label43=Label(scr2,text='ENTER YOUR PHONE NUMBER::',font=('Western',15),bg='yellow').place(x=10,y=70)
    my_label44=Label(scr2,text='ENTER OTP(sent to no.)::',font=('Western',15),bg='yellow').place(x=10,y=120)
    
    e4=Entry(scr2,width=30)
    e4.place(x=380,y=14)
    e5=Entry(scr2,width=30,show='*')
    e5.place(x=380,y=44)
    e6=Entry(scr2,width=30)
    e6.place(x=380,y=74)
    e7=Entry(scr2,width=15)
    e7.place(x=380,y=124)
    btn=Button(scr2,text='VARIFYY DETAILS',font=('Helvetica',20),bg='lemonchiffon',command=dest).place(x=210,y=160)

##def progress():
##    x=0
##    while x<10:
##        time.sleep(1)
##        my_progress['value']+=20
##        x+=1
##        scr3.update_idletasks()
def progress():
    global root1
    root1=Toplevel()
    root1.geometry('300x300')
    
    bar=Progressbar(root1,orient=HORIZONTAL,length=100)
    
    bar.pack(pady=20)
    root1.mainloop() 
    x=0
    while x<100:
        t.sleep(0.1)
        bar['value']+=1
        x=x+1
        root1.update_idletasks()
      
    root1.destroy()
    first()


def dest():
    acc_no=e4.get()
    ccv=e5.get()
    ph_no=e6.get()
    otp=e7.get()
    if acc_no=='' or ccv=='' or ph_no=='' or otp=='' :
        messagebox.showwarning('VARIFICATION','PLEASE FILL THE REQURED FIELD')
    else:
        messagebox.showwarning('VARIFICATION','SUCESSUFULLY VARIFIED')
        scr2.destroy()
        final()


##    global my_progress
##    global scr3
##    scr3=Toplevel()
##    scr3.geometry('700x200')
##    scr3.configure(bg='royalblue')
##    my_label45=Label(scr3,text='RUKO ZARAA SABAR KRO !!!!!',bg='yellow',font=('Helvetica',25)).pack()
##    my_label45=Label(scr3,text='VARIFY HO RHA HAI !!!!!',bg='yellow',font=('Helvetica',25)).pack()
##    my_progress=ttk.Progressbar(scr3,orient=HORIZONTAL,length=300,mode='determinate').pack(pady=20)
##    btn=Button(scr3,text='fuck off',command=progress).pack()
##    progress()
####    scr2.after(10000,third_2)
def final():
    global scr5
    global my_label100
    scr5=Toplevel()
    scr5.configure(bg='gold')
    scr5.geometry('450x500')
    my_label59=Label(scr5,text='CHECK-OUT DETAILS',font=('Times',18),bg='MAGENTA').pack()
    my_label60=Label(scr5,text='YOUR ORDER OF',font=('Western',15),bg='yellow').place(x=30,y=50)
##    my_label65=Label(scr5,text='---------------------').place(x=50,y=50)
    
    if e3.get()=='1':
        my_label46=Label(scr5,text='CHOLE KULCHE',font=('Western',15),bg='orange').place(x=280,y=50)
    elif e3.get()=='2':
        my_label46=Label(scr5,text='CHICKEN',font=('Western',15),bg='orange').place(x=280,y=50)
    elif e3.get()=='3':
        my_label46=Label(scr5,text='BIRYANI',font=('Western',15),bg='orange').place(x=280,y=50)
    elif e3.get()=='4':
        my_label46=Label(scr5,text='GERMAN MEAT',font=('Western',15),bg='orange').place(x=280,y=50)
    elif e3.get()=='5':
        my_label46=Label(scr5,text='LAMB MEAT',font=('Western',15),bg='orange').place(x=280,y=50)
    elif e3.get()=='6':
        my_label46=Label(scr5,text='MALFO',font=('Western',15),bg='orange').place(x=280,y=50)
    elif e3.get()=='7':
        my_label46=Label(scr5,text='FISH CURRY',font=('Western',15),bg='orange').place(x=280,y=50)
    elif e3.get()=='8':
        my_label46=Label(scr5,text='OPA',font=('Western',15),bg='orange').place(x=280,y=50)
    elif e3.get()=='9':
        my_label46=Label(scr5,text='RISSOTO',font=('Western',15),bg='orange').place(x=280,y=50)
    elif e3.get()=='10':
        my_label46=Label(scr5,text='RAULADE',font=('Western',15),bg='orange').place(x=280,y=50)
    elif e3.get()=='11':
        my_label46=Label(scr5,text='FALAFEL',font=('Western',15),bg='orange').place(x=280,y=50)
    elif e3.get()=='12':
        my_label46=Label(scr5,text='PANEER PAKODA',font=('Western',15),bg='orange').place(x=280,y=50)
    elif e3.get()=='13':
        my_label46=Label(scr5,text='SAMOSA',font=('Western',15),bg='orange').place(x=280,y=50)
    elif e3.get()=='14':
        my_label46=Label(scr5,text='ALOO TIKKI',font=('Western',15),bg='orange').place(x=280,y=50)
    elif e3.get()=='15':
        my_label46=Label(scr5,text='SNACKS',font=('Western',15),bg='orange').place(x=280,y=50)
    elif e3.get()=='16':
        my_label46=Label(scr5,text='ITALIAN',font=('Western',15),bg='orange').place(x=280,y=50)
    elif e3.get()=='17':
        my_label46=Label(scr5,text='PANI PURI',font=('Western',15),bg='orange').place(x=280,y=50)
    elif e3.get()=='18':
        my_label46=Label(scr5,text='FRENCH FRIES',font=('Western',15),bg='orange').place(x=280,y=50)
    elif e3.get()=='19':
        my_label46=Label(scr5,text='APPLE JUICE',font=('Western',15),bg='orange').place(x=280,y=50)
    elif e3.get()=='20':
        my_label46=Label(scr5,text='ORANGE JUICE',font=('Western',15),bg='orange').place(x=280,y=50)
    mylabel_61=Label(scr5,text='HAVE BEEN PLACED',font=('Helvatica',20),bg='aqua').place(x=70,y=90)
    mylabel_62=Label(scr5,text='SUCCESSFULLY ',font=('Times',25),bg='pink').place(x=70,y=140)

    img21=ImageTk.PhotoImage(Image.open(r"c:\gui\bhau1.png"))
    my_label21=Label(scr5,image=img21)
    my_label21.place(x=150,y=200)
    btn1=Button(scr5,text='TRACK YOUR ORDER',font=('Times',15),bg='pink',command=map1).place(x=100,y=310)
    btn3=Button(scr5,text='RATE MY APP',font=('Times',15),bg='pink',command=rate).place(x=100,y=360)
##    btn2=Button(scr5,text='VIEW TIME REMAINING',font=('Times',15),bg='pink',command=update_time).place(x=100,y=360)
    
    val=['CHOLE','CHICKEN','BIRYANI','GERMAN MEAT','LAMB MEAT','MALFO','FISH CURRY','OPA','RISSOTO','RAULADE','FALAFEL','PANEER PAKODA','SAMOSA','ALOO TIKKI','SNACKS','ITALIAN','PANI PURI','FRENCH FRIES','APPLE JUICE','ORANGE JUICE']
    
##    if e3.get()=='1':
##        query="""insert into software_2(food_code,food_name,members_selected,beverages,glasses_selected,adjustments,salad,soup,pickle,soda) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
##        val=(e3.get(),'CHOLE KULCHE',k1.get(),a.get(),u.get(),r.get(),s.get(),w.get(),x.get(),z.get())
##
##        
##    elif e3.get()=='2':
##        query="""insert into software_2(food_code,food_name,members_selected,beverages,glasses_selected,adjustments,salad,soup,pickle,soda) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
##        val=(e3.get(),'CHICKEN',k1.get(),a.get(),u.get(),r.get(),s.get(),w.get(),x.get(),z.get())
##        
##    elif e3.get()=='3':
##        query="""insert into software_2(food_code,food_name,members_selected,beverages,glasses_selected,adjustments,salad,soup,pickle,soda) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
##        val=(e3.get(),'BIRYANI',k1.get(),a.get(),u.get(),r.get(),s.get(),w.get(),x.get(),z.get())
##        
##    elif e3.get()=='4':
##        query="""insert into software_2(food_code,food_name,members_selected,beverages,glasses_selected,adjustments,salad,soup,pickle,soda) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
##        val=(e3.get(),'GERMAN MEAT',k1.get(),a.get(),u.get(),r.get(),s.get(),w.get(),x.get(),z.get())
##       
##    elif e3.get()=='5':
##        query="""insert into software_2(food_code,food_name,members_selected,beverages,glasses_selected,adjustments,salad,soup,pickle,soda) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
##        val=(e3.get(),'LAMB MEAT',k1.get(),a.get(),u.get(),r.get(),s.get(),w.get(),x.get(),z.get())
##        
##    elif e3.get()=='6':
##        query="""insert into software_2(food_code,food_name,members_selected,beverages,glasses_selected,adjustments,salad,soup,pickle,soda) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
##        val=(e3.get(),'MALFO',k1.get(),a.get(),u.get(),r.get(),s.get(),w.get(),x.get(),z.get())
##        
##    elif e3.get()=='7':
##        query="""insert into software_2(food_code,food_name,members_selected,beverages,glasses_selected,adjustments,salad,soup,pickle,soda) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
##        val=(e3.get(),'FISH CURRY',k1.get(),a.get(),u.get(),r.get(),s.get(),w.get(),x.get(),z.get())
##        
##    elif e3.get()=='8':
##        query="""insert into software_2(food_code,food_name,members_selected,beverages,glasses_selected,adjustments,salad,soup,pickle,soda) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
##        val=(e3.get(),'OPA',k1.get(),a.get(),u.get(),r.get(),s.get(),w.get(),x.get(),z.get())
##        
##    elif e3.get()=='9':
##        query="""insert into software_2(food_code,food_name,members_selected,beverages,glasses_selected,adjustments,salad,soup,pickle,soda) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
##        val=(e3.get(),'RISSOTO',k1.get(),a.get(),u.get(),r.get(),s.get(),w.get(),x.get(),z.get())
##        
##    elif e3.get()=='10':
##        query="""insert into software_2(food_code,food_name,members_selected,beverages,glasses_selected,adjustments,salad,soup,pickle,soda) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
##        val=(e3.get(),'RAULADE',k1.get(),a.get(),u.get(),r.get(),s.get(),w.get(),x.get(),z.get())
##        
##    elif e3.get()=='11':
##        query="""insert into software_2(food_code,food_name,members_selected,beverages,glasses_selected,adjustments,salad,soup,pickle,soda) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
##        val=(e3.get(),'FALAFEL',k1.get(),a.get(),u.get(),r.get(),s.get(),w.get(),x.get(),z.get())
##       
##    elif e3.get()=='12':
##        query="""insert into software_2(food_code,food_name,members_selected,beverages,glasses_selected,adjustments,salad,soup,pickle,soda) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
##        val=(e3.get(),'PANEER PAKODA',k1.get(),a.get(),u.get(),r.get(),s.get(),w.get(),x.get(),z.get())
##        
##    elif e3.get()=='13':
##        query="""insert into software_2(food_code,food_name,members_selected,beverages,glasses_selected,adjustments,salad,soup,pickle,soda) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
##        val=(e3.get(),'SAMOSA',k1.get(),a.get(),u.get(),r.get(),s.get(),w.get(),x.get(),z.get())
##        
##    elif e3.get()=='14':
##        query="""insert into software_2(food_code,food_name,members_selected,beverages,glasses_selected,adjustments,salad,soup,pickle,soda) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
##        val=(e3.get(),'ALOO TIKKI',k1.get(),a.get(),u.get(),r.get(),s.get(),w.get(),x.get(),z.get())
##        
##    elif e3.get()=='15':
##        query="""insert into software_2(food_code,food_name,members_selected,beverages,glasses_selected,adjustments,salad,soup,pickle,soda) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
##        val=(e3.get(),'SNACKS',k1.get(),a.get(),u.get(),r.get(),s.get(),w.get(),x.get(),z.get())
##        
##    elif e3.get()=='16':
##        query="""insert into software_2(food_code,food_name,members_selected,beverages,glasses_selected,adjustments,salad,soup,pickle,soda) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
##        val=(e3.get(),'ITALIAN',k1.get(),a.get(),u.get(),r.get(),s.get(),w.get(),x.get(),z.get())
##        
##    elif e3.get()=='17':
##        query="""insert into software_2(food_code,food_name,members_selected,beverages,glasses_selected,adjustments,salad,soup,pickle,soda) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
##        val=(e3.get(),'PANI PURI',k1.get(),a.get(),u.get(),r.get(),s.get(),w.get(),x.get(),z.get())
##        
##    elif e3.get()=='18':
##        query="""insert into software_2(food_code,food_name,members_selected,beverages,glasses_selected,adjustments,salad,soup,pickle,soda) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
##        val=(e3.get(),'FRENCH FRIES',k1.get(),a.get(),u.get(),r.get(),s.get(),w.get(),x.get(),z.get())
##        
##    elif e3.get()=='19':
##        query="""insert into software_2(food_code,food_name,members_selected,beverages,glasses_selected,adjustments,salad,soup,pickle,soda) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
##        val=(e3.get(),'APPLE JUICE',k1.get(),a.get(),u.get(),r.get(),s.get(),w.get(),x.get(),z.get())
##       
##    elif e3.get()=='20':
##        query="""insert into software_2(food_code,food_name,members_selected,beverages,glasses_selected,adjustments,salad,soup,pickle,soda) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
##        val=(e3.get(),'ORANGE JUICE',k1.get(),a.get(),u.get(),r.get(),s.get(),w.get(),x.get(),z.get())
    query="""insert into software_2(food_code,food_name,members_selected,beverages,glasses_selected,adjustments,salad,soup,pickle,soda) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""    
    val_1=(e3.get(),val[int(e3.get())-1],k1.get(),a.get(),u.get(),r.get(),s.get(),w.get(),x.get(),z.get())
    cursor.execute(query,val_1)
    con.commit()     
    
    scr5.mainloop()

    


    
def card():
    global scr4
    global e8
    global e9
    global e10
    global e11
    global e12
    global e13
    scr4=Toplevel()
    scr4.geometry('600x400')
    scr4.configure(bg='gold')
    my_label50=Label(scr4,text='SPECIFY CARD DETAILS',font=('Western',17),bg='magenta').pack()
    my_label51=Label(scr4,text='ENTER CARD NUMBER::',font=('Western',15),bg='deeppink').place(x=5,y=45)
    e8=Entry(scr4,font=('Western',15))
    e8.place(x=370,y=45)
    e9=Entry(scr4,font=('Western',15),width=4)
    e9.place(x=370,y=110)
    e10=Entry(scr4,font=('Western',15),width=4)
    e10.place(x=470,y=110)
    e11=Entry(scr4,font=('Western',15))
    e11.place(x=370,y=170)
    e12=Entry(scr4,font=('Western',15))
    e12.place(x=370,y=220)
    e13=Entry(scr4,font=('Western',15))
    e13.place(x=370,y=260)
    my_label52=Label(scr4,text='MONTH').place(x=370,y=140)
    my_label53=Label(scr4,text='YEAR').place(x=480,y=140)
    my_label54=Label(scr4,text='ENTER PHONE NUMBER',font=('Western',15),bg='deeppink').place(x=5,y=170)
    my_label55=Label(scr4,text='CARD EXPIRY MONTH AND YEAR',font=('Western',15),bg='deeppink').place(x=5,y=95)
    my_label56=Label(scr4,text='ENTER YOUR ADDRESS',font=('Western',15),bg='pink').place(x=5,y=220)
    my_label57=Label(scr4,text='ENTER NEAR-BY LANDMARK',font=('Western',15),bg='pink').place(x=5,y=260)

    btn1=Button(scr4,text='PAY',font=('Western',20),bg='pink',command=dest1,width=10).place(x=230,y=310)
    scr4.mainloop()

def dest1():
    if e8.get()=='' or e9.get()=='' or e10.get()=='' or e11.get()=='':
        messagebox.showwarning('VARIFICATION','PLEASE FILL THE REQURED FIELD')
    else:
        upi_update_data()
        messagebox.showwarning('VARIFICATION','PAVEMENT DONE SUCESSFULLY')
    
        scr4.destroy()
        final()
    
def upi_update_data():
    if e13.get()=="":
        query="""insert into software_3(card_number,expiry_month,expiry_date,phone_number,address,near_by_landmark) values(%s,%s,%s,%s,%s,%s)"""
        value=(e8.get(),e9.get(),e10.get(),e11.get(),e12.get(),'NO LANDMARK SPECIFIED')
    else:
        query="""insert into software_3(card_number,expiry_month,expiry_date,phone_number,address,near_by_landmark) values(%s,%s,%s,%s,%s,%s)"""
        value=(e8.get(),e9.get(),e10.get(),e11.get(),e12.get(),e13.get())
    cursor.execute(query,value)
    con.commit()
      




    
     
def map1():
    try:
        win=turtle.Screen()
        win.setup(width=800,height=600)
        ##win.bgcolor('cyan')
        win.bgpic(r"c:\gui\map2.gif")
        k=turtle.Turtle()
        k.width(9)
        k.color('red')
        k.penup()
        k.goto(-205,-130)
        k.pendown()
        k.rt(30)
        for i in range(12):
            k.fd(10)
            t.sleep(1)
        k.lt(100)
        for i in range(31):
            k.fd(10)
            t.sleep(1)
        k.fd(8)
    except:
        print('NAMASTE')

def clock():
    hour=t.strftime("%H")
    minute=t.strftime("%M")
    second=t.strftime("%S")

    hour1=t.strftime("%H")
    minute1=t.strftime("%M")
    second1=t.strftime("%S")
    for i in range(20,0,-1):
        my_label100.config(text=str(int(hour)-int(hour1))+':'+str(int(minute)-int(minute1))+':'+str((int(second)+i)-int(second1)))
    my_label100.after(1000,clock)
    

def update_time():
##    return True
    format='%H:%M:%S'
    now=(datetime.now()).strftime(format)
    s2=(datetime.now()).strftime(format)
    string=datetime.strptime(s2,format)
    
    my_label100.Label(text=string)
    
    my_label100.after(1000,update_time)

    

##clock()




   
def cod():
    final()
    

    
def second():
    aug=Toplevel()
    aug.geometry('1500x1500')
    aug.configure(bg='yellow')
    global faf
    faf=260
    img2=ImageTk.PhotoImage(Image.open(r"c:\gui\falafel2.png"))
    my_label2=Label(aug,image=img2)
    global pan
    pan=260
    img3=ImageTk.PhotoImage(Image.open(r"c:\gui\paneer1.png"))
    my_label3=Label(aug,image=img3)
    global sam
    sam=260
    img4=ImageTk.PhotoImage(Image.open(r"c:\gui\samosa1.png"))
    my_label4=Label(aug,image=img4)
    global tki
    tki=260
    img5=ImageTk.PhotoImage(Image.open(r"c:\gui\tkiil2.png"))
    my_label5=Label(aug,image=img5)
    global new
    new=260
    img6=ImageTk.PhotoImage(Image.open(r"c:\gui\new1.png"))
    my_label6=Label(aug,image=img6)
    global ita
    ita=260
    img7=ImageTk.PhotoImage(Image.open(r"c:\gui\italian.png"))
    my_label7=Label(aug,image=img7)
    global pani
    pani=260
    img8=ImageTk.PhotoImage(Image.open(r"c:\gui\pani4.png"))
    my_label8=Label(aug,image=img8)
    global fre
    fre=260
    img9=ImageTk.PhotoImage(Image.open(r"c:\gui\fremch1.png"))
    my_label9=Label(aug,image=img9)
    global app
    app=260
    img10=ImageTk.PhotoImage(Image.open(r"c:\gui\apple1.png"))
    my_label10=Label(aug,image=img10)
    global ora
    ora=260
    img11=ImageTk.PhotoImage(Image.open(r"c:\gui\orange1.png"))
    my_label11=Label(aug,image=img11)
    
##    tn2=Button(aug,text='BACK',command=lambda: aug.destroy())
##    tn5=Button(aug,text='FORWARD',command=third_1)

##    my_label32=Label(aug,text='FALAFEL',bg='cyan').grid(row=1,column=0)
##    my_label33=Label(aug,text='PANEER',bg='cyan').grid(row=1,column=1)
##    my_label34=Label(aug,text='SAMOSA',bg='cyan').grid(row=1,column=2)
##    my_label35=Label(aug,text='ALOO TIKKI',bg='cyan').grid(row=1,column=3)
##    my_label36=Label(aug,text='SNACKS',bg='cyan').grid(row=1,column=4)
##    my_label37=Label(aug,text='ITALIAN',bg='cyan').grid(row=4,column=0)
##    my_label38=Label(aug,text='PANI PURI',bg='cyan').grid(row=4,column=1)
##    my_label39=Label(aug,text='FRENCH FRIES',bg='cyan').grid(row=4,column=2)
##    my_label40=Label(aug,text='APPLE JUICE',bg='cyan').grid(row=4,column=3)
##    my_label41=Label(aug,text='ORANGE JUICE',bg='cyan').grid(row=4,column=4)
##    tn22=Button(aug,text='PROCEED',command=fourth,bg="magenta").grid(row=2,column=0)
##    tn23=Button(aug,text='PROCEED',command=fourth,bg="magenta").grid(row=2,column=1)
##    tn24=Button(aug,text='PROCEED',command=fourth,bg="magenta").grid(row=2,column=2)
##    tn25=Button(aug,text='PROCEED',command=fourth,bg="magenta").grid(row=2,column=3)
##    tn26=Button(aug,text='PROCEED',command=fourth,bg="magenta").grid(row=2,column=4)
##    tn27=Button(aug,text='PROCEED',command=fourth,bg="magenta").grid(row=5,column=0)
##    tn28=Button(aug,text='PROCEED',command=fourth,bg="magenta").grid(row=5,column=1)
##    tn29=Button(aug,text='PROCEED',command=fourth,bg="magenta").grid(row=5,column=2)
##    tn30=Button(aug,text='PROCEED',command=fourth,bg="magenta").grid(row=5,column=3)
##    tn31=Button(aug,text='PROCEED',command=fourth,bg="magenta").grid(row=5,column=4)
    
    my_label22=Label(aug,text='FALAFEL',font=('Western',12),padx=10,pady=10,bg="magenta")
    my_label23=Label(aug,text='PANEER PAKODA',font=('Western',12),padx=10,pady=10,bg="indigo")
    my_label24=Label(aug,text='SAMOSA',font=('Western',12),padx=10,pady=10,bg="cyan")
    my_label25=Label(aug,text='ALOO TKIKKI',font=('Western',12),padx=10,pady=10,bg="red")
    my_label26=Label(aug,text='SNACKS',font=('Western',12),padx=10,pady=10,bg="green")
    my_label27=Label(aug,text='ITALIAN',font=('Western',12),padx=10,pady=10,bg="gold")
    my_label28=Label(aug,text='PANI PURI',font=('Western',12),padx=10,pady=10,bg="navy")
    my_label29=Label(aug,text='FRENCH FRIES',font=('Western',12),padx=10,pady=10,bg="lime")
    my_label30=Label(aug,text='APPLE JUICE',font=('Western',12),padx=10,pady=10,bg="lemonchiffon")
    my_label31=Label(aug,text='ORANGE JUICE',font=('Western',12),padx=10,pady=10,bg="orange")

    my_label22.grid(row=1,column=0)
    my_label23.grid(row=1,column=1)
    my_label24.grid(row=1,column=2)
    my_label25.grid(row=1,column=3)
    my_label26.grid(row=1,column=4)
    my_label27.grid(row=4,column=0)
    my_label28.grid(row=4,column=1)
    my_label29.grid(row=4,column=2)
    my_label30.grid(row=4,column=3)
    my_label31.grid(row=4,column=4)

    Label(aug,text='160/-',font=('Times',15),padx=5,pady=5).place(x=205,y=255)
    Label(aug,text='260/-',font=('Times',15),padx=5,pady=5).place(x=505,y=255)
    Label(aug,text='240/-',font=('Times',15),padx=5,pady=5).place(x=775,y=255)
    Label(aug,text='360/-',font=('Times',15),padx=5,pady=5).place(x=1035,y=255)
    Label(aug,text='100/-',font=('Times',15),padx=5,pady=5).place(x=1285,y=255)
    Label(aug,text='11',font=('Times',15),padx=5,pady=5).place(x=205,y=295)
    Label(aug,text='12',font=('Times',15),padx=5,pady=5).place(x=505,y=295)
    Label(aug,text='13',font=('Times',15),padx=5,pady=5).place(x=775,y=295)
    Label(aug,text='14',font=('Times',15),padx=5,pady=5).place(x=1035,y=295)
    Label(aug,text='15',font=('Times',15),padx=5,pady=5).place(x=1285,y=295)

    Label(aug,text='560/-',font=('Times',15),padx=5,pady=5).place(x=185,y=600)
    Label(aug,text='764/-',font=('Times',15),padx=5,pady=5).place(x=505,y=600)
    Label(aug,text='523/-',font=('Times',15),padx=5,pady=5).place(x=790,y=600)
    Label(aug,text='934/-',font=('Times',15),padx=5,pady=5).place(x=1040,y=600)
    Label(aug,text='342/-',font=('Times',15),padx=5,pady=5).place(x=1295,y=600)
    Label(aug,text='16',font=('Times',15),padx=5,pady=5).place(x=185,y=640)
    Label(aug,text='17',font=('Times',15),padx=5,pady=5).place(x=505,y=640)
    Label(aug,text='18',font=('Times',15),padx=5,pady=5).place(x=790,y=640)
    Label(aug,text='19',font=('Times',15),padx=5,pady=5).place(x=1040,y=640)
    Label(aug,text='20',font=('Times',15),padx=5,pady=5).place(x=1295,y=640)

    tn12=Button(aug,text='PROCEED',bg='cyan',command=chole_1)
    tn13=Button(aug,text='PROCEED',bg='cyan',command=chole_1)
    tn14=Button(aug,text='PROCEED',bg='cyan',command=chole_1)
    tn15=Button(aug,text='PROCEED',bg='cyan',command=chole_1)
    tn16=Button(aug,text='PROCEED',bg='cyan',command=chole_1)
    tn17=Button(aug,text='PROCEED',bg='cyan',command=chole_1)
    tn18=Button(aug,text='PROCEED',bg='cyan',command=chole_1)
    tn19=Button(aug,text='PROCEED',bg='cyan',command=chole_1)
    tn20=Button(aug,text='PROCEED',bg='cyan',command=chole_1)
    tn21=Button(aug,text='PROCEED',bg='cyan',command=chole_1)

    tn12.grid(row=2,column=0,padx=10,pady=10)
    tn13.grid(row=2,column=1)
    tn14.grid(row=2,column=2)
    tn15.grid(row=2,column=3)
    tn16.grid(row=2,column=4)
    tn17.grid(row=5,column=0,padx=10,pady=10)
    tn18.grid(row=5,column=1)
    tn19.grid(row=5,column=2)
    tn20.grid(row=5,column=3)
    tn21.grid(row=5,column=4)

    
## for images
    my_label2.grid(row=0,column=0)
    my_label3.grid(row=0,column=1)
    my_label4.grid(row=0,column=2)
    my_label5.grid(row=0,column=3)
    my_label6.grid(row=0,column=4)
    my_label7.grid(row=3,column=0)
    my_label8.grid(row=3,column=1)
    my_label9.grid(row=3,column=2)
    my_label10.grid(row=3,column=3)
    my_label11.grid(row=3,column=4)

    
##    tn5.grid(row=6,column=0)
##    tn2.grid(row=6,column=1)
    
    aug.mainloop()

##def fourth():
##    sep=Toplevel()
##    sep.geometry('500x500')
##    sep.configure(bg='gold')
##    tn7=Button(sep,text='BACK',command=lambda: sep.destroy())
##    tn7.pack()
##    sep.mainloop()
    
def first():
    top=Toplevel(root)
    top.geometry('1500x1500')
    top.configure(bg='magenta')
    l1=Label(top,text=r"KRITIKA's CAFE",bg="lavender",padx=10,pady=10,font=('Times',20))
##    l2=Label(top,pady=20)
##    l2.configure(bg='magenta')
##    top.configure(bg='magenta')
    img1=ImageTk.PhotoImage(Image.open(r"c:\gui\bg3.png"))
    my_label1=Label(top,image=img1)
    
    tn1=Button(top,text='BACK',command=lambda: top.destroy(),font=('Times',20),bg='lime')
    tn3=Button(top,text='PROCEED TO STARTER',command=second,font=('Times',20),bg='lime')
    tn10=Button(top,text='PROCEED TO MAIN MENU',command=fifth,font=('Times',20),bg='lime')
    tn11=Button(top,text='PLAY SONGS',command=play,font=('Times',20),bg='lime')
    l1.pack()
    my_label1.pack()
    
##    l2.grid(row=2,column=0)
    tn1.place(x=600,y=650)
    tn3.place(x=200,y=550)
    tn10.place(x=800,y=550)
    tn11.place(x=600,y=650)
    top.mainloop()

def rate():
    global scr6
    scr6=Toplevel()
    scr6.geometry('400x270')
    scr6.configure(bg='magenta')
    global a1
    a1=IntVar()
##    a1.set(2)
    Radiobutton(scr6,text='1',variable=a1,value=1,font=('Times',12),bg='red',padx=10,pady=10).place(x=50,y=150)
    Radiobutton(scr6,text='2',variable=a1,value=2,font=('Times',12),bg='tomato',padx=10,pady=10).place(x=110,y=150)
    Radiobutton(scr6,text='3',variable=a1,value=3,font=('Times',12),bg='gold',padx=10,pady=10).place(x=170,y=150)
    Radiobutton(scr6,text='4',variable=a1,value=4,font=('Times',12),bg='greenyellow',padx=10,pady=10).place(x=230,y=150)
    Radiobutton(scr6,text='5',variable=a1,value=5,font=('Times',12),bg='lime',padx=10,pady=10).place(x=290,y=150)
##    Radiobutton(root,text='2',variable=a1,value=2,font=('Times',12),padx=10,pady=10).place(x=200,y=150)
    btn=Button(scr6,text='PROCEED',bg='cyan',command=step,font=('Helvatica',15),padx=10,pady=10).place(x=150,y=200)
##    img=ImageTk.PhotoImage(Image.open(r"c:\gui\01.png"))
##    my_label=Label(root,image=img)
##    my_label.place(x=50,y=35)
##    img=ImageTk.PhotoImage(Image.open(r"c:\gui_2\01.png"))
##    my_label=Label(image=img)
##    my_label.pack()
##    img=ImageTk.PhotoImage(Image.open(r"c:\gui\01.png"))
##    my_label=Label(scr6,image=img)
##    my_label.place(x=150,y=200)
    img1=ImageTk.PhotoImage(Image.open(r"c:\gui\02.png"))
    my_label1=Label(scr6,image=img1)
    my_label1.place(x=50,y=80)
    img2=ImageTk.PhotoImage(Image.open(r"c:\gui\03.png"))
    my_label2=Label(scr6,image=img2)
    my_label2.place(x=110,y=80)
    img3=ImageTk.PhotoImage(Image.open(r"c:\gui\02.png"))
    my_label3=Label(scr6,image=img3)
    my_label3.place(x=160,y=80)
    img4=ImageTk.PhotoImage(Image.open(r"c:\gui\03.png"))
    my_label4=Label(scr6,image=img4)
    my_label4.place(x=220,y=80)
    img5=ImageTk.PhotoImage(Image.open(r"c:\gui\02.png"))
    my_label5=Label(scr6,image=img5)
    my_label5.place(x=280,y=80)
    scr6.mainloop()


def play_gif():
    global gf1
    if a1.get()==1:
        gf1=Image.open(r"c:\gui\emj8.gif")
    elif a1.get()==2:
        gf1=Image.open(r"c:\gui\emj9.gif")
    elif a1.get()==3:
        gf1=Image.open(r"c:\gui\emj10.gif")
    elif a1.get()==4:
        gf1=Image.open(r"c:\gui\emj11.gif")
    else:
        gf1=Image.open(r"c:\gui\emj12.gif")
    
    lbl_1=Label(sep)
    lbl_1.place(x=140,y=0)

    if a1.get()==2 or a1.get()==4:

        for gf1 in ImageSequence.Iterator(gf1):
            gf1=gf1.resize((200,200))
            gf1=ImageTk.PhotoImage(gf1)
            lbl_1.config(image=gf1)
            sep.update()
            t.sleep(0.1)
        sep.after(0,play_gif)
    else:
        for gf1 in ImageSequence.Iterator(gf1):
            gf1=gf1.resize((200,200))
            gf1=ImageTk.PhotoImage(gf1)
            lbl_1.config(image=gf1)
            sep.update()
            t.sleep(0.01)
        sep.after(0,play_gif)
        
def step():
    global sep
    global e_feed
    sep=Toplevel()
    sep.geometry('500x500')
    sep.configure(bg='gold')
    
    play_gif()
    
    lbl=Label(sep,text="THANK YOU FOR YOUR FUCKI'N FEEDBACK",bg='gold',font=('Helvatica',20)).place(x=0,y=210)
    lbl1=Label(sep,text="IF YOU HAVE ANY QUERY RELATED TO OUR SOFTWARE JUST GO AND FUCK OFF",bg='gold',font=('Helvatica',20)).place(x=0,y=240)
    lbl2=Label(sep,text="I'M NOT HERE TO RESOLVE YOUR SHITTY DOUBT",bg='gold',font=('Helvatica',20)).place(x=0,y=270)
    lbl3=Label(sep,text="OR ELSE YOUR TYPE YOUR FUCKI'N WORDS IN THE BOX",bg='gold',font=('Helvatica',20)).place(x=0,y=300)
    lbl4=Label(sep,text="REGARDS KUSH AND KRITIKA",bg='red',font=('Mistral',20)).place(x=0,y=330)
    e_feed=Entry(sep,width=100,font=('Helvatia',15))
    e_feed.place(x=0,y=360)
    btn=Button(sep,text='DONE',font=('Times',30),bg='cyan',command=kush_2).place(x=200,y=400)
    
def kush_2():
    hour=t.strftime("%H")
    minute=t.strftime("%M")
    second=t.strftime("%S")
    time=hour+':'+minute+':'+second
    if e_feed.get()=="":
        query_2="""insert into software_4(rating,review,used_at_time) values(%s,%s,%s)"""
        val_2=(a1.get(),'NO FEEDBACK GIVEN',time)
    else:
        query_2="""insert into software_4(rating,review,used_at_time) values(%s,%s,%s)"""
        val_2=(a1.get(),e_feed.get(),time)
    cursor.execute(query_2,val_2)
    con.commit()
        
    messagebox.showwarning('RATING','APP RATED SUCCESSFULLY')
    messagebox.showwarning('RATING','THANK YOU FOR YOUR FEEDBACK')
    sep.destroy()
##    scr6.destroy()
    

    
def play():
    pygame.mixer.music.load(r"c:\gui\song1.mp3")
    pygame.mixer.music.play(loops=0)

def tatti():
    kri=turtle.Screen()
    kri.setup(width=700,height=500)
    a=turtle.Turtle()
##    das.penup()
##    das.goto(1000,1000)
##    das.pendown()
    turtle.color('deep pink')
    style=('Courier',50,'italic')
    style_1=('Courier',20,'italic') 
    for i in range(5,0,-1):
        turtle.write(i,font=style,align='center')
        t.sleep(1)
        turtle.clear()
##    a.bk(100)
##    a.fd(200)
##    a.lt(90)
##    a.fd(40)
##    a.lt(90)
##    a.fd(200)
##    a.lt(90)
##    a.fd(40)
##    a.lt(90)
##    a.penup()
##    a.goto(-90,10)
##    a.pendown()
##    a.fd(180)
##    a.lt(90)
##    a.fd(20)
##    a.lt(90)
##    a.fd(180)
##    a.lt(90)
##    a.fd(20)
##    t.sleep(90)
    
    turtle.write("WELCOME TO MY FUCKI'N SOFTWARE",font=style,align='center')
    t.sleep(5)
    turtle.clear()
##    turtle.write('THIS SOFTWARE IS CREATED BY Mrs. KRITIKA DAS AND Mr. KUSHAGRA SINGH AS A TERM 2 ANNUAL SYNOPSIS',font=style_1,align='center')
##    t.sleep(50)
    turtle.bye()
##tatti()
##t.sleep(1)
kush()
##root.mainloop()

##################                  SIZE::                                62.6 KB (64,104 bytes)
##################                  SIZE ON DISK::                  64.0 KB (65,536 bytes)

