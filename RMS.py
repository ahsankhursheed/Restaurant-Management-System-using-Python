from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import random  

window= Tk()
window.geometry("1366x768")
window.title("Restaurant Management System")

#Image

# pic=Image.open("your_pic.png")
# photos=ImageTk.PhotoImage(pic)
# label4=Label(image=photos,padx=0,pady=0)
# label4.place(x=0,y=0)

# Variables

chicken= IntVar()
beef=IntVar()
zinger= IntVar()
grilled= IntVar()
plain= IntVar()
masala= IntVar()
gourmet= IntVar()
cheese= IntVar()
fried=IntVar()
chicken_fried=IntVar()
singaporian=IntVar()
kabuli_pulao=IntVar()
chicken_tikka=IntVar()
malai_boti=IntVar()
seekh_kabab=IntVar()
afghani_boti=IntVar()
plain_nan=IntVar()
roghni_nan=IntVar()
garlic_nan=IntVar()
paratha=IntVar()
coke=IntVar()
sprite=IntVar()
fanta=IntVar()
sting=IntVar()

total_incl_gst= StringVar()

#Frames

Tops = Frame(window,width = 500,height=500,relief=SUNKEN)
Tops.pack()

f1 = Frame(window, background="lightcyan",bd=7,relief=SUNKEN)
f1.place(x=1,y=145, width=1105,height=410)

f2 = Frame(window, background="lightcyan",bd=7,relief=SUNKEN)
f2.place(x=1105,y=1, width=250,height=695)

f3 = Frame(f1, background="", bd=7, relief= SUNKEN)
f3.place(x=1, y= 260, width= 1093,height=60)

# Billing Receipt

txtarea=Text(f2)
txtarea.place(x=1,y=37, height= 640 , width= 238)

bill_number=StringVar()
num=random.randint(3400,9999)
bill_number.set(str(num))

#Labels

lblinfo = Label(Tops, text="RESTAURANT MANAGEMENT SYSTEM                        ",font=("georgia" ,33, 'bold'),fg="grey7",bd=10,anchor='w')
lblinfo.grid(row=5,column=3)

lb1=Label(f1, text="Billing Counter", fg="lightcyan", width=77, bg="grey7", bd=5, relief=GROOVE, font=("times new roman",18,"bold"))
lb1.place(x=1, y=1)

lba=Label(f1,text="BURGERS", fg= "black", width=12, bg="lightgreen", bd=5, relief=SUNKEN, font=("georgia",14,"bold"))
lba.place(x=1,y=39)

lbb=Label(f1,text="FRIES", fg= "black", width=12, bg="lightgreen", bd=5, relief=SUNKEN, font=("georgia",14,"bold"))
lbb.place(x=169,y=39)

lbc=Label(f1,text="RICE", fg= "black", width=16, bg="lightgreen", bd=5, relief=SUNKEN, font=("georgia",14,"bold"))
lbc.place(x=336,y=39)

lbd=Label(f1,text="BBQ", fg= "black", width=16, bg="lightgreen", bd=5, relief=SUNKEN, font=("georgia",14,"bold"))
lbd.place(x=544,y=39)

lbe=Label(f1,text="TANDOOR", fg= "black", width=14, bg="lightgreen", bd=5, relief=SUNKEN, font=("georgia",14,"bold"))
lbe.place(x=763,y=39)

lbf=Label(f1,text="DRINKS", fg= "black", width=10, bg="lightgreen", bd=5, relief=SUNKEN, font=("georgia",14,"bold"))
lbf.place(x=955,y=39)


lb1=Label(f1,text="Chicken", fg="black",bg="lightcyan", font=("serif",14, "bold"))
lb1.place(x=1, y= 105)

lb2=Label(f1, text="Beef", fg="black",bg="lightcyan", font=("serif",14, "bold"))
lb2.place(x=1, y=139)

lb3=Label(f1, text="Zinger", fg="black",bg="lightcyan", font=("serif",14, "bold"))
lb3.place(x=1, y=173)

lb4=Label(f1, text="Grilled", fg="black",bg="lightcyan", font=("serif",14, "bold"))
lb4.place(x=1, y=207)

lb4a=Label(f1, text="Plain", fg="black",bg="lightcyan", font=("serif",14, "bold"))
lb4a.place(x=170, y=105)

lb5=Label(f1, text="Masala", fg="black",bg="lightcyan", font=("serif",14, "bold"))
lb5.place(x=170, y=139)

