from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import sqlite3
import datetime
import os
import random

root = Tk()
root.title('OpenBox')
root.geometry('%dx%d+0+0' %(root.winfo_screenwidth(),root.winfo_screenheight()))

#--Login Variable
usernameVar = StringVar()
passwordVar = StringVar()

#--mainpage Variable
item = StringVar()
seller = StringVar()
customer = StringVar()
quantityVar = StringVar()
discVar = StringVar()
rateVar = 0
printlist = []

#--delete firm variable
firm = StringVar()

#--Check quantity
p_check = StringVar()

#--Product variables
product_name = StringVar()
product_qty = StringVar()
product_hsn = StringVar()
product_rate = StringVar()
product_mrp = StringVar()

#--Update Product Variables
p_name = StringVar()
p_qty = StringVar()
p_mrp = StringVar()
p_rate = StringVar()
p_hsn = StringVar()
n=q=m=r=h=0

#--Delete Product Variables
delete_name = StringVar()

#--Seller Variables
firmName = StringVar()
firmAddress = StringVar()
firmPhone = StringVar()
firmGst = StringVar()
firmOther = StringVar()

#--daat Creation
conn = sqlite3.connect('daat.db')

c = conn.cursor()

def deletecustomer():
    conn = sqlite3.connect('daat.db')
    c = conn.cursor()
    firmv = firm.get()
    sql = 'delete from cust where firmName=?'
    c.execute(sql, (firmv,))
    conn.commit()
    conn.close()
    firmname.delete(0,END)

def deletesel():
    conn = sqlite3.connect('daat.db')
    c = conn.cursor()
    firmv = firm.get()
    sql = 'delete from seller where firmName=?'
    c.execute(sql, (firmv,))
    conn.commit()
    conn.close()
    firmname.delete(0,END)

def custtodata():
    conn = sqlite3.connect('daat.db')
    c = conn.cursor()

    c.execute('create table if not exists cust(firmName text,firmAddress text,firmPhone int,firmGst text)')
    c.execute('insert into cust values(:firmName,:firmAddress,:firmPhone,:firmGst)',
        {
            'firmName' : firmName.get(),
            'firmAddress' : firmAddress.get(),
            'firmPhone' : firmPhone.get(),
            'firmGst' : firmGst.get(),
        }
        )
    conn.commit()

    nameentry.delete(0,END)
    addressentry.delete(0,END)
    phoneentry.delete(0,END)
    gstentry.delete(0,END)

    conn.close()

def sellertodata():
    conn = sqlite3.connect('daat.db')
    c = conn.cursor()

    c.execute('create table if not exists seller(firmName text,firmAddress text,firmPhone int,firmGst text,firmOther text)')
    c.execute('insert into seller values(:firmName,:firmAddress,:firmPhone,:firmGst,:firmOther)',
        {
            'firmName' : firmName.get(),
            'firmAddress' : firmAddress.get(),
            'firmPhone' : firmPhone.get(),
            'firmGst' : firmGst.get(),
            'firmOther' : firmOther.get()
        }
        )
    conn.commit()

    nameentry.delete(0,END)
    addressentry.delete(0,END)
    phoneentry.delete(0,END)
    gstentry.delete(0,END)
    otherentry.delete(0,END)

    conn.close()

def addcust():

    global nameentry
    global addressentry
    global phoneentry
    global gstentry

    sellerinfo = Toplevel(root)
    sellerinfo.geometry('500x500')
    label = Label(sellerinfo,text='Customer Information',font="Arial 40").pack()
    
    name = Label(sellerinfo, text="Firm Name").pack()
    nameentry= Entry(sellerinfo, textvariable=firmName,width = 30)
    nameentry.pack()

    address = Label(sellerinfo, text="Firm Address").pack()
    addressentry = Entry (sellerinfo, textvariable=firmAddress,width = 30)
    addressentry.pack()

    phone = Label(sellerinfo, text="Firm Phone No.").pack()
    phoneentry= Entry(sellerinfo, textvariable=firmPhone,width = 30)
    phoneentry.pack()

    gst = Label(sellerinfo, text="Firm GST No.").pack()
    gstentry= Entry(sellerinfo, textvariable=firmGst,width = 30)
    gstentry.pack()

    label = Label(sellerinfo,text=" ").pack()

    Submit=Button(sellerinfo, text="Submit",width=30, height=2,fg = 'white',bg = 'green',command = custtodata).pack()

    sellerinfo.mainloop()

