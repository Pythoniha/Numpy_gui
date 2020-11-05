import tkinter as tk
import numpy as np
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

# array Create
zz = np.zeros((3,3))
ones = np.ones((3,3))
emptys = np.empty((3,3))
# zz = np.array_str(zz)


# Style GUI Base
root = Tk()
root.title('Numpy GUI')
root.geometry("800x600")
root.resizable(False,False)


def zzz():
    global a
    a = tk.Label(root, text=zz).place(x=150 ,y=300) 
    return a
    print(a,zz)

def one():
    one = tk.Label(root,text=ones).place(x=150,y=300)

def empty():
    empty = tk.Label(root,text=emptys).place(x=150,y=300)
    
def send():
    sendx = modx.get()
    sendy = mody.get()
    array_input = np.zeros((int(sendx),int(sendy)))
    print(array_input)
    
def range_():
    pass
    
def linspace():
    pass
    
def full():
    pass
    
def eye():
    pass
    
def eye():
    pass
    
    
def random():
    pass

    
def empty():
    pass

def open_file():
    filename = filedialog.askopenfile()
    
def debug():
    from tkinter import messagebox
    messagebox.showinfo( title = 'Debug Mode', message = 'Entering Debug Has Been Trun On!' )

    
    
tk.LabelFrame(root,text='Creat Array').pack(fill='both',expand='yes')
# Butten Create Array
b_zero = tk.Button(root,text='Array Zero ',command= zzz)
b_one = tk.Button(root,text='Array One', command = one)
b_range = tk.Button(root,text='Range', command = range_)
b_linspace = tk.Button(root,text='linSpace', command = linspace)
b_full = tk.Button(root,text='full', command = full)
b_eye = tk.Button(root,text='eye', command = eye)
b_random = tk.Button(root,text='Random', command = random)
b_empty = tk.Button(root,text='Empty', command = empty)             
b_array_one = tk.Button(root,text='1D Array')
b_array_two = tk.Button(root,text='2D Array')
b_array_three = tk.Button(root,text='3D Array')

#Button Open File
b_open_file = tk.Button(root, text='Open File',command=open_file) 
b_open_file_csv = tk.Button(root,text='Open csv')


b_save_file = tk.Button(root,text='Save File')
b_save_file_csv = tk.Button(root,text='save Csv File')

# number1 = tk.intVar()
# number2 = tk.intngVar()
# Entry : 
tk.Label(root, text='Array X : ').place(x=1,y=15) # Label
tk.Label(root, text='Array Y : ').place(x=1,y=50) # Label
modx = tk.Entry(root)
mody = tk.Entry(root)
tk.Button(root, text='Sumbit',command=send).place(x=10,y=90)


# entry Text :



# Set Menu


# Atomatic Debug[..:: AI Method ::..]
tk.Button(root,text='Debug',command=debug).pack()


# Set Button
b_zero.place(x=700,y=10)
b_one.place(x=700,y=30)
b_range.place(x=700,y=60)
b_linspace.place(x=700,y=90)
b_full.place(x=700,y=120)
b_random.place(x=700,y=150)
b_empty.place(x=700,y=180)
b_array_one.place(x=700,y=210)
b_array_two.place(x=700,y=240)
b_array_three.place(x=700,y=270)

# Save Button
b_open_file.place(x=200,y=30)
b_open_file_csv.place(x=200,y=60)
b_save_file.place(x=200,y=90)
b_save_file_csv.place(x=200,y=120)

modx.place(x=1,y=35)
mody.place(x=1,y=70)
#Text = 

# Menu
menubar = Menu(root) 
file = Menu(root , tearoff=0)  
file.add_command(label="Open File")  
file.add_command(label="Open File Csv") 
file.add_separator()
file.add_command(label="Save")
file.add_command(label="SaveFile as")
file.add_separator()
file.add_command(label="Exit",command= root.destroy)


menubar.add_cascade(label="File", menu=file)

edit = Menu(root , tearoff=0)  
edit.add_command(label="PLT")  
edit.add_command(label="Show MatplotLib")
edit.add_separator()
edit.add_command(label="PLT")  
edit.add_command(label="Show MatplotLib")

menubar.add_cascade(label="Edit", menu=edit)


Setting = Menu(root , tearoff=0)  
Setting.add_command(label="Views")  
Setting.add_command(label="License")
Setting.add_separator()
Setting.add_command(label="Dark Theme")  
Setting.add_command(label="Font Setting's")
Setting.add_separator()

menubar.add_cascade(label="Setting", menu=Setting)

about = Menu(root , tearoff=0)  
 
about.add_command(label="Lincense")
about.add_separator()
about.add_command(label="Help")  
about.add_command(label="Document")
about.add_separator()
about.add_command(label="About") 

menubar.add_cascade(label="about", menu=about)


# Loop Run
root.config(menu=menubar)

root.mainloop()