lb6=Label(f1, text="Gourmet", fg="black",bg="lightcyan", font=("serif",14, "bold"))
lb6.place(x=170, y=173)

lb8=Label(f1, text="Cheese", fg="black",bg="lightcyan", font=("serif",14, "bold"))
lb8.place(x=170, y=207)

lb9=Label(f1, text="Fried", fg="black",bg="lightcyan", font=("serif",14, "bold"))
lb9.place(x=336, y=105)

lb10=Label(f1, text="Chicken Fried", fg="black",bg="lightcyan", font=("serif",14, "bold"))
lb10.place(x=336, y=139)

lb11=Label(f1, text="Singaporian", fg="black",bg="lightcyan", font=("serif",14, "bold"))
lb11.place(x=336, y=173)

lb12=Label(f1, text="Kabuli Pulao", fg="black",bg="lightcyan", font=("serif",14, "bold"))
lb12.place(x=336, y=207)

lb7=Label(f1, text="Chicken Tikka", fg="black",bg="lightcyan", font=("serif",14, "bold"))
lb7.place(x=548, y=105)

lb7=Label(f1, text="Malai Boti", fg="black",bg="lightcyan", font=("serif",14, "bold"))
lb7.place(x=548, y=139)

lb7=Label(f1, text="Seekh Kabab", fg="black",bg="lightcyan", font=("serif",14, "bold"))
lb7.place(x=548, y=173)

lb7=Label(f1, text="Afghani Boti", fg="black",bg="lightcyan", font=("serif",14, "bold"))
lb7.place(x=548, y=207)

lb7=Label(f1, text="Plain Nan", fg="black",bg="lightcyan", font=("serif",14, "bold"))
lb7.place(x=765, y=105)

lb7=Label(f1, text="Roghni Nan", fg="black",bg="lightcyan", font=("serif",14, "bold"))
lb7.place(x=765, y=139)

lb7=Label(f1, text="Garlic Nan", fg="black",bg="lightcyan", font=("serif",14, "bold"))
lb7.place(x=765, y=173)

lb7=Label(f1, text="Paratha", fg="black",bg="lightcyan", font=("serif",14, "bold"))
lb7.place(x=765, y=207)

lb7=Label(f1, text="Coke", fg="black",bg="lightcyan", font=("serif",14, "bold"))
lb7.place(x=956, y=105)

lb7=Label(f1, text="Sprite", fg="black",bg="lightcyan", font=("serif",14, "bold"))
lb7.place(x=956, y=139)

lb7=Label(f1, text="Fanta", fg="black",bg="lightcyan", font=("serif",14, "bold"))
lb7.place(x=956, y=173)

lb7=Label(f1, text="Sting", fg="black",bg="lightcyan", font=("serif",14, "bold"))
lb7.place(x=956, y=207)

lb13=Label(f3, text="TOTAL incl. GST",fg="black",bg="lightgreen", font=("serif",18, "bold"))
lb13.place(x=435,y= 5)

lb14=Label(f2, text="Billing Receipt", fg="lightcyan", width=16, bg="grey7", bd=5, relief=GROOVE, font=("times new roman",18,"bold"))
lb14.place(x=1, y=1)

# Entry

entry=Entry(f1, textvariable=chicken, width=10, bd=5, relief=SUNKEN)
entry.place(x=86, y=105)

entry_1=Entry(f1, textvariable=beef , width=10, bd=5, relief=SUNKEN)
entry_1.place(x=86,y=139)

entry_2=Entry(f1, textvariable=zinger, width=10, bd=5, relief=SUNKEN)
entry_2.place(x=86,y=173)

entry_3=Entry(f1, textvariable=grilled, width=10, bd=5, relief=SUNKEN)
entry_3.place(x=86,y=207)

entry_4=Entry(f1, textvariable=plain, width=10, bd=5, relief=SUNKEN)
entry_4.place(x=262,y=105)

entry_5=Entry(f1, textvariable=masala, width=10, bd=5, relief=SUNKEN)
entry_5.place(x=262,y=139)

entry_6=Entry(f1, textvariable=gourmet, width=10, bd=5, relief=SUNKEN)
entry_6.place(x=262,y=173)

entry_7=Entry(f1, textvariable=cheese, width=10, bd=5, relief=SUNKEN)
entry_7.place(x=262,y=207)

entry_8=Entry(f1, textvariable=fried, width=10, bd=5, relief=SUNKEN)
entry_8.place(x=472,y=105)