def addseller():

    global nameentry
    global addressentry
    global phoneentry
    global gstentry
    global otherentry

    sellerinfo = Toplevel(root)
    sellerinfo.geometry('500x500')
    label = Label(sellerinfo,text='Seller Information',font="Arial 40").pack()
    
    name = Label(sellerinfo, text="Firm Name").pack()
    nameentry= Entry(sellerinfo, textvariable=firmName,width = 30)
    nameentry.pack()

    address = Label(sellerinfo, text="Firm Address").pack()
    addressentry = Entry (sellerinfo, textvariable=firmAddress,width = 30)
    addressentry.pack()

    phone = Label(sellerinfo, text="Firm Phone No.").pack()
    phoneentry= Entry(sellerinfo, textvariable=firmPhone,width = 30)
    phoneentry.pack()

    gst = Label(sellerinfo, text="Firm GST No.").pack()
    gstentry= Entry(sellerinfo, textvariable=firmGst,width = 30)
    gstentry.pack()

    other = Label(sellerinfo, text="Brands Name").pack()
    otherentry= Entry(sellerinfo, textvariable=firmOther,width = 30)
    otherentry.pack()

    label = Label(sellerinfo,text=" ").pack()

    Submit=Button(sellerinfo, text="Submit",width=30, height=2,fg = 'white',bg = 'green',command = sellertodata).pack()

    sellerinfo.mainloop()

def clear_screen():

    for widget in root.winfo_children():
        widget.destroy()

def logout():
    clear_screen()
    loginpage()


def deleteseller():
    global firmname
    delete = Toplevel(root)
    delete.geometry('400x200')
    label = Label(delete,text = 'Enter Firm Name to delete').pack(pady = 10)
    firmname = Entry(delete,textvariable = firm).pack()
    submit = Button(delete,text = "Submit",command=deletesel).pack(pady = 10)

def deletecust():
    global firmname
    delete = Toplevel(root)
    delete.geometry('400x200')
    label = Label(delete,text = 'Enter Firm Name to delete').pack(pady = 10)
    firmname = Entry(delete,textvariable = firm).pack()
    submit = Button(delete,text = "Submit",command=deletecustomer).pack(pady = 10)

def add():
    conn = sqlite3.connect('daat.db')
    c = conn.cursor()
    n = product_name.get()
    q = product_qty.get()
    m = product_mrp.get()
    r = product_rate.get()
    productadd.destroy()
    if(len(n)>21):
        messagebox.showerror('Length exceed','Max input length exceeded')
    else:
        c.execute('create table if not exists product(product_name text PRIMARY KEY, product_qty int, product_mrp text, product_rate text)')
        c.execute('insert into product values(:product_name, :product_qty, :product_mrp, :product_rate)',
            {
                'product_name' : n,
                'product_qty' : q,
                'product_mrp' : m,
                'product_rate' : r
            }
            )
        conn.commit()
        product_list.append(n)
        createitemselect()

    conn.close()

def addwork(event):
    add()
    product_name_entry.delete(0,END)
    product_qty_entry.delete(0,END)
    product_mrp_entry.delete(0,END)
    product_rate_entry.delete(0,END)

