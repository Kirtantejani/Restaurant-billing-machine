#Import required module
from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
import random
import time

a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#creating Indian Food Page
def Indian_Food():
    root=Toplevel()
    root.geometry("1600x1300+0+0")
    def undiyupuri():
        global a
        a=a+1
    def uttapam():
        global b
        b=b+1
    def idli():
        global c
        c+=1
    def vej():
        global d
        d+=1
    def rice():
        global e
        e+=1
    def gulab():
        global f
        f+=1
    def kaju():
        global g
        g+=1
    def jalebi():
        global h
        h+=1
    def rasgulla():
        global i
        i+=1
    def ladoo():
        global j
        j+=1
    def chai():
        global k
        k+=1
    def kesar():
        global l
        l+=1
    def lassi():
        global m
        m+=1
    def chass():
        global n
        n+=1
    def toddy():
        global o
        o+=1
    def coca():
        global p
        p+=1
    def pepsi():
        global q
        q+=1
    def thumbs():
        global r
        r+=1
    def sprite():
        global s
        s+=1
    def maza():
        global t
        t+=1

    def receipt():
        global TotalBill    
        textreceipt.delete(1.0,END)
        x=random.randint(100,10000)
        billnumber='BILL'+str(x)
        date=time.strftime('%d/%m/%Y')
        textreceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t\t'+date+'\n')
        txtName=text.get()
        textreceipt.insert(END,f'Customer Name:\t{txtName}\n')
        textreceipt.insert(END,'==================================================\n')
        textreceipt.insert(END,f'Items\t\t\tQnt.\t\t\tPrice\n')
        if a>0:
            textreceipt.insert(END,f'Undiyu Puri\t\t\t{a}\t\t\t{a*100}\n')
        if b>0:
            textreceipt.insert(END,f'Uttapam\t\t\t{b}\t\t\t{b*70}\n')
        if c>0:
            textreceipt.insert(END,f'Idli Samber\t\t\t{c}\t\t\t{c*50}\n')
        if d>0:
            textreceipt.insert(END,f'Vej Biryani\t\t\t{d}\t\t\t{d*110}\n')
        if e>0:
            textreceipt.insert(END,f'Dal And Rice\t\t\t{e}\t\t\t{e*110}\n')
        if f>0:
            textreceipt.insert(END,f'Gulab Jamun\t\t\t{f}\t\t\t{f*30}\n')
        if g>0:
            textreceipt.insert(END,f'Kaju Katari\t\t\t{g}\t\t\t{g*50}\n')
        if h>0:
            textreceipt.insert(END,f'Jalebi\t\t\t{h}\t\t\t{h*50}\n')
        if i>0:
            textreceipt.insert(END,f'Rasgulla\t\t\t{i}\t\t\t{i*50}\n')
        if j>0:
            textreceipt.insert(END,f'Ladoo\t\t\t{j}\t\t\t{j*40}\n')
        if k>0:
            textreceipt.insert(END,f'Chai\t\t\t{k}\t\t\t{k*30}\n')
        if l>0:
            textreceipt.insert(END,f'Kesar Dudh\t\t\t{l}\t\t\t{l*60}\n')
        if m>0:
            textreceipt.insert(END,f'Lassi\t\t\t{m}\t\t\t{m*40}\n')
        if n>0:
            textreceipt.insert(END,f'Masala Chass\t\t\t{n}\t\t\t{n*30}\n')
        if o>0:
            textreceipt.insert(END,f'Toddy\t\t\t{o}\t\t\t{o*50}\n')
        if p>0:
            textreceipt.insert(END,f'Coca-Cola\t\t\t{p}\t\t\t{p*20}\n')
        if q>0:
            textreceipt.insert(END,f'Pepsi\t\t\t{q}\t\t\t{q*20}\n')
        if r>0:
            textreceipt.insert(END,f'Thumbs Up\t\t\t{r}\t\t\t{r*20}\n')
        if s>0:
            textreceipt.insert(END,f'Sprite\t\t\t{s}\t\t\t{s*20}\n')
        if t>0:
            textreceipt.insert(END,f'Maza\t\t\t{t}\t\t\t{t*20}\n')



    def total():
        receipt()
        TotalBill=(a*100)+(b*70)+(c*50)+(d*110)+(e*50)+(f*30)+(g*50)+(h*50)+(i*50)+(j*40)+(k*30)+(l*60)+(m*40)+(n*30)+(o*50)+(p*20)+(q*20)+(r*20)+(s*20)+(t*20)
        if TotalBill>0:
            textreceipt.insert(END,'==================================================\n')
            textreceipt.insert(END,f'TotalBill:\t\t\t\t\t\t{TotalBill}')

    def reset():
        global a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t
        a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
        textreceipt.delete(1.0,END)

    def send():
        top=Toplevel()
        top.geometry("250x200+600+300")
        top.title("Send Receipt")
        label=Label(top,text="Your Bill Sent Successful",compound='center',bg="#15133C",fg="#00FFAB")
        label.pack(pady=50)
        textreceipt.delete(1.0,END)
        global a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t
        a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
        top.mainloop()

    def back():
        root.destroy()
        global a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t
        a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

    #Background image and head
    filename=Image.open("D:\\Project\\photos\\Indian food\\background.jpg")
    filename=ImageTk.PhotoImage(filename.resize((1700,800)))
    l1=Label(root,image=filename)
    l1.place(x=0,y=0)
    root.title("Bill Machine")

    #frame head 1
    f1=Frame(root,bd=5,relief=GROOVE)
    f1.pack(side=TOP)

    #Frame head 2
    f2=Frame(root,bd=5,relief=GROOVE)
    f2.pack()

    #First head
    bill=Label(f1,text="Billing Machine",fg="#FF7F3F",bg="#FDD998",width=1300,font=("Times new roman",27,"bold"),compound='center')
    bill.pack()

    #Second Head
    indian_food=Label(f2,text="Indian Food",fg="#FF7F3F",bg="#FDD998",width=1300,font=("Times new roman",27,"bold"),compound='center')
    indian_food.pack()

    #text in frame 3 and create
    f3=LabelFrame(root,text="Food",font=("Times new roman",25,"bold"),bg="#FDD998",fg="#FF7F3F")
    f3.pack(side=LEFT,padx=5)

    #first image
    image1=Image.open("D:\\Project\\photos\\Indian food\\undhiyu.jfif")
    resize_image1=ImageTk.PhotoImage(image1.resize((115,65)))
    label_image1=Label(f3,image=resize_image1)
    label_image1.pack(ipady=5)

    #First image text 1
    label_text1=Label(f3,text="Undhiyu Puri",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text1.pack()

    #Creating Button 1
    button1=Button(f3,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=undiyupuri)
    button1.pack(pady=2)

    #second image
    image2=Image.open("D:\\Project\\photos\\Indian food\\uttapam.jfif")
    resize_image2=ImageTk.PhotoImage(image2.resize((115,65)))
    label_image2=Label(f3,image=resize_image2)
    label_image2.pack(ipady=5)

    #Second image text 2
    label_text2=Label(f3,text="Uttapam",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text2.pack()

    #Creating Button 2
    button2=Button(f3,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=uttapam)
    button2.pack(pady=2)

    #third image 
    image3=Image.open("D:\\Project\\photos\\Indian food\\idli-sambar.jpg")
    resize_image3=ImageTk.PhotoImage(image3.resize((115,65)))
    label_image3=Label(f3,image=resize_image3)
    label_image3.pack(ipady=5)

    #Third image text 3
    label_text3=Label(f3,text="Idli Samber",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text3.pack()

    #Creating Button 3
    button3=Button(f3,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=idli)
    button3.pack(pady=2)

    #four image 
    image4=Image.open("D:\\Project\\photos\\Indian food\\vej biryani.jpg")
    resize_image4=ImageTk.PhotoImage(image4.resize((115,65)))
    label_image4=Label(f3,image=resize_image4)
    label_image4.pack(ipady=5)

    #Third image text 4
    label_text4=Label(f3,text="Vej Biryani",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text4.pack()

    #Creating Button 4
    button4=Button(f3,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=vej)
    button4.pack(pady=2)

    #five image 
    image5=Image.open("D:\\Project\\photos\\Indian food\\rice and dal.jfif")
    resize_image5=ImageTk.PhotoImage(image5.resize((115,65)))
    label_image5=Label(f3,image=resize_image5)
    label_image5.pack(ipady=5)

    #Third image text 5
    label_text5=Label(f3,text="Rice and Dal",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text5.pack()

    #Creating Button 5
    button5=Button(f3,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=rice)
    button5.pack(pady=2)



    #text and Frame creating 4
    sweet=LabelFrame(root,text="Sweet",font=("Times new roman",25,"bold"),bg="#FDD998",fg="#FF7F3F")
    sweet.pack(side=LEFT,padx=5)

    #first image in sweet
    sweet_image1=Image.open("D:\\Project\\photos\\Indian food\\gulabjamun.jfif")
    sweet_resize_image1=ImageTk.PhotoImage(sweet_image1.resize((115,65)))
    sweet_label_image1=Label(sweet,image=sweet_resize_image1)
    sweet_label_image1.pack(ipady=5)

     #First image text 1 of sweet
    label_text6=Label(sweet,text="Gulab Jamun",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text6.pack()

    #Creating Button 1 of sweet
    button6=Button(sweet,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=gulab)
    button6.pack(pady=2)

    #second image in sweet
    sweet_image2=Image.open("D:\\Project\\photos\\Indian food\\kajukatari.jfif")
    sweet_resize_image2=ImageTk.PhotoImage(sweet_image2.resize((115,65)))
    sweet_label_image2=Label(sweet,image=sweet_resize_image2)
    sweet_label_image2.pack(ipady=5)

     #second image text of sweet
    label_text7=Label(sweet,text="Kaju Katari",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text7.pack()

    #Creating Button 2 of sweet
    button7=Button(sweet,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=kaju)
    button7.pack(pady=2)

    #third image in sweet
    sweet_image3=Image.open("D:\\Project\\photos\\Indian food\\jalebi.jfif")
    sweet_resize_image3=ImageTk.PhotoImage(sweet_image3.resize((115,65)))
    sweet_label_image3=Label(sweet,image=sweet_resize_image3)
    sweet_label_image3.pack(ipady=5)

     #third image text 1 of sweet
    label_text8=Label(sweet,text="Jalebi",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text8.pack()

    #Creating Button 3 of sweet
    button8=Button(sweet,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=jalebi)
    button8.pack(pady=2)

    #fourth image in sweet
    sweet_image4=Image.open("D:\\Project\\photos\\Indian food\\rasgulla.jfif")
    sweet_resize_image4=ImageTk.PhotoImage(sweet_image4.resize((115,65)))
    sweet_label_image4=Label(sweet,image=sweet_resize_image4)
    sweet_label_image4.pack(ipady=5)

     #Fourth image text 1 of sweet
    label_text9=Label(sweet,text="Rasgulla",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text9.pack()

    #Creating Button 4 of sweet
    button9=Button(sweet,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=rasgulla)
    button9.pack(pady=2)

    #fifth image in sweet
    sweet_image5=Image.open("D:\\Project\\photos\\Indian food\\ladoo.jfif")
    sweet_resize_image5=ImageTk.PhotoImage(sweet_image5.resize((115,65)))
    sweet_label_image5=Label(sweet,image=sweet_resize_image5 )
    sweet_label_image5.pack(ipady=5)

     #Fifth image text 1 of sweet
    label_text10=Label(sweet,text="Ladoo",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text10.pack()

    #Creating Button 5 of sweet
    button10=Button(sweet,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=ladoo)
    button10.pack(pady=2)


    #text and Frame creating 4
    drink=LabelFrame(root,text="Drink",font=("Times new roman",25,"bold"),bg="#FDD998",fg="#FF7F3F")
    drink.pack(side=LEFT,padx=5)

    #first image in drink
    drink_image1=Image.open("D:\\Project\\photos\\Indian food\\Chai.jfif")
    drink_resize_image1=ImageTk.PhotoImage(drink_image1.resize((115,65)))
    drink_label_image1=Label(drink,image=drink_resize_image1)
    drink_label_image1.pack(ipady=5)

     #First image text 1 of drink
    label_text11=Label(drink,text="Chai",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text11.pack()

    #Creating Button 1 of drink
    button11=Button(drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=chai)
    button11.pack(pady=2)

    #second image in drink
    drink_image2=Image.open("D:\\Project\\photos\\Indian food\\kesar dudh.jfif")
    drink_resize_image2=ImageTk.PhotoImage(drink_image2.resize((115,65)))
    drink_label_image2=Label(drink,image=drink_resize_image2)
    drink_label_image2.pack(ipady=5)

     #second image text of drink
    label_text12=Label(drink,text="Kesar Dudh",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text12.pack()

    #Creating Button 2 of drink
    button12=Button(drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=kesar)
    button12.pack(pady=2)

    #third image in drink
    drink_image3=Image.open("D:\\Project\\photos\\Indian food\\lassi.jfif")
    drink_resize_image3=ImageTk.PhotoImage(drink_image3.resize((115,65)))
    drink_label_image3=Label(drink,image=drink_resize_image3)
    drink_label_image3.pack(ipady=5)

     #third image text 1 of drink
    label_text13=Label(drink,text="Lassi",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text13.pack()

    #Creating Button 3 of drink
    button13=Button(drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=lassi)
    button13.pack(pady=2)

    #fourth image in drink
    drink_image4=Image.open("D:\\Project\\photos\\Indian food\\Chhash.jfif")
    drink_resize_image4=ImageTk.PhotoImage(drink_image4.resize((115,65)))
    drink_label_image4=Label(drink,image=drink_resize_image4)
    drink_label_image4.pack(ipady=5)

     #Fourth image text 1 of drink
    label_text14=Label(drink,text="Masala Chaas",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text14.pack()

    #Creating Button 4 of drink
    button14=Button(drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=chass)
    button14.pack(pady=2)

    #fifth image in drink
    drink_image5=Image.open("D:\\Project\\photos\\Indian food\\toddy.jfif")
    drink_resize_image5=ImageTk.PhotoImage(drink_image5.resize((115,65)))
    drink_label_image5=Label(drink,image=drink_resize_image5 )
    drink_label_image5.pack(ipady=5)

     #Fifth image text 1 of drink
    label_text15=Label(drink,text="Toddy",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text15.pack()

    #Creating Button 5 of drink
    button15=Button(drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=toddy)
    button15.pack(pady=2)

    #text and Frame creating 5
    soft_drink=LabelFrame(root,text="Soft Drink",font=("Times new roman",25,"bold"),bg="#FDD998",fg="#FF7F3F")
    soft_drink.pack(side=LEFT,padx=5)

    #first image in soft drink
    soft_drink_image1=Image.open("D:\\Project\\photos\\Indian food\\cocacola.jfif")
    soft_drink_resize_image1=ImageTk.PhotoImage(soft_drink_image1.resize((115,65)))
    soft_drink_label_image1=Label(soft_drink,image=soft_drink_resize_image1)
    soft_drink_label_image1.pack(ipady=5)

     #First image text 1 of soft drink
    label_text16=Label(soft_drink,text="Coca-Cola",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text16.pack()

    #Creating Button 1 of soft drink
    button16=Button(soft_drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=coca)
    button16.pack(pady=2)

    #second image in soft drink
    soft_drink_image2=Image.open("D:\\Project\\photos\\Indian food\\pepsi.jfif")
    soft_drink_resize_image2=ImageTk.PhotoImage(soft_drink_image2.resize((115,65)))
    soft_drink_label_image2=Label(soft_drink,image=soft_drink_resize_image2)
    soft_drink_label_image2.pack(ipady=5)

     #second image text of soft drink
    label_text17=Label(soft_drink,text="Pepsi",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text17.pack()

    #Creating Button 2 of soft drink
    button17=Button(soft_drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=pepsi)
    button17.pack(pady=2)

    #third image in soft drink
    soft_drink_image3=Image.open("D:\\Project\\photos\\Indian food\\thumbsup.jfif")
    soft_drink_resize_image3=ImageTk.PhotoImage(soft_drink_image3.resize((115,65)))
    soft_drink_label_image3=Label(soft_drink,image=soft_drink_resize_image3)
    soft_drink_label_image3.pack(ipady=5)

     #third image text 1 of soft drink
    label_text18=Label(soft_drink,text="Thumbs Up",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text18.pack()

    #Creating Button 3 of soft drink
    button18=Button(soft_drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=thumbs)
    button18.pack(pady=2)

    #fourth image in soft drink
    soft_drink_image4=Image.open("D:\\Project\\photos\\Indian food\\sprite.jfif")
    soft_drink_resize_image4=ImageTk.PhotoImage(soft_drink_image4.resize((115,65)))
    soft_drink_label_image4=Label(soft_drink,image=soft_drink_resize_image4)
    soft_drink_label_image4.pack(ipady=5)

     #Fourth image text 1 of soft drink
    label_text19=Label(soft_drink,text="Sprite",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text19.pack()

    #Creating Button 4 of soft drink
    button19=Button(soft_drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=sprite)
    button19.pack(pady=2)

    #fifth image in soft drink
    soft_drink_image5=Image.open("D:\\Project\\photos\\Indian food\\maza.jfif")
    soft_drink_resize_image5=ImageTk.PhotoImage(soft_drink_image5.resize((115,65)))
    soft_drink_label_image5=Label(soft_drink,image=soft_drink_resize_image5 )
    soft_drink_label_image5.pack(ipady=5)

     #Fifth image text 1 of soft drink
    label_text20=Label(soft_drink,text="Maza",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text20.pack()

    #Creating Button 5 of soft drink
    button20=Button(soft_drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=maza)
    button20.pack(pady=2)

    #creating frame 5
    billframe=LabelFrame(root,text="Receipt",font=("Times new roman",25,"bold"),bg="#FDD998",fg="#FF7F3F")
    billframe.pack(side=LEFT,padx=7)

    #adding text area
    textreceipt=Text(billframe,font=("Times new roman",12,"bold"),bg="white",height=30)
    textreceipt.pack()

    #creating button
    button21=Button(billframe,text="Total",bg="#FDD998",fg="#FF7F3F",font=("Times new roman",15,"bold"),compound='center',command=total)
    button21.pack(side=LEFT,padx=13,pady=5)

    button22=Button(billframe,text="Receipt",bg="#FDD998",fg="#FF7F3F",font=("Times new roman",15,"bold"),compound='center',command=receipt)
    button22.pack(side=LEFT,padx=13)

    button23=Button(billframe,text="Reset",bg="#FDD998",fg="#FF7F3F",font=("Times new roman",15,"bold"),compound='center',command=reset)
    button23.pack(side=LEFT,padx=13)

    button24=Button(billframe,text="Send",bg="#FDD998",fg="#FF7F3F",font=("Times new roman",15,"bold"),compound='center',command=send)
    button24.pack(side=LEFT,padx=13)

    button25=Button(billframe,text="Back",bg="#FDD998",fg="#FF7F3F",font=("Times new roman",15,"bold"),compound='center',command=back)
    button25.pack(side=LEFT,padx=13)

    

    #Indian Food Page Mainloop
    root.mainloop()  

def Chinese_Food():
    root=Toplevel()
    root.geometry("1600x1300+0+0")
    def dim():
        global a
        a=a+1
    def quick():
        global b
        b=b+1
    def szechwan():
        global c
        c+=1
    def springroll():
        global d
        d+=1
    def rice():
        global e
        e+=1
    def red():
        global f
        f+=1
    def egg():
        global g
        g+=1
    def tanghulu():
        global h
        h+=1
    def pancake():
        global i
        i+=1
    def fried():
        global j
        j+=1
    def Tieguanyin():
        global k
        k+=1
    def Jiuniang():
        global l
        l+=1
    def pearl():
        global m
        m+=1
    def greentea():
        global n
        n+=1
    def soybean():
        global o
        o+=1
    def coca():
        global p
        p+=1
    def pepsi():
        global q
        q+=1
    def thumbs():
        global r
        r+=1
    def sprite():
        global s
        s+=1
    def maza():
        global t
        t+=1

    def receipt():
        global TotalBill
        textreceipt.delete(1.0,END)
        x=random.randint(100,10000)
        billnumber='BILL'+str(x)
        date=time.strftime('%d/%m/%Y')
        textreceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t\t'+date+'\n')
        txtName=text.get()
        textreceipt.insert(END,f'Customer Name:\t{txtName}\n')
        textreceipt.insert(END,'==================================================\n')
        textreceipt.insert(END,f'Items\t\t\tQnt.\t\t\tPrice\n')
        if a>0:
            textreceipt.insert(END,f'Dim Sums\t\t\t{a}\t\t\t{a*450}\n')
        if b>0:
            textreceipt.insert(END,f'Quick Noodles\t\t\t{b}\t\t\t{b*50}\n')
        if c>0:
            textreceipt.insert(END,f'Szechwan Chilli Chicken\t\t\t{c}\t\t\t{c*160}\n')
        if d>0:
            textreceipt.insert(END,f'Spring Rolls\t\t\t{d}\t\t\t{d*40}\n')
        if e>0:
            textreceipt.insert(END,f'Stir Fried Tofu with Rice\t\t\t{e}\t\t\t{e*120}\n')
        if f>0:
            textreceipt.insert(END,f'Red Been Bun\t\t\t{f}\t\t\t{f*250}\n')
        if g>0:
            textreceipt.insert(END,f'Egg Tarts\t\t\t{g}\t\t\t{g*200}\n')
        if h>0:
            textreceipt.insert(END,f'Tanghulu\t\t\t{h}\t\t\t{h*100}\n')
        if i>0:
            textreceipt.insert(END,f'Pumpkin pancakes\t\t\t{i}\t\t\t{i*180}\n')
        if j>0:
            textreceipt.insert(END,f'Fried Durian\t\t\t{j}\t\t\t{j*180}\n')
        if k>0:
            textreceipt.insert(END,f'Tieguanyin\t\t\t{k}\t\t\t{k*70}\n')
        if l>0:
            textreceipt.insert(END,f'Jiuniang\t\t\t{l}\t\t\t{l*120}\n')
        if m>0:
            textreceipt.insert(END,f'Pearl milk tea\t\t\t{m}\t\t\t{m*80}\n')
        if n>0:
            textreceipt.insert(END,f'Chivas mixed with green tea\t\t\t{n}\t\t\t{n*60}\n')
        if o>0:
            textreceipt.insert(END,f'Soybean milk\t\t\t{o}\t\t\t{o*50}\n')
        if p>0:
            textreceipt.insert(END,f'Coca-Cola\t\t\t{p}\t\t\t{p*20}\n')
        if q>0:
            textreceipt.insert(END,f'Pepsi\t\t\t{q}\t\t\t{q*20}\n')
        if r>0:
            textreceipt.insert(END,f'Thumbs Up\t\t\t{r}\t\t\t{r*20}\n')
        if s>0:
            textreceipt.insert(END,f'Sprite\t\t\t{s}\t\t\t{s*20}\n')
        if t>0:
            textreceipt.insert(END,f'Maza\t\t\t{t}\t\t\t{t*20}\n')



    def total():
        receipt()
        TotalBill=(a*450)+(b*50)+(c*160)+(d*40)+(e*120)+(f*250)+(g*200)+(h*100)+(i*180)+(j*180)+(k*70)+(l*120)+(m*80)+(n*60)+(o*50)+(p*20)+(q*20)+(r*20)+(s*20)+(t*20)
        if TotalBill>0:
            textreceipt.insert(END,'==================================================\n')
            textreceipt.insert(END,f'TotalBill:\t\t\t\t\t\t{TotalBill}')

    def reset():
        global a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t
        a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
        textreceipt.delete(1.0,END)

    def send():
        top=Toplevel()
        top.geometry("250x200+600+300")
        top.title("Send Receipt")
        label=Label(top,text="Your Bill Sent Successful",compound='center',bg="#15133C",fg="#00FFAB")
        label.pack(pady=50)
        textreceipt.delete(1.0,END)
        global a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t
        a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
        top.mainloop()

    def back():
        root.destroy()
        global a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t
        a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

    #Background image and head
    filename=Image.open("D:\\Project\\photos\\Indian food\\background.jpg")
    filename=ImageTk.PhotoImage(filename.resize((1700,800)))
    l1=Label(root,image=filename)
    l1.place(x=0,y=0)
    root.title("Bill Machine")

    #frame head 1
    f1=Frame(root,bd=5,relief=GROOVE)
    f1.pack(side=TOP)

    #Frame head 2
    f2=Frame(root,bd=5,relief=GROOVE)
    f2.pack()

    #First head
    bill=Label(f1,text="Billing Machine",fg="#FF7F3F",bg="#FDD998",width=1300,font=("Times new roman",27,"bold"),compound='center')
    bill.pack()

    #Second Head
    indian_food=Label(f2,text="Chinese Food",fg="#FF7F3F",bg="#FDD998",width=1300,font=("Times new roman",27,"bold"),compound='center')
    indian_food.pack()

    #text in frame 3 and create
    f3=LabelFrame(root,text="Food",font=("Times new roman",25,"bold"),bg="#FDD998",fg="#FF7F3F")
    f3.pack(side=LEFT,padx=5)

    #first image
    image1=Image.open("D:\\Project\\photos\\chinese food\\Dim Sums.jfif")
    resize_image1=ImageTk.PhotoImage(image1.resize((115,65)))
    label_image1=Label(f3,image=resize_image1)
    label_image1.pack(ipady=5)

    #First image text 1
    label_text1=Label(f3,text="Dim Sums",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text1.pack()

    #Creating Button 1
    button1=Button(f3,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=dim)
    button1.pack(pady=2)

    #second image
    image2=Image.open("D:\\Project\\photos\\chinese food\\Quick Noodles.jfif")
    resize_image2=ImageTk.PhotoImage(image2.resize((115,65)))
    label_image2=Label(f3,image=resize_image2)
    label_image2.pack(ipady=5)

    #Second image text 2
    label_text2=Label(f3,text="Quick Noodles",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text2.pack()

    #Creating Button 2
    button2=Button(f3,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=quick)
    button2.pack(pady=2)

    #third image 
    image3=Image.open("D:\\Project\\photos\\chinese food\\Szechwan Chilli Chicken.jfif")
    resize_image3=ImageTk.PhotoImage(image3.resize((115,65)))
    label_image3=Label(f3,image=resize_image3)
    label_image3.pack(ipady=5)

    #Third image text 3
    label_text3=Label(f3,text="Szechwan Chilli Chicken",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text3.pack()

    #Creating Button 3
    button3=Button(f3,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=szechwan)
    button3.pack(pady=2)

    #four image 
    image4=Image.open("D:\\Project\\photos\\chinese food\\Spring Rolls.jfif")
    resize_image4=ImageTk.PhotoImage(image4.resize((115,65)))
    label_image4=Label(f3,image=resize_image4)
    label_image4.pack(ipady=5)

    #Third image text 4
    label_text4=Label(f3,text="Spring Rolls",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text4.pack()

    #Creating Button 4
    button4=Button(f3,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=springroll)
    button4.pack(pady=2)

    #five image 
    image5=Image.open("D:\\Project\\photos\\chinese food\\Stir Fried Tofu with Rice.jfif")
    resize_image5=ImageTk.PhotoImage(image5.resize((115,65)))
    label_image5=Label(f3,image=resize_image5)
    label_image5.pack(ipady=5)

    #Third image text 5
    label_text5=Label(f3,text="Stir Fried Tofu with Rice",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text5.pack()

    #Creating Button 5
    button5=Button(f3,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=rice)
    button5.pack(pady=2)



    #text and Frame creating 4
    sweet=LabelFrame(root,text="Sweet",font=("Times new roman",25,"bold"),bg="#FDD998",fg="#FF7F3F")
    sweet.pack(side=LEFT,padx=5)

    #first image in sweet
    sweet_image1=Image.open("D:\\Project\\photos\\chinese food\\Red Been Bun.jfif")
    sweet_resize_image1=ImageTk.PhotoImage(sweet_image1.resize((115,65)))
    sweet_label_image1=Label(sweet,image=sweet_resize_image1)
    sweet_label_image1.pack(ipady=5)

     #First image text 1 of sweet
    label_text6=Label(sweet,text="Red Been Bun",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text6.pack()

    #Creating Button 1 of sweet
    button6=Button(sweet,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=red)
    button6.pack(pady=2)

    #second image in sweet
    sweet_image2=Image.open("D:\\Project\\photos\\chinese food\\Egg Tarts.jfif")
    sweet_resize_image2=ImageTk.PhotoImage(sweet_image2.resize((115,65)))
    sweet_label_image2=Label(sweet,image=sweet_resize_image2)
    sweet_label_image2.pack(ipady=5)

     #second image text of sweet
    label_text7=Label(sweet,text="Egg Tarts",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text7.pack()

    #Creating Button 2 of sweet
    button7=Button(sweet,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=egg)
    button7.pack(pady=2)

    #third image in sweet
    sweet_image3=Image.open("D:\\Project\\photos\\chinese food\\Tanghulu..jfif")
    sweet_resize_image3=ImageTk.PhotoImage(sweet_image3.resize((115,65)))
    sweet_label_image3=Label(sweet,image=sweet_resize_image3)
    sweet_label_image3.pack(ipady=5)

     #third image text 1 of sweet
    label_text8=Label(sweet,text="Tanghulu",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text8.pack()

    #Creating Button 3 of sweet
    button8=Button(sweet,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=tanghulu)
    button8.pack(pady=2)

    #fourth image in sweet
    sweet_image4=Image.open("D:\\Project\\photos\\chinese food\\Pumpkin pancakes.jfif")
    sweet_resize_image4=ImageTk.PhotoImage(sweet_image4.resize((115,65)))
    sweet_label_image4=Label(sweet,image=sweet_resize_image4)
    sweet_label_image4.pack(ipady=5)

     #Fourth image text 1 of sweet
    label_text9=Label(sweet,text="Pumpkin pancakes",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text9.pack()

    #Creating Button 4 of sweet
    button9=Button(sweet,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=pancake)
    button9.pack(pady=2)

    #fifth image in sweet
    sweet_image5=Image.open("D:\\Project\\photos\\chinese food\\fried durian.jfif")
    sweet_resize_image5=ImageTk.PhotoImage(sweet_image5.resize((115,65)))
    sweet_label_image5=Label(sweet,image=sweet_resize_image5 )
    sweet_label_image5.pack(ipady=5)

     #Fifth image text 1 of sweet
    label_text10=Label(sweet,text="Fried Durian",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text10.pack()

    #Creating Button 5 of sweet
    button10=Button(sweet,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=fried)
    button10.pack(pady=2)


    #text and Frame creating 4
    drink=LabelFrame(root,text="Drink",font=("Times new roman",25,"bold"),bg="#FDD998",fg="#FF7F3F")
    drink.pack(side=LEFT,padx=5)

    #first image in drink
    drink_image1=Image.open("D:\\Project\\photos\\chinese food\\Tieguanyin.jfif")
    drink_resize_image1=ImageTk.PhotoImage(drink_image1.resize((115,65)))
    drink_label_image1=Label(drink,image=drink_resize_image1)
    drink_label_image1.pack(ipady=5)

     #First image text 1 of drink
    label_text11=Label(drink,text="Tieguanyin",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text11.pack()

    #Creating Button 1 of drink
    button11=Button(drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=Tieguanyin)
    button11.pack(pady=2)

    #second image in drink
    drink_image2=Image.open("D:\\Project\\photos\\chinese food\\Jiuniang.jfif")
    drink_resize_image2=ImageTk.PhotoImage(drink_image2.resize((115,65)))
    drink_label_image2=Label(drink,image=drink_resize_image2)
    drink_label_image2.pack(ipady=5)

     #second image text of drink
    label_text12=Label(drink,text="Jiuniang",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text12.pack()

    #Creating Button 2 of drink
    button12=Button(drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=Jiuniang)
    button12.pack(pady=2)

    #third image in drink
    drink_image3=Image.open("D:\\Project\\photos\\chinese food\\Pearl milk tea..jfif")
    drink_resize_image3=ImageTk.PhotoImage(drink_image3.resize((115,65)))
    drink_label_image3=Label(drink,image=drink_resize_image3)
    drink_label_image3.pack(ipady=5)

     #third image text 1 of drink
    label_text13=Label(drink,text="Pearl milk tea",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text13.pack()

    #Creating Button 3 of drink
    button13=Button(drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=pearl)
    button13.pack(pady=2)

    #fourth image in drink
    drink_image4=Image.open("D:\\Project\\photos\\chinese food\\Chivas mixed with green tea.jfif")
    drink_resize_image4=ImageTk.PhotoImage(drink_image4.resize((115,65)))
    drink_label_image4=Label(drink,image=drink_resize_image4)
    drink_label_image4.pack(ipady=5)

     #Fourth image text 1 of drink
    label_text14=Label(drink,text="Chivas mixed with green tea",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text14.pack()

    #Creating Button 4 of drink
    button14=Button(drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=greentea)
    button14.pack(pady=2)

    #fifth image in drink
    drink_image5=Image.open("D:\\Project\\photos\\chinese food\\Soybean milk.jfif")
    drink_resize_image5=ImageTk.PhotoImage(drink_image5.resize((115,65)))
    drink_label_image5=Label(drink,image=drink_resize_image5 )
    drink_label_image5.pack(ipady=5)

     #Fifth image text 1 of drink
    label_text15=Label(drink,text="Soybean milk",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text15.pack()

    #Creating Button 5 of drink
    button15=Button(drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=soybean)
    button15.pack(pady=2)

    #text and Frame creating 5
    soft_drink=LabelFrame(root,text="Soft Drink",font=("Times new roman",25,"bold"),bg="#FDD998",fg="#FF7F3F")
    soft_drink.pack(side=LEFT,padx=5)

    #first image in soft drink
    soft_drink_image1=Image.open("D:\\Project\\photos\\Indian food\\cocacola.jfif")
    soft_drink_resize_image1=ImageTk.PhotoImage(soft_drink_image1.resize((115,65)))
    soft_drink_label_image1=Label(soft_drink,image=soft_drink_resize_image1)
    soft_drink_label_image1.pack(ipady=5)

     #First image text 1 of soft drink
    label_text16=Label(soft_drink,text="Coca-Cola",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text16.pack()

    #Creating Button 1 of soft drink
    button16=Button(soft_drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=coca)
    button16.pack(pady=2)

    #second image in soft drink
    soft_drink_image2=Image.open("D:\\Project\\photos\\Indian food\\pepsi.jfif")
    soft_drink_resize_image2=ImageTk.PhotoImage(soft_drink_image2.resize((115,65)))
    soft_drink_label_image2=Label(soft_drink,image=soft_drink_resize_image2)
    soft_drink_label_image2.pack(ipady=5)

     #second image text of soft drink
    label_text17=Label(soft_drink,text="Pepsi",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text17.pack()

    #Creating Button 2 of soft drink
    button17=Button(soft_drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=pepsi)
    button17.pack(pady=2)

    #third image in soft drink
    soft_drink_image3=Image.open("D:\\Project\\photos\\Indian food\\thumbsup.jfif")
    soft_drink_resize_image3=ImageTk.PhotoImage(soft_drink_image3.resize((115,65)))
    soft_drink_label_image3=Label(soft_drink,image=soft_drink_resize_image3)
    soft_drink_label_image3.pack(ipady=5)

     #third image text 1 of soft drink
    label_text18=Label(soft_drink,text="Thumbs Up",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text18.pack()

    #Creating Button 3 of soft drink
    button18=Button(soft_drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=thumbs)
    button18.pack(pady=2)

    #fourth image in soft drink
    soft_drink_image4=Image.open("D:\\Project\\photos\\Indian food\\sprite.jfif")
    soft_drink_resize_image4=ImageTk.PhotoImage(soft_drink_image4.resize((115,65)))
    soft_drink_label_image4=Label(soft_drink,image=soft_drink_resize_image4)
    soft_drink_label_image4.pack(ipady=5)

     #Fourth image text 1 of soft drink
    label_text19=Label(soft_drink,text="Sprite",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text19.pack()

    #Creating Button 4 of soft drink
    button19=Button(soft_drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=sprite)
    button19.pack(pady=2)

    #fifth image in soft drink
    soft_drink_image5=Image.open("D:\\Project\\photos\\Indian food\\maza.jfif")
    soft_drink_resize_image5=ImageTk.PhotoImage(soft_drink_image5.resize((115,65)))
    soft_drink_label_image5=Label(soft_drink,image=soft_drink_resize_image5 )
    soft_drink_label_image5.pack(ipady=5)

     #Fifth image text 1 of soft drink
    label_text20=Label(soft_drink,text="Maza",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text20.pack()

    #Creating Button 5 of soft drink
    button20=Button(soft_drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=maza)
    button20.pack(pady=2)

    #creating frame 5
    billframe=LabelFrame(root,text="Receipt",font=("Times new roman",25,"bold"),bg="#FDD998",fg="#FF7F3F")
    billframe.pack(side=LEFT,padx=7)

    #adding text area
    textreceipt=Text(billframe,font=("Times new roman",12,"bold"),bg="white",height=30)
    textreceipt.pack()

    #creating button
    button21=Button(billframe,text="Total",bg="#FDD998",fg="#FF7F3F",font=("Times new roman",15,"bold"),compound='center',command=total)
    button21.pack(side=LEFT,padx=13,pady=5)

    button22=Button(billframe,text="Receipt",bg="#FDD998",fg="#FF7F3F",font=("Times new roman",15,"bold"),compound='center',command=receipt)
    button22.pack(side=LEFT,padx=13)

    button23=Button(billframe,text="Reset",bg="#FDD998",fg="#FF7F3F",font=("Times new roman",15,"bold"),compound='center',command=reset)
    button23.pack(side=LEFT,padx=13)

    button24=Button(billframe,text="Send",bg="#FDD998",fg="#FF7F3F",font=("Times new roman",15,"bold"),compound='center',command=send)
    button24.pack(side=LEFT,padx=13)

    button25=Button(billframe,text="Back",bg="#FDD998",fg="#FF7F3F",font=("Times new roman",15,"bold"),compound='center',command=back)
    button25.pack(side=LEFT,padx=13)

    

    #Indian Food Page Mainloop
    root.mainloop()  

def American_Food():
    root=Toplevel()
    root.geometry("1600x1300+0+0")
    def apple():
        global a
        a=a+1
    def hamburger():
        global b
        b=b+1
    def bagel_lox():
        global c
        c+=1
    def pizza():
        global d
        d+=1
    def Texas():
        global e
        e+=1
    def cookies():
        global f
        f+=1
    def cobbler():
        global g
        g+=1
    def gelato():
        global h
        h+=1
    def todd():
        global i
        i+=1
    def carrot_cake():
        global j
        j+=1
    def old():
        global k
        k+=1
    def Sazerac():
        global l
        l+=1
    def Manhattan():
        global m
        m+=1
    def julep():
        global n
        n+=1
    def pisco():
        global o
        o+=1
    def coca():
        global p
        p+=1
    def pepsi():
        global q
        q+=1
    def thumbs():
        global r
        r+=1
    def sprite():
        global s
        s+=1
    def maza():
        global t
        t+=1

    def receipt():
        global TotalBill
        textreceipt.delete(1.0,END)
        x=random.randint(100,10000)
        billnumber='BILL'+str(x)
        date=time.strftime('%d/%m/%Y')
        textreceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t\t'+date+'\n')
        txtName=text.get()
        textreceipt.insert(END,f'Customer Name:\t{txtName}\n')
        textreceipt.insert(END,'==================================================\n')
        textreceipt.insert(END,f'Items\t\t\tQnt.\t\t\tPrice\n')
        if a>0:
            textreceipt.insert(END,f'Apple Pie\t\t\t{a}\t\t\t{a*150}\n')
        if b>0:
            textreceipt.insert(END,f'The Hamburger\t\t\t{b}\t\t\t{b*160}\n')
        if c>0:
            textreceipt.insert(END,f'Bagel and Lox\t\t\t{c}\t\t\t{c*200}\n')
        if d>0:
            textreceipt.insert(END,f'Deep-Dish Pizza\t\t\t{d}\t\t\t{d*299}\n')
        if e>0:
            textreceipt.insert(END,f'Texas Barbecue\t\t\t{e}\t\t\t{e*180}\n')
        if f>0:
            textreceipt.insert(END,f'The Perfect Chocolate Chip Cookies\t\t\t{f}\t\t\t{f*90}\n')
        if g>0:
            textreceipt.insert(END,f'Peach Cobbler\t\t\t{g}\t\t\t{g*150}\n')
        if h>0:
            textreceipt.insert(END,f'Vanilla Gelato\t\t\t{h}\t\t\t{h*120}\n')
        if i>0:
            textreceipt.insert(END,f"Todd's Snickerdoodles\t\t\t{i}\t\t\t{i*90}\n")
        if j>0:
            textreceipt.insert(END,f'Classic Carrot Cake\t\t\t{j}\t\t\t{j*300}\n')
        if k>0:
            textreceipt.insert(END,f'Old-Fashioned\t\t\t{k}\t\t\t{k*80}\n')
        if l>0:
            textreceipt.insert(END,f'Sazerac\t\t\t{l}\t\t\t{l*150}\n')
        if m>0:
            textreceipt.insert(END,f'Manhattan\t\t\t{m}\t\t\t{m*200}\n')
        if n>0:
            textreceipt.insert(END,f'Mint Julep\t\t\t{n}\t\t\t{n*150}\n')
        if o>0:
            textreceipt.insert(END,f'Pisco Punch\t\t\t{o}\t\t\t{o*100}\n')
        if p>0:
            textreceipt.insert(END,f'Coca-Cola\t\t\t{p}\t\t\t{p*20}\n')
        if q>0:
            textreceipt.insert(END,f'Pepsi\t\t\t{q}\t\t\t{q*20}\n')
        if r>0:
            textreceipt.insert(END,f'Thumbs Up\t\t\t{r}\t\t\t{r*20}\n')
        if s>0:
            textreceipt.insert(END,f'Sprite\t\t\t{s}\t\t\t{s*20}\n')
        if t>0:
            textreceipt.insert(END,f'Maza\t\t\t{t}\t\t\t{t*20}\n')



    def total():
        TotalBill=(a*150)+(b*160)+(c*200)+(d*299)+(e*180)+(f*90)+(g*150)+(h*120)+(i*90)+(j*300)+(k*80)+(l*150)+(m*200)+(n*150)+(o*100)+(p*20)+(q*20)+(r*20)+(s*20)+(t*20)
        if TotalBill>0:
            textreceipt.insert(END,'==================================================\n')
            textreceipt.insert(END,f'TotalBill:\t\t\t\t\t\t{TotalBill}')

    def reset():
        global a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t
        a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
        textreceipt.delete(1.0,END)

    def send():
        top=Toplevel()
        top.geometry("250x200+600+300")
        top.title("Send Receipt")
        label=Label(top,text="Your Bill Sent Successful",compound='center',bg="#15133C",fg="#00FFAB")
        label.pack(pady=50)
        textreceipt.delete(1.0,END)
        global a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t
        a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
        top.mainloop()

    def back():
        root.destroy()
        global a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t
        a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

    #Background image and head
    filename=Image.open("D:\\Project\\photos\\Indian food\\background.jpg")
    filename=ImageTk.PhotoImage(filename.resize((1700,800)))
    l1=Label(root,image=filename)
    l1.place(x=0,y=0)
    root.title("Bill Machine")

    #frame head 1
    f1=Frame(root,bd=5,relief=GROOVE)
    f1.pack(side=TOP)

    #Frame head 2
    f2=Frame(root,bd=5,relief=GROOVE)
    f2.pack()

    #First head
    bill=Label(f1,text="Billing Machine",fg="#FF7F3F",bg="#FDD998",width=1300,font=("Times new roman",27,"bold"),compound='center')
    bill.pack()

    #Second Head
    indian_food=Label(f2,text="American Food",fg="#FF7F3F",bg="#FDD998",width=1300,font=("Times new roman",27,"bold"),compound='center')
    indian_food.pack()

    #text in frame 3 and create
    f3=LabelFrame(root,text="Food",font=("Times new roman",25,"bold"),bg="#FDD998",fg="#FF7F3F")
    f3.pack(side=LEFT,padx=5)

    #first image
    image1=Image.open("D:\\Project\\photos\\American food\\Apple Pie.jfif")
    resize_image1=ImageTk.PhotoImage(image1.resize((115,65)))
    label_image1=Label(f3,image=resize_image1)
    label_image1.pack(ipady=5)

    #First image text 1
    label_text1=Label(f3,text="Apple Pie",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text1.pack()

    #Creating Button 1
    button1=Button(f3,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=apple)
    button1.pack(pady=2)

    #second image
    image2=Image.open("D:\\Project\\photos\\American food\\The Hamburger.jfif")
    resize_image2=ImageTk.PhotoImage(image2.resize((115,65)))
    label_image2=Label(f3,image=resize_image2)
    label_image2.pack(ipady=5)

    #Second image text 2
    label_text2=Label(f3,text="The Hamburger",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text2.pack()

    #Creating Button 2
    button2=Button(f3,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=hamburger)
    button2.pack(pady=2)

    #third image 
    image3=Image.open("D:\\Project\\photos\\American food\\Bagel and Lox.jfif")
    resize_image3=ImageTk.PhotoImage(image3.resize((115,65)))
    label_image3=Label(f3,image=resize_image3)
    label_image3.pack(ipady=5)

    #Third image text 3
    label_text3=Label(f3,text="Bagel and Lox",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text3.pack()

    #Creating Button 3
    button3=Button(f3,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=bagel_lox)
    button3.pack(pady=2)

    #four image 
    image4=Image.open("D:\\Project\\photos\\American food\\Deep-Dish Pizza.jfif")
    resize_image4=ImageTk.PhotoImage(image4.resize((115,65)))
    label_image4=Label(f3,image=resize_image4)
    label_image4.pack(ipady=5)

    #Third image text 4
    label_text4=Label(f3,text="Deep-Dish Pizza",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text4.pack()

    #Creating Button 4
    button4=Button(f3,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=pizza)
    button4.pack(pady=2)

    #five image 
    image5=Image.open("D:\\Project\\photos\\American food\\Texas Barbecue.jfif")
    resize_image5=ImageTk.PhotoImage(image5.resize((115,65)))
    label_image5=Label(f3,image=resize_image5)
    label_image5.pack(ipady=5)

    #Third image text 5
    label_text5=Label(f3,text="Texas Barbecue",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text5.pack()

    #Creating Button 5
    button5=Button(f3,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=Texas)
    button5.pack(pady=2)



    #text and Frame creating 4
    sweet=LabelFrame(root,text="Sweet",font=("Times new roman",25,"bold"),bg="#FDD998",fg="#FF7F3F")
    sweet.pack(side=LEFT,padx=5)

    #first image in sweet
    sweet_image1=Image.open("D:\\Project\\photos\\American food\\The Perfect Chocolate Chip Cookies.jfif")
    sweet_resize_image1=ImageTk.PhotoImage(sweet_image1.resize((115,65)))
    sweet_label_image1=Label(sweet,image=sweet_resize_image1)
    sweet_label_image1.pack(ipady=5)

     #First image text 1 of sweet
    label_text6=Label(sweet,text="The Perfect Chocolate Chip Cookies",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text6.pack()

    #Creating Button 1 of sweet
    button6=Button(sweet,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=cookies)
    button6.pack(pady=2)

    #second image in sweet
    sweet_image2=Image.open("D:\\Project\\photos\\American food\\Peach Cobbler.jfif")
    sweet_resize_image2=ImageTk.PhotoImage(sweet_image2.resize((115,65)))
    sweet_label_image2=Label(sweet,image=sweet_resize_image2)
    sweet_label_image2.pack(ipady=5)

     #second image text of sweet
    label_text7=Label(sweet,text="Peach Cobbler",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text7.pack()

    #Creating Button 2 of sweet
    button7=Button(sweet,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=cobbler)
    button7.pack(pady=2)

    #third image in sweet
    sweet_image3=Image.open("D:\\Project\\photos\\American food\\Vanilla Gelato.jfif")
    sweet_resize_image3=ImageTk.PhotoImage(sweet_image3.resize((115,65)))
    sweet_label_image3=Label(sweet,image=sweet_resize_image3)
    sweet_label_image3.pack(ipady=5)

     #third image text 1 of sweet
    label_text8=Label(sweet,text="Vanilla Gelato",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text8.pack()

    #Creating Button 3 of sweet
    button8=Button(sweet,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=gelato)
    button8.pack(pady=2)

    #fourth image in sweet
    sweet_image4=Image.open("D:\\Project\\photos\\American food\\Todd's Snickerdoodles.jfif")
    sweet_resize_image4=ImageTk.PhotoImage(sweet_image4.resize((115,65)))
    sweet_label_image4=Label(sweet,image=sweet_resize_image4)
    sweet_label_image4.pack(ipady=5)

     #Fourth image text 1 of sweet
    label_text9=Label(sweet,text="Todd's Snickerdoodles",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text9.pack()

    #Creating Button 4 of sweet
    button9=Button(sweet,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=todd)
    button9.pack(pady=2)

    #fifth image in sweet
    sweet_image5=Image.open("D:\\Project\\photos\\American food\\Classic Carrot Cake.jfif")
    sweet_resize_image5=ImageTk.PhotoImage(sweet_image5.resize((115,65)))
    sweet_label_image5=Label(sweet,image=sweet_resize_image5 )
    sweet_label_image5.pack(ipady=5)

     #Fifth image text 1 of sweet
    label_text10=Label(sweet,text="Classic Carrot Cake",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text10.pack()

    #Creating Button 5 of sweet
    button10=Button(sweet,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=carrot_cake)
    button10.pack(pady=2)


    #text and Frame creating 4
    drink=LabelFrame(root,text="Drink",font=("Times new roman",25,"bold"),bg="#FDD998",fg="#FF7F3F")
    drink.pack(side=LEFT,padx=5)

    #first image in drink
    drink_image1=Image.open("D:\\Project\\photos\\American food\\Old-Fashioned.jfif")
    drink_resize_image1=ImageTk.PhotoImage(drink_image1.resize((115,65)))
    drink_label_image1=Label(drink,image=drink_resize_image1)
    drink_label_image1.pack(ipady=5)

     #First image text 1 of drink
    label_text11=Label(drink,text="Old-Fashioned",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text11.pack()

    #Creating Button 1 of drink
    button11=Button(drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=old)
    button11.pack(pady=2)

    #second image in drink
    drink_image2=Image.open("D:\\Project\\photos\\American food\\Sazerac.jfif")
    drink_resize_image2=ImageTk.PhotoImage(drink_image2.resize((115,65)))
    drink_label_image2=Label(drink,image=drink_resize_image2)
    drink_label_image2.pack(ipady=5)

     #second image text of drink
    label_text12=Label(drink,text="Sazerac",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text12.pack()

    #Creating Button 2 of drink
    button12=Button(drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=Sazerac)
    button12.pack(pady=2)

    #third image in drink
    drink_image3=Image.open("D:\\Project\\photos\\American food\\Manhattan..jfif")
    drink_resize_image3=ImageTk.PhotoImage(drink_image3.resize((115,65)))
    drink_label_image3=Label(drink,image=drink_resize_image3)
    drink_label_image3.pack(ipady=5)

     #third image text 1 of drink
    label_text13=Label(drink,text="Manhattan",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text13.pack()

    #Creating Button 3 of drink
    button13=Button(drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=Manhattan)
    button13.pack(pady=2)

    #fourth image in drink
    drink_image4=Image.open("D:\\Project\\photos\\American food\\Mint Julep.jfif")
    drink_resize_image4=ImageTk.PhotoImage(drink_image4.resize((115,65)))
    drink_label_image4=Label(drink,image=drink_resize_image4)
    drink_label_image4.pack(ipady=5)

     #Fourth image text 1 of drink
    label_text14=Label(drink,text="Mint Julep",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text14.pack()

    #Creating Button 4 of drink
    button14=Button(drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=julep)
    button14.pack(pady=2)

    #fifth image in drink
    drink_image5=Image.open("D:\\Project\\photos\\American food\\Pisco Punch.jfif")
    drink_resize_image5=ImageTk.PhotoImage(drink_image5.resize((115,65)))
    drink_label_image5=Label(drink,image=drink_resize_image5 )
    drink_label_image5.pack(ipady=5)

     #Fifth image text 1 of drink
    label_text15=Label(drink,text="Pisco Punch",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text15.pack()

    #Creating Button 5 of drink
    button15=Button(drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=pisco)
    button15.pack(pady=2)

    #text and Frame creating 5
    soft_drink=LabelFrame(root,text="Soft Drink",font=("Times new roman",25,"bold"),bg="#FDD998",fg="#FF7F3F")
    soft_drink.pack(side=LEFT,padx=5)

    #first image in soft drink
    soft_drink_image1=Image.open("D:\\Project\\photos\\Indian food\\cocacola.jfif")
    soft_drink_resize_image1=ImageTk.PhotoImage(soft_drink_image1.resize((115,65)))
    soft_drink_label_image1=Label(soft_drink,image=soft_drink_resize_image1)
    soft_drink_label_image1.pack(ipady=5)

     #First image text 1 of soft drink
    label_text16=Label(soft_drink,text="Coca-Cola",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text16.pack()

    #Creating Button 1 of soft drink
    button16=Button(soft_drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=coca)
    button16.pack(pady=2)

    #second image in soft drink
    soft_drink_image2=Image.open("D:\\Project\\photos\\Indian food\\pepsi.jfif")
    soft_drink_resize_image2=ImageTk.PhotoImage(soft_drink_image2.resize((115,65)))
    soft_drink_label_image2=Label(soft_drink,image=soft_drink_resize_image2)
    soft_drink_label_image2.pack(ipady=5)

     #second image text of soft drink
    label_text17=Label(soft_drink,text="Pepsi",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text17.pack()

    #Creating Button 2 of soft drink
    button17=Button(soft_drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=pepsi)
    button17.pack(pady=2)

    #third image in soft drink
    soft_drink_image3=Image.open("D:\\Project\\photos\\Indian food\\thumbsup.jfif")
    soft_drink_resize_image3=ImageTk.PhotoImage(soft_drink_image3.resize((115,65)))
    soft_drink_label_image3=Label(soft_drink,image=soft_drink_resize_image3)
    soft_drink_label_image3.pack(ipady=5)

     #third image text 1 of soft drink
    label_text18=Label(soft_drink,text="Thumbs Up",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text18.pack()

    #Creating Button 3 of soft drink
    button18=Button(soft_drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=thumbs)
    button18.pack(pady=2)

    #fourth image in soft drink
    soft_drink_image4=Image.open("D:\\Project\\photos\\Indian food\\sprite.jfif")
    soft_drink_resize_image4=ImageTk.PhotoImage(soft_drink_image4.resize((115,65)))
    soft_drink_label_image4=Label(soft_drink,image=soft_drink_resize_image4)
    soft_drink_label_image4.pack(ipady=5)

     #Fourth image text 1 of soft drink
    label_text19=Label(soft_drink,text="Sprite",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text19.pack()

    #Creating Button 4 of soft drink
    button19=Button(soft_drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=sprite)
    button19.pack(pady=2)

    #fifth image in soft drink
    soft_drink_image5=Image.open("D:\\Project\\photos\\Indian food\\maza.jfif")
    soft_drink_resize_image5=ImageTk.PhotoImage(soft_drink_image5.resize((115,65)))
    soft_drink_label_image5=Label(soft_drink,image=soft_drink_resize_image5 )
    soft_drink_label_image5.pack(ipady=5)

     #Fifth image text 1 of soft drink
    label_text20=Label(soft_drink,text="Maza",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text20.pack()

    #Creating Button 5 of soft drink
    button20=Button(soft_drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=maza)
    button20.pack(pady=2)

    #creating frame 5
    billframe=LabelFrame(root,text="Receipt",font=("Times new roman",25,"bold"),bg="#FDD998",fg="#FF7F3F")
    billframe.pack(side=LEFT,padx=7)

    #adding text area
    textreceipt=Text(billframe,font=("Times new roman",12,"bold"),bg="white",height=30)
    textreceipt.pack()

    #creating button
    button21=Button(billframe,text="Total",bg="#FDD998",fg="#FF7F3F",font=("Times new roman",15,"bold"),compound='center',command=total)
    button21.pack(side=LEFT,padx=13,pady=5)

    button22=Button(billframe,text="Receipt",bg="#FDD998",fg="#FF7F3F",font=("Times new roman",15,"bold"),compound='center',command=receipt)
    button22.pack(side=LEFT,padx=13)

    button23=Button(billframe,text="Reset",bg="#FDD998",fg="#FF7F3F",font=("Times new roman",15,"bold"),compound='center',command=reset)
    button23.pack(side=LEFT,padx=13)

    button24=Button(billframe,text="Send",bg="#FDD998",fg="#FF7F3F",font=("Times new roman",15,"bold"),compound='center',command=send)
    button24.pack(side=LEFT,padx=13)

    button25=Button(billframe,text="Back",bg="#FDD998",fg="#FF7F3F",font=("Times new roman",15,"bold"),compound='center',command=back)
    button25.pack(side=LEFT,padx=13)

    

    #Indian Food Page Mainloop
    root.mainloop()  



def Italian_Food():
    root=Toplevel()
    root.geometry("1600x1300+0+0")
    def Risotto():
        global a
        a=a+1
    def polenta():
        global b
        b=b+1
    def Lasagna():
        global c
        c+=1
    def Ravioli():
        global d
        d+=1
    def Ribollita():
        global e
        e+=1
    def Tiramisu():
        global f
        f+=1
    def Torta():
        global g
        g+=1
    def cotta():
        global h
        h+=1
    def Semifreddo():
        global i
        i+=1
    def Cannoli():
        global j
        j+=1
    def Americano():
        global k
        k+=1
    def Negroni():
        global l
        l+=1
    def Aperitivo():
        global m
        m+=1
    def Bellini():
        global n
        n+=1
    def Campari():
        global o
        o+=1
    def coca():
        global p
        p+=1
    def pepsi():
        global q
        q+=1
    def thumbs():
        global r
        r+=1
    def sprite():
        global s
        s+=1
    def maza():
        global t
        t+=1

    def receipt():
        global TotalBill
        textreceipt.delete(1.0,END)
        x=random.randint(100,10000)
        billnumber='BILL'+str(x)
        date=time.strftime('%d/%m/%Y')
        textreceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t\t'+date+'\n')
        txtName=text.get()
        textreceipt.insert(END,f'Customer Name:\t{txtName}\n')
        textreceipt.insert(END,'==================================================\n')
        textreceipt.insert(END,f'Items\t\t\tQnt.\t\t\tPrice\n')
        if a>0:
            textreceipt.insert(END,f'Risotto Alla Milanese\t\t\t{a}\t\t\t{a*200}\n')
        if b>0:
            textreceipt.insert(END,f'Polenta\t\t\t{b}\t\t\t{b*490}\n')
        if c>0:
            textreceipt.insert(END,f'Lasagna\t\t\t{c}\t\t\t{c*150}\n')
        if d>0:
            textreceipt.insert(END,f'Ravioli\t\t\t{d}\t\t\t{d*100}\n')
        if e>0:
            textreceipt.insert(END,f'Ribollita\t\t\t{e}\t\t\t{e*180}\n')
        if f>0:
            textreceipt.insert(END,f'Tiramisu\t\t\t{f}\t\t\t{f*80}\n')
        if g>0:
            textreceipt.insert(END,f'Torta del nonna\t\t\t{g}\t\t\t{g*250}\n')
        if h>0:
            textreceipt.insert(END,f'Vanilla panna cotta\t\t\t{h}\t\t\t{h*300}\n')
        if i>0:
            textreceipt.insert(END,f"Semifreddo\t\t\t{i}\t\t\t{i*140}\n")
        if j>0:
            textreceipt.insert(END,f'Cannoli\t\t\t{j}\t\t\t{j*250}\n')
        if k>0:
            textreceipt.insert(END,f'Americano\t\t\t{k}\t\t\t{k*280}\n')
        if l>0:
            textreceipt.insert(END,f'Negroni\t\t\t{l}\t\t\t{l*600}\n')
        if m>0:
            textreceipt.insert(END,f'Aperitivo\t\t\t{m}\t\t\t{m*150}\n')
        if n>0:
            textreceipt.insert(END,f'Bellini\t\t\t{n}\t\t\t{n*150}\n')
        if o>0:
            textreceipt.insert(END,f'Campari\t\t\t{o}\t\t\t{o*200}\n')
        if p>0:
            textreceipt.insert(END,f'Coca-Cola\t\t\t{p}\t\t\t{p*20}\n')
        if q>0:
            textreceipt.insert(END,f'Pepsi\t\t\t{q}\t\t\t{q*20}\n')
        if r>0:
            textreceipt.insert(END,f'Thumbs Up\t\t\t{r}\t\t\t{r*20}\n')
        if s>0:
            textreceipt.insert(END,f'Sprite\t\t\t{s}\t\t\t{s*20}\n')
        if t>0:
            textreceipt.insert(END,f'Maza\t\t\t{t}\t\t\t{t*20}\n')



    def total():
        TotalBill=(a*200)+(b*490)+(c*150)+(d*100)+(e*180)+(f*80)+(g*250)+(h*300)+(i*140)+(j*250)+(k*280)+(l*600)+(m*150)+(n*150)+(o*200)+(p*20)+(q*20)+(r*20)+(s*20)+(t*20)
        if TotalBill>0:
            textreceipt.insert(END,'==================================================\n')
            textreceipt.insert(END,f'TotalBill:\t\t\t\t\t\t{TotalBill}')

    def reset():
        global a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t
        a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
        textreceipt.delete(1.0,END)

    def send():
        top=Toplevel()
        top.geometry("250x200+600+300")
        top.title("Send Receipt")
        label=Label(top,text="Your Bill Sent Successful",compound='center',bg="#15133C",fg="#00FFAB")
        label.pack(pady=50)
        textreceipt.delete(1.0,END)
        global a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t
        a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
        top.mainloop()

    def back():
        root.destroy()
        global a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t
        a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

    #Background image and head
    filename=Image.open("D:\\Project\\photos\\Indian food\\background.jpg")
    filename=ImageTk.PhotoImage(filename.resize((1700,800)))
    l1=Label(root,image=filename)
    l1.place(x=0,y=0)
    root.title("Bill Machine")

    #frame head 1
    f1=Frame(root,bd=5,relief=GROOVE)
    f1.pack(side=TOP)

    #Frame head 2
    f2=Frame(root,bd=5,relief=GROOVE)
    f2.pack()

    #First head
    bill=Label(f1,text="Billing Machine",fg="#FF7F3F",bg="#FDD998",width=1300,font=("Times new roman",27,"bold"),compound='center')
    bill.pack()

    #Second Head
    indian_food=Label(f2,text="American Food",fg="#FF7F3F",bg="#FDD998",width=1300,font=("Times new roman",27,"bold"),compound='center')
    indian_food.pack()

    #text in frame 3 and create
    f3=LabelFrame(root,text="Food",font=("Times new roman",25,"bold"),bg="#FDD998",fg="#FF7F3F")
    f3.pack(side=LEFT,padx=5)

    #first image
    image1=Image.open("D:\\Project\\photos\\Italian Food\\Risotto Alla Milanese.jfif")
    resize_image1=ImageTk.PhotoImage(image1.resize((115,65)))
    label_image1=Label(f3,image=resize_image1)
    label_image1.pack(ipady=5)

    #First image text 1
    label_text1=Label(f3,text="Risotto Alla Milanese",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text1.pack()

    #Creating Button 1
    button1=Button(f3,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=Risotto)
    button1.pack(pady=2)

    #second image
    image2=Image.open("D:\\Project\\photos\\Italian Food\\polenta.jfif")
    resize_image2=ImageTk.PhotoImage(image2.resize((115,65)))
    label_image2=Label(f3,image=resize_image2)
    label_image2.pack(ipady=5)

    #Second image text 2
    label_text2=Label(f3,text="Polenta",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text2.pack()

    #Creating Button 2
    button2=Button(f3,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=polenta)
    button2.pack(pady=2)

    #third image 
    image3=Image.open("D:\\Project\\photos\\Italian Food\\Lasagna.jfif")
    resize_image3=ImageTk.PhotoImage(image3.resize((115,65)))
    label_image3=Label(f3,image=resize_image3)
    label_image3.pack(ipady=5)

    #Third image text 3
    label_text3=Label(f3,text="Lasagna",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text3.pack()

    #Creating Button 3
    button3=Button(f3,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=Lasagna)
    button3.pack(pady=2)

    #four image 
    image4=Image.open("D:\\Project\\photos\\Italian Food\\Ravioli.jfif")
    resize_image4=ImageTk.PhotoImage(image4.resize((115,65)))
    label_image4=Label(f3,image=resize_image4)
    label_image4.pack(ipady=5)

    #Third image text 4
    label_text4=Label(f3,text="Ravioli",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text4.pack()

    #Creating Button 4
    button4=Button(f3,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=Ravioli)
    button4.pack(pady=2)

    #five image 
    image5=Image.open("D:\\Project\\photos\\Italian Food\\Ribollita.jfif")
    resize_image5=ImageTk.PhotoImage(image5.resize((115,65)))
    label_image5=Label(f3,image=resize_image5)
    label_image5.pack(ipady=5)

    #Third image text 5
    label_text5=Label(f3,text="Ribollita",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text5.pack()

    #Creating Button 5
    button5=Button(f3,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=Ribollita)
    button5.pack(pady=2)



    #text and Frame creating 4
    sweet=LabelFrame(root,text="Sweet",font=("Times new roman",25,"bold"),bg="#FDD998",fg="#FF7F3F")
    sweet.pack(side=LEFT,padx=5)

    #first image in sweet
    sweet_image1=Image.open("D:\\Project\\photos\\Italian Food\\Tiramisu.jfif")
    sweet_resize_image1=ImageTk.PhotoImage(sweet_image1.resize((115,65)))
    sweet_label_image1=Label(sweet,image=sweet_resize_image1)
    sweet_label_image1.pack(ipady=5)

     #First image text 1 of sweet
    label_text6=Label(sweet,text="Tiramisu",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text6.pack()

    #Creating Button 1 of sweet
    button6=Button(sweet,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=Tiramisu)
    button6.pack(pady=2)

    #second image in sweet
    sweet_image2=Image.open("D:\\Project\\photos\\Italian Food\\Torta del nonna.jfif")
    sweet_resize_image2=ImageTk.PhotoImage(sweet_image2.resize((115,65)))
    sweet_label_image2=Label(sweet,image=sweet_resize_image2)
    sweet_label_image2.pack(ipady=5)

     #second image text of sweet
    label_text7=Label(sweet,text="Torta del nonna",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text7.pack()

    #Creating Button 2 of sweet
    button7=Button(sweet,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=Torta)
    button7.pack(pady=2)

    #third image in sweet
    sweet_image3=Image.open("D:\\Project\\photos\\Italian Food\\Vanilla panna cotta.jfif")
    sweet_resize_image3=ImageTk.PhotoImage(sweet_image3.resize((115,65)))
    sweet_label_image3=Label(sweet,image=sweet_resize_image3)
    sweet_label_image3.pack(ipady=5)

     #third image text 1 of sweet
    label_text8=Label(sweet,text="Vanilla panna cotta",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text8.pack()

    #Creating Button 3 of sweet
    button8=Button(sweet,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=cotta)
    button8.pack(pady=2)

    #fourth image in sweet
    sweet_image4=Image.open("D:\\Project\\photos\\Italian Food\\Semifreddo.jfif")
    sweet_resize_image4=ImageTk.PhotoImage(sweet_image4.resize((115,65)))
    sweet_label_image4=Label(sweet,image=sweet_resize_image4)
    sweet_label_image4.pack(ipady=5)

     #Fourth image text 1 of sweet
    label_text9=Label(sweet,text="Semifreddo",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text9.pack()

    #Creating Button 4 of sweet
    button9=Button(sweet,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=Semifreddo)
    button9.pack(pady=2)

    #fifth image in sweet
    sweet_image5=Image.open("D:\\Project\\photos\\Italian Food\\Cannoli.jfif")
    sweet_resize_image5=ImageTk.PhotoImage(sweet_image5.resize((115,65)))
    sweet_label_image5=Label(sweet,image=sweet_resize_image5 )
    sweet_label_image5.pack(ipady=5)

     #Fifth image text 1 of sweet
    label_text10=Label(sweet,text="Cannoli",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text10.pack()

    #Creating Button 5 of sweet
    button10=Button(sweet,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=Cannoli)
    button10.pack(pady=2)


    #text and Frame creating 4
    drink=LabelFrame(root,text="Drink",font=("Times new roman",25,"bold"),bg="#FDD998",fg="#FF7F3F")
    drink.pack(side=LEFT,padx=5)

    #first image in drink
    drink_image1=Image.open("D:\\Project\\photos\\Italian Food\\Americano.jfif")
    drink_resize_image1=ImageTk.PhotoImage(drink_image1.resize((115,65)))
    drink_label_image1=Label(drink,image=drink_resize_image1)
    drink_label_image1.pack(ipady=5)

     #First image text 1 of drink
    label_text11=Label(drink,text="Americano",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text11.pack()

    #Creating Button 1 of drink
    button11=Button(drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=Americano)
    button11.pack(pady=2)

    #second image in drink
    drink_image2=Image.open("D:\\Project\\photos\\Italian Food\\Negroni.jfif")
    drink_resize_image2=ImageTk.PhotoImage(drink_image2.resize((115,65)))
    drink_label_image2=Label(drink,image=drink_resize_image2)
    drink_label_image2.pack(ipady=5)

     #second image text of drink
    label_text12=Label(drink,text="Negroni",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text12.pack()

    #Creating Button 2 of drink
    button12=Button(drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=Negroni)
    button12.pack(pady=2)

    #third image in drink
    drink_image3=Image.open("D:\\Project\\photos\\Italian Food\\Aperitivo.jfif")
    drink_resize_image3=ImageTk.PhotoImage(drink_image3.resize((115,65)))
    drink_label_image3=Label(drink,image=drink_resize_image3)
    drink_label_image3.pack(ipady=5)

     #third image text 1 of drink
    label_text13=Label(drink,text="Aperitivo",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text13.pack()

    #Creating Button 3 of drink
    button13=Button(drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=Aperitivo)
    button13.pack(pady=2)

    #fourth image in drink
    drink_image4=Image.open("D:\\Project\\photos\\Italian Food\\Bellini.jfif")
    drink_resize_image4=ImageTk.PhotoImage(drink_image4.resize((115,65)))
    drink_label_image4=Label(drink,image=drink_resize_image4)
    drink_label_image4.pack(ipady=5)

     #Fourth image text 1 of drink
    label_text14=Label(drink,text="Bellini",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text14.pack()

    #Creating Button 4 of drink
    button14=Button(drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=Bellini)
    button14.pack(pady=2)

    #fifth image in drink
    drink_image5=Image.open("D:\\Project\\photos\\Italian Food\\Campari.jfif")
    drink_resize_image5=ImageTk.PhotoImage(drink_image5.resize((115,65)))
    drink_label_image5=Label(drink,image=drink_resize_image5 )
    drink_label_image5.pack(ipady=5)

     #Fifth image text 1 of drink
    label_text15=Label(drink,text="Campari",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text15.pack()

    #Creating Button 5 of drink
    button15=Button(drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=Campari)
    button15.pack(pady=2)

    #text and Frame creating 5
    soft_drink=LabelFrame(root,text="Soft Drink",font=("Times new roman",25,"bold"),bg="#FDD998",fg="#FF7F3F")
    soft_drink.pack(side=LEFT,padx=5)

    #first image in soft drink
    soft_drink_image1=Image.open("D:\\Project\\photos\\Indian food\\cocacola.jfif")
    soft_drink_resize_image1=ImageTk.PhotoImage(soft_drink_image1.resize((115,65)))
    soft_drink_label_image1=Label(soft_drink,image=soft_drink_resize_image1)
    soft_drink_label_image1.pack(ipady=5)

     #First image text 1 of soft drink
    label_text16=Label(soft_drink,text="Coca-Cola",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text16.pack()

    #Creating Button 1 of soft drink
    button16=Button(soft_drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=coca)
    button16.pack(pady=2)

    #second image in soft drink
    soft_drink_image2=Image.open("D:\\Project\\photos\\Indian food\\pepsi.jfif")
    soft_drink_resize_image2=ImageTk.PhotoImage(soft_drink_image2.resize((115,65)))
    soft_drink_label_image2=Label(soft_drink,image=soft_drink_resize_image2)
    soft_drink_label_image2.pack(ipady=5)

     #second image text of soft drink
    label_text17=Label(soft_drink,text="Pepsi",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text17.pack()

    #Creating Button 2 of soft drink
    button17=Button(soft_drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=pepsi)
    button17.pack(pady=2)

    #third image in soft drink
    soft_drink_image3=Image.open("D:\\Project\\photos\\Indian food\\thumbsup.jfif")
    soft_drink_resize_image3=ImageTk.PhotoImage(soft_drink_image3.resize((115,65)))
    soft_drink_label_image3=Label(soft_drink,image=soft_drink_resize_image3)
    soft_drink_label_image3.pack(ipady=5)

     #third image text 1 of soft drink
    label_text18=Label(soft_drink,text="Thumbs Up",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text18.pack()

    #Creating Button 3 of soft drink
    button18=Button(soft_drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=thumbs)
    button18.pack(pady=2)


    #fourth image in soft drink
    soft_drink_image4=Image.open("D:\\Project\\photos\\Indian food\\sprite.jfif")
    soft_drink_resize_image4=ImageTk.PhotoImage(soft_drink_image4.resize((115,65)))
    soft_drink_label_image4=Label(soft_drink,image=soft_drink_resize_image4)
    soft_drink_label_image4.pack(ipady=5)

     #Fourth image text 1 of soft drink
    label_text19=Label(soft_drink,text="Sprite",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text19.pack()

    #Creating Button 4 of soft drink
    button19=Button(soft_drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=sprite)
    button19.pack(pady=2)

    #fifth image in soft drink
    soft_drink_image5=Image.open("D:\\Project\\photos\\Indian food\\maza.jfif")
    soft_drink_resize_image5=ImageTk.PhotoImage(soft_drink_image5.resize((115,65)))
    soft_drink_label_image5=Label(soft_drink,image=soft_drink_resize_image5 )
    soft_drink_label_image5.pack(ipady=5)

     #Fifth image text 1 of soft drink
    label_text20=Label(soft_drink,text="Maza",width=35,compound='left',fg="#EC5858",bg="#FDD998")
    label_text20.pack()

    #Creating Button 5 of soft drink
    button20=Button(soft_drink,text="Add",compound='center',width=7,bg="#FFF8CD",fg="#61B15A",command=maza)
    button20.pack(pady=2)

    #creating frame 5
    billframe=LabelFrame(root,text="Receipt",font=("Times new roman",25,"bold"),bg="#FDD998",fg="#FF7F3F")
    billframe.pack(side=LEFT,padx=7)

    #adding text area
    textreceipt=Text(billframe,font=("Times new roman",12,"bold"),bg="white",height=30)
    textreceipt.pack()

    #creating button
    button21=Button(billframe,text="Total",bg="#FDD998",fg="#FF7F3F",font=("Times new roman",15,"bold"),compound='center',command=total)
    button21.pack(side=LEFT,padx=13,pady=5)

    button22=Button(billframe,text="Receipt",bg="#FDD998",fg="#FF7F3F",font=("Times new roman",15,"bold"),compound='center',command=receipt)
    button22.pack(side=LEFT,padx=13)

    button23=Button(billframe,text="Reset",bg="#FDD998",fg="#FF7F3F",font=("Times new roman",15,"bold"),compound='center',command=reset)
    button23.pack(side=LEFT,padx=13)

    button24=Button(billframe,text="Send",bg="#FDD998",fg="#FF7F3F",font=("Times new roman",15,"bold"),compound='center',command=send)
    button24.pack(side=LEFT,padx=13)

    button25=Button(billframe,text="Back",bg="#FDD998",fg="#FF7F3F",font=("Times new roman",15,"bold"),compound='center',command=back)
    button25.pack(side=LEFT,padx=13)

    

    #Indian Food Page Mainloop
    root.mainloop()  

#creating Home Page 
root1=Tk()
root1.geometry("1300x1300+0+0")

#Add Background Image
background=Image.open("D:\\Project\\photos\\Indian food\\background.jpg")
background=ImageTk.PhotoImage(background.resize((1700,800)))
l1=Label(root1,image=background)
l1.place(x=0,y=0)

#Home Page First Frame
name_frame=Frame(root1,bg="#FFDFAF")
name_frame.pack(padx=10,pady=150)

#First Frame Text
label_text=Label(name_frame,text="What Is Your Name?",fg="#F6D860",bg="#FF7F3F",font=("Times new roman",30,"bold"),compound='center')
label_text.pack()

#First Frame Textbox
text=Entry(name_frame,width=20,font=("Times new roman",15,"bold"),bg="#C9A9A6",fg="#FF4646")
text.pack(padx=10,pady=10)

#Home Page Second Frame
food_frame=Frame(root1,bg="#FFDFAF")
food_frame.pack(pady=20)

#Second Frame Text
label_text=Label(food_frame,text="Would You Like To Eat Tonight?",fg="#F6D860",bg="#FF7F3F",font=("Times new roman",30,"bold"),compound='center')
label_text.pack()

#Indian Food Button
button1=Button(food_frame,text="Indian Food",font=("Times new roman",15,"bold"),compound='center',command=Indian_Food,fg="#FF4646",bg="#C9A9A6",width=25,height=1)
button1.pack(padx=5,pady=7)

#Chinese Food Button
button2=Button(food_frame,text="Chinese Food",font=("Times new roman",15,"bold"),compound='center',command=Chinese_Food,fg="#682C0E",bg="#C9A9A6",width=25,height=1)
button2.pack(padx=5,pady=7)

#American Food Button
button3=Button(food_frame,text="American Food",font=("Times new roman",15,"bold"),compound='center',command=American_Food,fg="#721B65",bg="#C9A9A6",width=25,height=1)
button3.pack(padx=5,pady=7)

#Italian Food Button
button4=Button(food_frame,text="Italian Food",font=("Times new roman",15,"bold"),compound='center',command=Italian_Food,fg="#5C7AEA",bg="#C9A9A6",width=25,height=1)
button4.pack(padx=5,pady=7)

button4=Button(food_frame,text="Back",font=("Times new roman",15,"bold"),compound='center',command=root1.destroy,fg="red",bg="#C9A9A6",width=25,height=1)
button4.pack(padx=5,pady=7)

#Home Page Mainloop 
root1.mainloop()