entry_9=Entry(f1, textvariable=chicken_fried, width=10, bd=5, relief=SUNKEN)
entry_9.place(x=472,y=139)

entry_10=Entry(f1, textvariable=singaporian, width=10, bd=5, relief=SUNKEN)
entry_10.place(x=472,y=173)

entry_11=Entry(f1, textvariable=kabuli_pulao, width=10, bd=5, relief=SUNKEN)
entry_11.place(x=472,y=207)

entry_12=Entry(f1, textvariable=chicken_tikka, width=10, bd=5, relief=SUNKEN)
entry_12.place(x=685,y=105)

entry_13=Entry(f1, textvariable=malai_boti, width=10, bd=5, relief=SUNKEN)
entry_13.place(x=685,y=139)

entry_14=Entry(f1, textvariable=seekh_kabab, width=10, bd=5, relief=SUNKEN)
entry_14.place(x=685,y=173)

entry_15=Entry(f1, textvariable=afghani_boti, width=10, bd=5, relief=SUNKEN)
entry_15.place(x=685,y=207)

entry_16=Entry(f1, textvariable=plain_nan, width=10, bd=5, relief=SUNKEN)
entry_16.place(x=880,y=105)

entry_17=Entry(f1, textvariable=roghni_nan, width=10, bd=5, relief=SUNKEN)
entry_17.place(x=880,y=139)

entry_18=Entry(f1, textvariable=garlic_nan, width=10, bd=5, relief=SUNKEN)
entry_18.place(x=880,y=173)

entry_19=Entry(f1, textvariable=paratha, width=10, bd=5, relief=SUNKEN)
entry_19.place(x=880,y=207)

entry_20=Entry(f1, textvariable=coke, width=10, bd=5, relief=SUNKEN)
entry_20.place(x=1017,y=105)

entry_21=Entry(f1, textvariable=sprite, width=10, bd=5, relief=SUNKEN)
entry_21.place(x=1017,y=139)

entry_22=Entry(f1, textvariable=fanta, width=10, bd=5, relief=SUNKEN)
entry_22.place(x=1017,y=173)

entry_23=Entry(f1, textvariable=sting, width=10, bd=5, relief=SUNKEN)
entry_23.place(x=1017,y=207)

entry_24=Entry(f3, textvariable=total_incl_gst, bd=6, relief=SUNKEN)
entry_24.place(x=650,y=5, height=38, width=160 )

# Functions

def exit():
    
    a=messagebox.askyesno("Exit", "Are you sure you want to exit ?")
    if a>0:
        window.destroy()
    else:
        return
        
def reset():
    
    chicken.set(0)
    beef.set(0)
    zinger.set(0)
    grilled.set(0)
    plain.set(0)
    masala.set(0)
    gourmet.set(0)
    cheese.set(0)
    fried.set(0)
    chicken_fried.set(0)
    singaporian.set(0)
    kabuli_pulao.set(0)
    chicken_tikka.set(0)
    malai_boti.set(0)
    seekh_kabab.set(0)
    afghani_boti.set(0)
    plain_nan.set(0)
    roghni_nan.set(0)
    garlic_nan.set(0)
    paratha.set(0)
    coke.set(0)
    sprite.set(0)
    fanta.set(0)
    sting.set(0)
    
    total_incl_gst.set("")
    bill_number.set("")
    num=random.randint(3400,9999)
    bill_number.set(str(num))
    welcome()
    
def total():
    
    price_chicken       = chicken.get()* 200
    price_beef          = beef.get()* 180
    price_zinger        = zinger.get()* 220
    price_grilled       = grilled.get()* 260
    price_plain         = plain.get()* 120
    price_masala        = masala.get()* 140
    price_gourmet       = gourmet.get()* 180
    price_cheese        = cheese.get()* 170
    price_fried         = fried.get()* 180
    price_chicken_fried = chicken_fried.get()* 220
    price_singaporian   = singaporian.get()* 250
    price_kabuli_pulao  = kabuli_pulao.get()* 260
    price_chicken_tikka = chicken_tikka.get()* 200
    price_malai_boti    = malai_boti.get()* 190
    price_seekh_kabab   = seekh_kabab.get()* 170
    price_afghani_boti  = afghani_boti.get()* 170
    price_plain_nan     = plain_nan.get()* 20
    price_roghni_nan    = roghni_nan.get()* 35
    price_garlic_nan    = garlic_nan.get()* 30
    price_paratha       = paratha.get()* 25
    price_coke          = coke.get()* 65
    price_sprite        = sprite.get()* 65
    price_fanta         = fanta.get()* 65
    price_sting         = sting.get()* 65
    

    price_total= (price_chicken + price_beef + price_zinger + price_grilled + price_plain + price_masala 
                  + price_gourmet + price_cheese + price_fried + price_chicken_fried + price_singaporian + price_kabuli_pulao
                  + price_chicken_tikka + price_malai_boti + price_seekh_kabab + price_afghani_boti 
                  + price_plain_nan + price_roghni_nan + price_garlic_nan + price_paratha 
                  + price_coke + price_sprite + price_fanta + price_sting)
    
    price_total_gst= str(price_total + (price_total*(13/100)or(12/100)or(11/100)))
    
    total_incl_gst.set("Rs. " + str(price_total_gst))
    
