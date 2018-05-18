from tkinter import *
import pickle

discount = pickle.load(open('dicount.p','rb'))
root = Tk()
root.title('Pricing strategies')
root.geometry('900x600')

Label(root, text = 'Products eligible for giving discounts', font =('Helvetica', 15, 'bold', 'underline')).place(relx = 0.3, rely = 0)

def getprod():
    j = 1
    lis.delete(0, END)
    for i in range(len(discount)):
        lis.insert(END,'{}. {}'.format(j, discount[i]))
        j +=1

lis = Listbox(root, width = 60, height = 25)
lis.place(relx = 0.4, rely = 0.2)
    
bu = Button(root, text = 'Get Products for discount', command = getprod)
bu.place(relx = 0.1, rely = 0.2)

root.mainloop()