def addproduct():
    global productadd
    global product_name_entry
    global product_qty_entry
    global product_mrp_entry
    global product_rate_entry
    productadd = Toplevel(root)
    productadd.geometry('600x300')
    product_name_label = Label(productadd,text = 'Product Name : ')
    product_name_label.grid(row = 0,column = 1, padx = 10, pady = 10)
    product_name_entry = Entry(productadd,textvariable = product_name, width = 50)
    product_name_entry.grid(row = 0, column = 2, padx = 10, pady = 10)
    product_name_entry.focus()

    product_qty_label = Label(productadd,text = 'Product Quantity : ')
    product_qty_label.grid(row = 1,column = 1, padx = 10, pady = 10)
    product_qty_entry = Entry(productadd,textvariable = product_qty, width = 50)
    product_qty_entry.grid(row = 1, column = 2, padx = 10, pady = 10)

    product_mrp_label = Label(productadd,text = 'Product M.R.P : ')
    product_mrp_label.grid(row = 2,column = 1, padx = 10, pady = 10)
    product_mrp_entry = Entry(productadd,textvariable = product_mrp, width = 50)
    product_mrp_entry.grid(row = 2, column = 2, padx = 10, pady = 10)

    product_rate_label = Label(productadd,text = 'Product Rate : ')
    product_rate_label.grid(row = 3,column = 1, padx = 10, pady = 10)
    product_rate_entry = Entry(productadd,textvariable = product_rate, width = 50)
    product_rate_entry.grid(row = 3, column = 2, padx = 10, pady = 10)
    product_rate_entry.bind('<Return>',addwork)

    submit = Button(productadd,text = "Submit", bg = 'green', fg = 'white')
    submit.grid(row = 5, column = 2)
    submit.bind('<Button-1>',addwork)

    product_name_entry.delete(0,END)
    product_qty_entry.delete(0,END)
    product_mrp_entry.delete(0,END)
    product_rate_entry.delete(0,END)

def delete(event):
    conn = sqlite3.connect('daat.db')
    c = conn.cursor()
    namedele = delete_name.get()
    productdel.destroy()
    try:
        sql = 'delete from product where product_name = ?'
        c.execute(sql,(namedele,))
        conn.commit()
        product_list.remove(namedele)
        createitemselect()
    except:
        messagebox.showerror('Invalid Information','Product not availble')
    product_name_entry.delete(0,END)
    conn.close()

def deleteproduct():
    global productdel
    global product_name_entry
    global product
    productdel = Toplevel(root)
    productdel.geometry('400x200')
    product_name_label = Label(productdel,text = 'Product Name : ')
    product_name_label.grid(row = 0,column = 1, padx = 10, pady = 10)
    product_name_entry = Entry(productdel,textvariable = delete_name, width = 30)
    product_name_entry.grid(row = 0, column = 2, padx = 10, pady = 10)
    product_name_entry.bind('<Return>',delete)
    product_name_entry.focus()

    submit = Button(productdel,text = "Submit", bg = 'green', fg = 'white')
    submit.grid(row = 5, column = 2)
    submit.bind('<Button-1>',delete)

    product.mainloop()

def updatework(event):
    conn = sqlite3.connect('daat.db')
    c = conn.cursor()
    c.execute("update product set product_name = '%s', product_qty = '%s', product_mrp = '%s', product_rate = '%s' where product_name = '%s'"%(product_name.get(),product_qty.get(),product_mrp.get(),product_rate.get(),val))
    conn.commit()
    conn.close()
    product_list = []
    listbox_update(product)
    name.delete(0,END)
    qty.delete(0,END)
    mrp.delete(0,END)
    rate.delete(0,END)
    updatewin.destroy()

