from tkinter import *

root = Tk()
root.geometry("900x600")
frame = Frame(root, width=20, height=50, background="#b22222")
frame.place(relx = 0.7, rely = 0.1)
frame1 = Frame(root, width=20, height=50, background="#b22222")
frame1.place(relx = 0.7, rely = 0.13)

cont = ['col1', 'col2', 'col3', 'col4']
rows = []
for i in range(1):
    cols = []
    for j in range(4):
        e = Entry(frame, relief=RIDGE, width = 10, exportselection=0, bg = 'black')
        e.grid(row=i, column=j, sticky=NSEW)
        e.insert(END, cont[j])
        cols.append(e)
        e.configure(state='readonly')
    rows.append(cols)

rows = []
for i in range(30):
    cols = []
    for j in range(4):
        e = Entry(frame1, relief=RIDGE, width = 10, exportselection=0, bg = 'black')
        e.grid(row=i, column=j, sticky=NSEW)
        e.insert(END, '%d %d' % (i, j))
        cols.append(e)
        e.configure(state='readonly')
    rows.append(cols)

root.mainloop()
