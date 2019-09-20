#Employee Record System 
from tkinter import*

from tkinter import messagebox

products = []
root=Tk()                               #Main window
f=Frame(root)
frame1=Frame(root)
frame2=Frame(root)
frame3=Frame(root)
root.title("Simple Employee Record System")
root.geometry("830x400")
root.configure(background="Black")
color = "Brown"
index = 0
root["bg"] ="#11998e"
class Product:
    def __init__(self, firstname, lastname, position,department):
        self.firstname = firstname
        self.lastname = lastname
        self.position = position
        self.department = department

    def getFirstname(self):
        return self.firstname

    def getLastname(self):
        return self.lastname

    def getPosition(self):
        return self.position
    def getDepartment(self):
        return self.department

    def updateSelf(self, firstname, lastname, position,department ):
        self.firstname = firstname
        self.lastname = lastname
        self.position = position
        self.department = department

        btn1['state'] = DISABLED
        btn2['state'] = NORMAL
        viewProducts()
        Update()
        messagebox.showinfo("Info", "Data Successfully Updated")

def addProduct():
    global products,index
    index += 1
    product = Product(e1.get(), e2.get(), e3.get(),e4.get())
    products.append(product)
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')
    e4.delete(0, 'end')
    messagebox.showinfo("Info","Data Successfully Added")

def deleteProduct(product):
    global products
    products.remove(product)
    viewProducts()
    messagebox.showinfo("Info", "Data Has Been Deleted")


def updateProduct(product):
    en1.delete(0, 'end')
    en2.delete(0, 'end')
    en3.delete(0, 'end')
    en4.delete(0,'end')
    en1.insert(0, product.getFirstname())
    en2.insert(0, product.getLastname())
    en3.insert(0, product.getPosition())
    en4.insert(0, product.getDepartment())
    btn1['state'] = NORMAL
    btn1.configure(command=lambda: product.updateSelf(en1.get(), en2.get(), en3.get(),en4.get()))


def add_info():
    clear_all()
    global e1, e2, e3,e4, btn1, btn2
    Label(frame1, text="Employee Information",background = "Brown",relief=RIDGE,fg="white").grid(row=0, column=0, sticky=W, padx=10, pady=5)
    Label(frame1, text="First Name: ",background = "Brown",relief=RIDGE,fg="white").grid(row=1, column=0, sticky=W, padx=10, pady=5)
    Label(frame1, text="Last Name: ",background = "Brown",relief=RIDGE,fg="white").grid(row=2, column=0, sticky=W, padx=10, pady=5)
    Label(frame1, text="Position: ",background = "Brown",relief=RIDGE,fg="white").grid(row=3, column=0, sticky=W, padx=10, pady=5)
    Label(frame1, text="Department: ",background = "Brown",relief=RIDGE,fg="white").grid(row=4, column=0, sticky=W, padx=10, pady=5)

    btn2 = Button(frame1, text="Add Product",background = "Brown", width=15, state=NORMAL,command=addProduct,fg="white" )
    btn2.grid(row=6, column=2, pady=10)


    e1 = Entry(frame1, width=45)
    e2 = Entry(frame1, width=45)
    e3 = Entry(frame1, width=45)
    e4 = Entry(frame1, width=45)

    e1.grid(row=1, column=1, sticky=W, padx=10, pady=5, columnspan=2)
    e2.grid(row=2, column=1, sticky=W, padx=10, pady=5, columnspan=2)
    e3.grid(row=3, column=1, sticky=W, padx=10, pady=5, columnspan=2)
    e4.grid(row=4, column=1, sticky=W, padx=10, pady=5, columnspan=2)
    e1.focus()
    e2.focus()
    e3.focus()
    e4.focus()

    frame1.configure(background="Brown")
    frame1.grid(pady=10)

def viewProducts():
    global products
    row = 1
    list = separator.grid_slaves()
    for l in list:
        l.destroy()

    addHeaders()
    for product in products:
        Label(separator, text=product.getFirstname(), background=color, width=10,fg="white").grid(row=row, column=0,
                                                                                  sticky=W + E + N + S, padx=10, pady=5)
        Label(separator, text=product.getLastname(), background=color, width=10,fg="white").grid(row=row, column=1,
                                                                                  sticky=W + E + N + S, padx=10, pady=5)
        Label(separator, text=product.getPosition(), background=color, width=10,fg="white").grid(row=row, column=2,
                                                                                   sticky=W + E + N + S, padx=10,pady=5)
        Label(separator, text=product.getDepartment(), background=color, width=10,fg="white").grid(row=row, column=3,
                                                                                      sticky=W + E + N + S, padx=10,
                                                                                      pady=5)
        btn_a2 = Button(separator, text="Delete", width=12,command=lambda prod=product: deleteProduct(prod),background=color,fg="white")
        btn_a2.grid(row=row, column=5, sticky=E, padx=5, pady=5)

        row += 1


def addHeaders():
    frame1.grid_forget()
    frame3.grid_forget()
    separator.grid(row=5, column=0, columnspan=5, pady=5, sticky=W + E + N + S)
    Label(frame2, text="FirstName", background=color, width=10,fg="white").grid(row=0, column=0, sticky=W, padx=10, pady=5)
    Label(frame2, text="LastName", background=color, width=10,fg="white").grid(row=0, column=1, sticky=W, padx=10, pady=5)
    Label(frame2,text="Position", background=color, width=10,fg="white").grid(row=0, column=2, sticky=W, padx=10, pady=5)
    Label(frame2, text="Department", background=color, width=10,fg="white").grid(row=0, column=3, sticky=W, padx=10, pady=5)
    Label(frame2,text="Action", background=color, width=10,fg="white").grid(row=0, column=4, sticky=W, padx=10, pady=5,columnspan=2)
    frame2.configure(background="Brown")
    frame2.grid(pady=10)