def update(event):
    global updatewin
    global name
    global qty
    global mrp
    global rate
    global val
    conn = sqlite3.connect('daat.db')
    c = conn.cursor()
    updatewin = Toplevel(root)
    updatewin.geometry('600x400')

    sql_select = 'select * from product where product_name = ?'
    val = p_name.get()
    a = c.execute(sql_select,(val,))
    for i in a:
        n = i[0]
        q = i[1]
        m = i[2]
        r = i[3]

    name = Label(updatewin,text = 'Product Name : ')
    name.grid(row = 0,column = 1, padx = 10, pady = 10)
    name = Entry(updatewin,textvariable = product_name, width = 50)
    name.grid(row = 0, column = 2, padx = 10, pady = 10)
    name.focus()

    qty = Label(updatewin,text = 'Product Quantity : ')
    qty.grid(row = 1,column = 1, padx = 10, pady = 10)
    qty = Entry(updatewin,textvariable = product_qty, width = 50)
    qty.grid(row = 1, column = 2, padx = 10, pady = 10)

    mrp = Label(updatewin,text = 'Product M.R.P : ')
    mrp.grid(row = 2,column = 1, padx = 10, pady = 10)
    mrp = Entry(updatewin,textvariable = product_mrp, width = 50)
    mrp.grid(row = 2, column = 2, padx = 10, pady = 10)

    rate = Label(updatewin,text = 'Product Rate : ')
    rate.grid(row = 3,column = 1, padx = 10, pady = 10)
    rate = Entry(updatewin,textvariable = product_rate, width = 50)
    rate.grid(row = 3, column = 2, padx = 10, pady = 10)
    rate.bind('<Return>',updatework)

    submit = Button(updatewin,text = "Update", bg = 'green', fg = 'white')
    submit.grid(row = 5, column = 2)
    submit.bind('<Button-1>',updatework)

    name.delete(0,END)
    qty.delete(0,END)
    mrp.delete(0,END)
    rate.delete(0,END)

    name.insert(0,n)
    qty.insert(0,q)
    mrp.insert(0,m)
    rate.insert(0,r)

def updateproduct():
    global updatewindow
    try:
        if updatewindow.state()=='normal':
            updatewindow.focus()
    except NameError as e:
        print(e)
        updatewindow = Toplevel(root)
        updatewindow.geometry('400x200')
        name_label = Label(updatewindow,text = 'Product Name : ')
        name_label.grid(row = 0,column = 1, padx = 10, pady = 10)
        name_entry = Entry(updatewindow,textvariable = p_name, width = 30)
        name_entry.grid(row = 0, column = 2, padx = 10, pady = 10)
        name_entry.bind('<Return>',update)
        name_entry.focus()

        submit = Button(updatewindow,text = "Submit", bg = 'green', fg = 'white')
        submit.grid(row = 5, column = 2)
        submit.bind('<Button-1>',update)

def listbox_update(data):
    # delete previous data
    listbox.delete(0, END)

    # sorting data 
    data = sorted(data, key=str.lower)

    # put new data
    for item in data:
        listbox.insert('end', item)

def on_keyrelease(event):

    # get text from entry
    value = event.widget.get()
    value = value.strip().lower()

    # get data from product_list
    if value == '':
        data = product_list
    else:
        data = []
        for item in product_list:
            if value in item.lower():
                data.append(item)                

    # update data in listbox
    listbox_update(data)
def on_select(event):
    conn = sqlite3.connect('daat.db')
    c = conn.cursor()
    it = item.get()
    quan = quantityVar.get()
    sql = 'select * from product where product_name = ?'
    a = c.execute(sql, (it,))
    for i in a:
        if(i[1]==0 or i[1]=='0' or int(quan) > i[1]):
            messagebox.showerror('Invalid Quantity','Quantity is not Availble !!')
        else:
            sql2 = 'update product set product_qty = product_qty-? where product_name = ?'
            c.execute(sql2, (quan,it))
            conn.commit()
            billsTV.insert("", 'end', text ="L1",values =(i[0],quan,i[2],i[3],'%.2f'%(float(quan)*float(i[3]))))
            appendlist = [i[0],quan,i[2],i[3],'%.2f'%(float(quan)*float(i[3]))]
            printlist.append(appendlist)
    entry.delete(0,END)
    quantityEntry.delete(0,END)
    rateLabel.configure(text = '')
    frame.destroy()
    conn.close()
    createitemselect()

def on_do(event):
    global rateLabel
    conn = sqlite3.connect('daat.db')
    c = conn.cursor()
    item = listbox.get(listbox.curselection())
    sql = 'select * from product where product_name = ?'
    a = c.execute(sql, (item,))
    for i in a:
        rateVar = i[3]
        rateLabel = Label(root, text="Rate   "+str(rateVar),font = "Arial 10")
        rateLabel.grid(row=1, column=4, pady=(10,0))
    entry.delete(0,END)
    entry.insert(0,item)
    listbox_update(product_list)