def welcome():
    
    txtarea.delete("1.0",END)
    txtarea.insert(END, "\t  |RECEIPT|\n=============================\n   'Food Mania Restaurant'\n=============================")
    txtarea.insert(END,f"\n Bill Number : {bill_number.get()} \n Applied GST Rate : Custom")
    txtarea.insert(END, "\n-----------------------------\nProducts\t     Qty\t      Price\n-----------------------------")
    
def bill():
    
    welcome()
    
    
    price_chicken       = chicken.get()* 200
    price_beef          = beef.get()* 180
    price_zinger        = zinger.get()* 220
    price_grilled       = grilled.get()* 260
    price_plain         = plain.get()* 120
    price_masala        = masala.get()* 140
    price_gourmet       = gourmet.get()* 180
    price_cheese        = cheese.get()* 170
    price_fried         = fried.get()* 180
    price_chicken_fried = chicken_fried.get()* 220
    price_singaporian   = singaporian.get()* 250
    price_kabuli_pulao  = kabuli_pulao.get()* 260
    price_chicken_tikka = chicken_tikka.get()* 200
    price_malai_boti    = malai_boti.get()* 190
    price_seekh_kabab   = seekh_kabab.get()* 170
    price_afghani_boti  = afghani_boti.get()* 170
    price_plain_nan     = plain_nan.get()* 20
    price_roghni_nan    = roghni_nan.get()* 35
    price_garlic_nan    = garlic_nan.get()* 30
    price_paratha       = paratha.get()* 25
    price_coke          = coke.get()* 65
    price_sprite        = sprite.get()* 65
    price_fanta         = fanta.get()* 65
    price_sting         = sting.get()* 65
    

    price_total= (price_chicken + price_beef + price_zinger + price_grilled + price_plain + price_masala 
                  + price_gourmet + price_cheese + price_fried + price_chicken_fried + price_singaporian + price_kabuli_pulao
                  + price_chicken_tikka + price_malai_boti + price_seekh_kabab + price_afghani_boti 
                  + price_plain_nan + price_roghni_nan + price_garlic_nan + price_paratha 
                  + price_coke + price_sprite + price_fanta + price_sting)
    
    price_total_gst= str(price_total + (price_total*(13/100)or(12/100)or(11/100)))
    
    total_incl_gst.set("Rs. " + str(price_total_gst))
    
    if chicken.get()!=0:
        txtarea.insert(END,"\nChicken Burger\t {}\t       {}".format(chicken.get(),price_chicken))
    
    if beef.get()!=0:
        txtarea.insert(END,"\nBeef Burger\t    {}\t       {}".format(beef.get(),price_beef))
    
    if zinger.get()!=0:
        txtarea.insert(END,"\nZinger Burger\t  {}\t       {}".format(zinger.get(),price_zinger))
        
    if grilled.get()!=0:
        txtarea.insert(END,"\nGrilled Burger\t {}\t       {}".format(grilled.get(),price_grilled))
    
    if plain.get()!=0:
        txtarea.insert(END,"\nPlain Fries\t    {}\t       {}".format(plain.get(),price_plain))
    
    if masala.get()!=0:
        txtarea.insert(END,"\nMasala Fries\t   {}\t       {}".format(masala.get(),price_masala))
        
    if gourmet.get()!=0:
        txtarea.insert(END,"\nGourmet Fries\t  {}\t       {}".format(gourmet.get(),price_gourmet))
        
    if cheese.get()!=0:
        txtarea.insert(END,"\nCheese Fries\t   {}\t       {}".format(cheese.get(),price_cheese))
        
    if fried.get()!=0:
        txtarea.insert(END,"\nFried Rice\t     {}\t       {}".format(fried.get(),price_fried))
        
    if chicken_fried.get()!=0:
        txtarea.insert(END,"\nFried Rice(Ck) \t{}\t       {}".format(chicken_fried.get(),price_chicken_fried))
        
    if singaporian.get()!=0:
        txtarea.insert(END,"\nSingaporian\t    {}\t       {}".format(singaporian.get(),price_singaporian))
        
    if kabuli_pulao.get()!=0:
        txtarea.insert(END,"\nKabuli Pulao\t   {}\t       {}".format(kabuli_pulao.get(),price_kabuli_pulao))
        
    if chicken_tikka.get()!=0:
        txtarea.insert(END,"\nChicken Tikka\t  {}\t       {}".format(chicken_tikka.get(),price_chicken_tikka))
        
    if malai_boti.get()!=0:
        txtarea.insert(END,"\nMalai Boti\t     {}\t       {}".format(malai_boti.get(),price_malai_boti))
        
    if seekh_kabab.get()!=0:
        txtarea.insert(END,"\nSeekh Kabab\t    {}\t       {}".format(seekh_kabab.get(),price_seekh_kabab))
        
    if afghani_boti.get()!=0:
        txtarea.insert(END,"\nAfghani Boti\t   {}\t       {}".format(afghani_boti.get(),price_afghani_boti))
        
    if plain_nan.get()!=0:
        txtarea.insert(END,"\nPlain Nan\t      {}\t       {}".format(plain_nan.get(),price_plain_nan))
        
    if roghni_nan.get()!=0:
        txtarea.insert(END,"\nRoghni Nan\t     {}\t       {}".format(roghni_nan.get(),price_roghni_nan))
        
    if garlic_nan.get()!=0:
        txtarea.insert(END,"\nGarlic Nan\t     {}\t       {}".format(garlic_nan.get(),price_garlic_nan))
        
    if paratha.get()!=0:
        txtarea.insert(END,"\nParatha\t        {}\t       {}".format(paratha.get(),price_paratha))
        
    if coke.get()!=0:
        txtarea.insert(END,"\nCoke\t        {}\t       {}".format(coke.get(),price_coke))
        
    if sprite.get()!=0:
        txtarea.insert(END,"\nSprite\t        {}\t       {}".format(sprite.get(),price_sprite))
        
    if fanta.get()!=0:
        txtarea.insert(END,"\nFanta\t        {}\t       {}".format(fanta.get(),price_fanta))
    
    if sting.get()!=0:
        txtarea.insert(END,"\nSting\t        {}\t       {}".format(sting.get(),price_sting))
        
    txtarea.insert(END,"\n-----------------------------\n Total Incl. GST: {}".format(total_incl_gst.get()))
    txtarea.insert(END, "\n-----------------------------   THANK YOU, VISIT US AGAIN!")
    
    filing()
    