def viewUpdate():
    global products
    row = 1
    list = separators.grid_slaves()
    for l in list:
        l.destroy()

    adddata()
    for product in products:
        global btna1
        Label(separators, text=product.getFirstname(), background=color, width=10,fg="white").grid(row=row, column=0,
                                                                                  sticky=W + E + N + S, padx=10, pady=5)
        Label(separators, text=product.getLastname(), background=color, width=10,fg="white").grid(row=row, column=1,
                                                                                  sticky=W + E + N + S, padx=10, pady=5)
        Label(separators, text=product.getPosition(), background=color, width=10,fg="white").grid(row=row, column=2,
                                                                                   sticky=W + E + N + S, padx=10,                                                                              pady=5)
        Label(separators, text=product.getDepartment(), background=color, width=10,fg="white").grid(row=row, column=3,
                                                                                      sticky=W + E + N + S, padx=10,
                                                                                      pady=5)
        btna1 = Button(separators, text="Update", width=7, command=lambda prod=product: updateProduct(prod),fg="white", background=color)
        btna1.grid(row=row, column=4, sticky=E, padx=5, pady=5)
        row += 1

    en1.delete(0, 'end')
    en2.delete(0, 'end')
    en3.delete(0, 'end')
    en4.delete(0, 'end')

def adddata():
    separators.grid(row=5, column=0, columnspan=5, pady=5, sticky=W + E + N + S)
    Label(separators, text="FirstName", background=color, width=10,fg="white").grid(row=0, column=0, sticky=W, padx=10, pady=5)
    Label(separators, text="LastName", background=color, width=10,fg="white").grid(row=0, column=1, sticky=W, padx=10, pady=5)
    Label(separators, text="Position", background=color, width=10,fg="white").grid(row=0, column=2, sticky=W, padx=10, pady=5)
    Label(separators, text="Department", background=color, width=10,fg="white").grid(row=0, column=3, sticky=W, padx=10, pady=5)
    Label(separators, text="Action", background=color, width=10,fg="white").grid(row=0, column=4, sticky=W, padx=10, pady=5,columnspan=2)
    frame3.configure(background="Brown")
    frame3.grid(pady=10)


def Update():
    frame1.grid_forget()
    frame2.grid_forget()
    global en1, en2, en3, en4, btn1
    Label(frame3, text="First Name: ",background=color,fg="white").grid(row=1, column=0, sticky=W, padx=10, pady=5)
    Label(frame3, text="Last Name: ",background=color,fg="white").grid(row=2, column=0, sticky=W, padx=10, pady=5)
    Label(frame3, text="Position: ",background=color,fg="white").grid(row=3, column=0, sticky=W, padx=10, pady=5)
    Label(frame3, text="Department: ",background=color,fg="white").grid(row=4, column=0, sticky=W, padx=10, pady=5)
    btn1 = Button(frame3, text="Update Product", width=15, state=DISABLED,background=color,fg="white")
    btn1.grid(row=5, column=5, pady=10)

    en1 = Entry(frame3, width=45)
    en2 = Entry(frame3, width=45)
    en3 = Entry(frame3, width=45)
    en4 = Entry(frame3, width=45)

    en1.grid(row=1, column=1, sticky=W, padx=10, pady=5, columnspan=2)
    en2.grid(row=2, column=1, sticky=W, padx=10, pady=5, columnspan=2)
    en3.grid(row=3, column=1, sticky=W, padx=10, pady=5, columnspan=2)
    en4.grid(row=4, column=1, sticky=W, padx=10, pady=5, columnspan=2)
    frame3.configure(background="Brown")
    frame3.grid(pady=10)
    viewUpdate()




def clear_all():             #for clearing the entry widgets
    frame1.grid_forget()
    frame2.grid_forget()
    frame3.grid_forget()



#Main window buttons and labels

label1=Label(root,text="EMPLOYEE RECORD SYSTEM")
label1.config(font=('Italic',16,'bold'), justify=CENTER, background="Orange",fg="Yellow", anchor="center", width= 65)
label1.grid(row=0, sticky=E)

label2=Label(f,text="Select an action: ",font=('bold',12), background="#11998e", fg="White")
label2.grid(row=1, column=1, padx=10)
button1=Button(f,text="Create", background="Brown", fg="White", command=add_info, width=15)
button1.grid(row=1, column=2, padx=10)
button2=Button(f,text="Delete", background="Brown", fg="White", command=viewProducts, width=15)
button2.grid(row=1, column=3, padx=10)
button3=Button(f,text="Update", background="Brown", fg="White", command=Update, width=15)
button3.grid(row=1, column=4, padx=10)
button4=Button(f,text="Exit", background="Brown", fg="White", width=15, command=root.destroy)
button4.grid(row=1, column=5, padx=10)
f.configure(background="#11998e")
f.grid()
global separator,separators
separator = Canvas(frame2, height=800, width=420, background=color, relief=SUNKEN)
separators = Canvas(frame3, height=800, width=420, background=color, relief=SUNKEN)

root.mainloop()