def check(event):
    conn = sqlite3.connect('daat.db')
    c = conn.cursor()
    item = listbox.get(listbox.curselection())
    sql = 'select * from product where product_name = ?'
    a = c.execute(sql, (item,))
    for i in a:
        x = i[1]
    label = Label(checkwin, text = 'Availble quantity : '+str(x), fg = 'green',font = 'Arial 15')
    label.grid(row = 3, column = 0,columnspan = 2)

def checkquan():
    global checkwin
    global entry
    global listbox
    checkwin = Toplevel(root)
    checkwin.geometry('400x200')

    label = Label(checkwin,text = 'Product name :')
    label.grid(row = 0, column = 0, padx = 10)

    fr = Frame(checkwin)
    fr.grid(row = 0, column = 1,rowspan = 3)

    entry = Entry(fr,text = item,width = 40)
    entry.pack()
    entry.focus_set()
    entry.bind('<KeyRelease>', on_keyrelease)
    
    listbox = Listbox(fr,width = 40,height = 4)
    listbox.pack(side = 'left',expand = True,padx = (15,0))
    listbox.bind('<Return>', check)
    listbox_update(product_list)

    scrol = Scrollbar(fr, orient="vertical")
    scrol.config(command=listbox.yview)
    scrol.pack(side = 'right')

    listbox.configure(yscrollcommand = scrol.set)

def optionpage():
    global optionframe
    try:
        if optionframe.state()=='normal':
            optionframe.focus()
    except NameError as e:
        optionframe = Toplevel(root)
        optionframe.geometry('600x400')

        addbutton = Button(optionframe,text = 'Add Seller',font = '15',fg="white", bg = 'green',relief = FLAT,command = addseller)
        addbutton.grid(row = 1,column = 3,ipadx=35,ipady=13,pady = 20,padx = 10)
        
        deletebutton = Button(optionframe,text = 'Delete Seller',font = '15',fg="white", bg = 'green',relief = FLAT,command = deleteseller)
        deletebutton.grid(row = 2,column = 1,ipadx=35,ipady=13,pady = 20,padx = (25,10))

        addbutton = Button(optionframe,text = 'Add Customer',font = '15',fg="white", bg = 'green',relief = FLAT,command = addcust)
        addbutton.grid(row = 1,column = 1,ipadx=25,ipady=13,pady = 20,padx = (25,10))
        
        deletebutton = Button(optionframe,text = 'Delete Customer',font = '15',fg="white", bg = 'green',relief = FLAT,command = deletecust)
        deletebutton.grid(row = 1,column = 2,ipadx=25,ipady=13,pady = 20,padx = 10)

        additem = Button(optionframe,text = 'Add Item',font = '15',fg="white", bg = 'green',relief = FLAT, command = addproduct)
        additem.grid(row = 2,column = 2,ipadx=35,ipady=13,pady = 20,padx = 10)

        deleteitem = Button(optionframe,text = 'Delete Item',font = '15',fg="white", bg = 'green',relief = FLAT,command = deleteproduct)
        deleteitem.grid(row = 2,column = 3,ipadx=35,ipady=13,pady = 20,padx = 10)

        updateitem = Button(optionframe,text = 'Update Item',font = '15',fg="white", bg = 'green',relief = FLAT,command = updateproduct)
        updateitem.grid(row = 3,column = 1,ipadx=35,ipady=13,pady = 20, padx = (25,10))

        showbil = Button(optionframe,text = 'Show Bills',font = '15',fg="white", bg = 'green',relief = FLAT )
        showbil.grid(row = 3,column = 2,ipadx=35,ipady=13,pady = 20,padx = 10)

        checkquantity = Button(optionframe,text = 'Check Quantity',font = '15',fg="white", bg = 'green',relief = FLAT, command = checkquan)
        checkquantity.grid(row = 3,column = 3,ipadx=25,ipady=13,pady = 20, padx = 10)