def filing():
    
    a=messagebox.askyesno("Save Bill", "Do you want to save the billing information ?")
    if a>0:
        bill_data= txtarea.get("1.0",END)
        infile=open("C:\\Users\\ahsan\\Desktop\\Restaurant Management System\\bills/"+str(bill_number.get())+" .txt","w")
        infile.write(bill_data)
        infile.close()
    else:
        return
    

    
# Buttons

total_btn=Button(f1, text="TOTAL" , command = total, font=("georgia",12,"bold"),height=3,width=24,bg="grey6",fg="lightcyan",bd=5,relief=SUNKEN)
total_btn.place(x=1,y=321)

gt_btn=Button(f1, text="GENERATE  BILL", command= bill , font=("georgia",12,"bold"),height=3,width=24,bg="grey6",fg="lightcyan",bd=5,relief=SUNKEN)
gt_btn.place(x=277,y=321)

reset_btn=Button(f1, text="RESET",command= reset, font=("georgia",12,"bold"),height=3,width=24,bg="grey6",fg="lightcyan",bd=5,relief=SUNKEN)
reset_btn.place(x=555,y=321)

exit_btn=Button(f1, text="EXIT",font=("georgia",12,"bold"),height=3,width=23,bg="grey6",fg="lightcyan",bd=5,relief=SUNKEN, command=exit)
exit_btn.place(x=825,y=321)

welcome()

window.mainloop()