def createitemselect():
    global frame
    global listbox
    global entry
    global quantityEntry

    frame = Frame(root)
    frame.grid(row = 1, column = 1,padx = (10,0), pady = (20,0))

    entry = Entry(frame,textvariable = item,width = 40)
    entry.pack(pady = (10,0))
    entry.focus_set()
    entry.bind('<KeyRelease>', on_keyrelease)
    
    listbox = Listbox(frame,width = 40,height = 4)
    listbox.pack(side = 'left',expand = True,fill = 'y',padx = (15,0))
    listbox.bind('<Return>', on_do)
    listbox_update(product_list)

    scrol = Scrollbar(frame, orient="vertical")
    scrol.config(command=listbox.yview)
    scrol.pack(side = 'right',fill = 'y')

    listbox.configure(yscrollcommand = scrol.set)

    quantityLabel = Label(root, text="Quantity :",font = "Arial 10")
    quantityLabel.grid(row=1, column=2,pady=(10,0))

    quantityEntry=Entry(root, textvariable=quantityVar)
    quantityEntry.grid(row=1, column=3,pady=(10,0))
    quantityEntry.bind('<Return>',on_select)
    conn.close()

def print_bill():

    messagebox.showinfo('Generate Bill','Printing in process')
    date = str(datetime.date.today())
    time = datetime.datetime.now()
    directory = "D:/New folder/Projects/OpenBox/"+ date[:4] + '/' + date[5:7] + '/' + date[8:10] + '/'
    if not os.path.exists(directory):
        os.makedirs(directory)

    #Template Of Bill
    company = '\t\t\t\t\tEstimate\n\n'
    phone = '\t\t\t\t\t\t'+'Mob  : 7976426794'+'\n'
    sample = 'Invoice : '+str(time.strftime('%H.%M.%S'))
    dt = '\t\t\t\t\t\t\t\t\t'+'Date : '+ str(datetime.date.today())
    table_header = '------------------------------------------------------------------------'

    table_detail = '\nS.no\t'+'|'+' Products\t\t\t'+'|'+'Qty\t\t'+'|'+'M.R.P\t'+'|'+'Rate\t\t'+'|'+'Amount\n'
    final = company + table_header + sample + phone + dt + '\n' + table_header + table_detail + table_header

    #open file to write
    file_name = str(directory) + str(time.strftime('%H.%M.%S')) + '.rtf'
    f = open(file_name,'w')
    f.write(final)
    r = 1
    q = 0
    gt = 0
    for t in printlist:
        if(len(t[0])<17):
            t[0]+='\t'
        f.write('\n'+ ' '+ str(r)+'\t'+'|'+  t[0]+'\t'+'|'+  t[1]+'\t'+'\t'+'|'+  t[2]+'\t'+'\t'+'|'+ t[3]+'\t'+'\t'+'|'+ t[4])
        q+=int(t[1])
        gt+=float(t[4])
        r+=1
    f.write('\n\n'+table_header)
    f.write('\nTotal Quantity : '+ str(q) + '\t\t\t\t\t\tGrand Total : '+ str(gt) + '\n' + table_header)
    f.close()


    '''billString+="=====================Receipt=========================\n\n"
    billString+="======================================================\n"
    billString+="{:<20}{:<10}{:<15}{:<10}\ns".format("Name", "Rate", "Quantity", "Cost")
    billString+="======================================================\n"
    
   

    
    for item in itemLists:
        billString+="{:<20}{:<10}{:<15}{:<10}\n".format(item["name"],item["rate"],item["quantity"],item["cost"])

    billString+="======================================================\n"
    billString+="{:<20}{:<10}{:<15}{:<10}\n".format("Total Cost"," "," ",totalCost)

    billFile = filedialog.asksaveasfile(mode='w',defaultextension=".txt")
    if billFile is None:
        messagebox.showerror("Invalid file Name", "Please enter valid name")
    else:
        billFile.write(billString)
        billFile.close()
        
    print(billString)'''

def mainpage():

    clear_screen()

    global listbox
    global product_list
    global billsTV
    product_list = []
    conn = sqlite3.connect('daat.db')
    c = conn.cursor()
    a = c.execute('select * from product')
    for i in a:
        product_list.append(i[0])
    logoutbutton = Button(root,text = 'Options',font="Arial 15",fg="white", bg = 'green',relief = FLAT,command=optionpage,width = 12,height=2)
    logoutbutton.grid(row=0,column = 0,ipadx  = 10)
    
    label = Label(root,text = 'OpenBox Billing System',font="Arial 38",fg="white", bg = 'green',width = 35)
    label.grid(row=0,column=1,columnspan=6)
    
    logoutbutton = Button(root,text = 'Logout',font="Arial 15",fg="white", bg = 'green',relief = FLAT,command=logout,width = 12,height=2)
    logoutbutton.grid(row=0 , column=7 ,ipadx  = 10)
    
    itemLabel = Label(root, text="Select Item :",font = "Arial 10")
    itemLabel.grid(row=1, column=0, padx=(5,0),pady=(10,0))

    createitemselect()

    billLabel=Label(root, text="\n\n")
    billLabel.grid(row=2, column=1)

    billframe = Frame(root, bg = 'white')
    billframe.grid(row = 3, column = 0,columnspan = 5)

    billsTV = ttk.Treeview(billframe,selectmode = 'browse',height = 20)
    billsTV.pack(side = 'left',padx = 5)

    billsTV['columns'] = ('1','2','3','4','5')
    billsTV['show'] = 'headings'

    scrollBar = Scrollbar(billframe,command=billsTV.yview)
    scrollBar.pack(side = 'right', fill = 'y')

    billsTV.configure(yscrollcommand=scrollBar.set)

    billsTV.column("1", anchor ='c')
    billsTV.column("2", anchor ='c')
    billsTV.column("3", anchor ='c')
    billsTV.column("4", anchor ='c')
    billsTV.column("5", anchor ='c')

    billsTV.heading('1',text="Item Description")
    billsTV.heading('2',text="QTY")
    billsTV.heading('3',text="M.R.P")
    billsTV.heading('4',text="Rate")
    billsTV.heading('5',text="Amount")

    generateBill = Button(root, text="Generate Bill",width=25,height = 2, bg = 'green', fg = 'white',relief = FLAT,command = print_bill)
    generateBill.grid(row = 3, column = 6, sticky = 'se')


def adminLogin(event):
    conn = sqlite3.connect('daat.db')

    c = conn.cursor()

    c.execute('create table if not exists product(product_name text PRIMARY KEY, product_qty int, product_mrp text, product_rate text)')

    username = usernameVar.get()
    password = passwordVar.get()

    if(username == 'admin' and password == '1234'):
        userentry.delete(0,END)
        passentry.delete(0,END)
        mainpage()
    else:
        messagebox.showerror("Invalid user", "Username/Password Invalid!!")

def loginpage():

    global userentry
    global passentry

    title = Label(root,text="OpenBox Billing System",font="Arial 40",fg="white", bg = 'green')
    title.pack(ipadx = root.winfo_screenwidth())

    loginLabel = Label(root,text="Access Control",font="Arial 30").pack()

    usernameLabel = Label(root, text="Username").pack()

    userentry= Entry(root, textvariable=usernameVar,width = 30)
    userentry.pack()

    passwordLabel = Label(root, text="Password").pack()

    passentry = Entry (root, textvariable=passwordVar,show="*",width = 30)
    passentry.pack()
    passentry.bind('<Return>',adminLogin)

    label = Label(root,text=" ").pack()

    loginButton=Button(root, text="Login",width=30, height=2,fg = 'white',bg = 'green',command=adminLogin)
    loginButton.pack()
    loginButton.bind('<Button-1>',adminLogin)

loginpage()

root.mainloop() 