'''Simple Calculator Using Python Tkinter'''

'''
    function definition outside
    1. Number button
    2. Addition
    3. Subtraction
    4. Multiplication
    5. Division
    6. Percentage
    7. Power(^2)
    8. Operation
    9. Clear
'''

#1
def button_click(number):
    
    s_number=str(number)
    
    if (s_number == '.'):
        if entry_input.get().count('.') == 0:
            entry_input.insert(tk.END,str(number))
        else:
            print()

    else:
        entry_input.insert(tk.END,str(number))

#2
def perform_addtion():
    global prev,operation
    prev=float(entry_input.get())
    entry_input.delete(0,tk.END)
    operation='+'

#3
def perform_sub():
    global prev,operation
    prev=float(entry_input.get())
    entry_input.delete(0,tk.END)
    operation='-'

#4
def perform_multi():
    global prev,operation
    prev=float(entry_input.get())
    entry_input.delete(0,tk.END)
    operation='*'

#5
def perform_div():
    global prev,operation
    prev=float(entry_input.get())
    entry_input.delete(0,tk.END)
    operation='/'

#6
def perform_per():
    global prev,operation
    prev=float(entry_input.get())
    entry_input.delete(0,tk.END)
    operation='%'

#7
def perform_square():
    global prev,operation,curr
    prev=float(entry_input.get())
    curr=prev
    entry_input.delete(0,tk.END)

    result=float(prev)*float(curr)
    entry_input.insert(0,result)

#8
def equal_click():
    global curr,prev
    curr=float(entry_input.get())
    entry_input.delete(0,tk.END)

    if operation=='+':
        result=float(curr)+float(prev)
    elif operation=='-':
        result=float(prev)-float(curr)
    elif operation=='*':
        result=float(curr)*float(prev)
    elif operation=='/':
        result=float(prev)/float(curr)
    elif operation=='%':
        result=float(prev)/float(curr) * 100
    entry_input.insert(0,result)
    prev=result

#9
def aclear_click():
    entry_input.delete(0,tk.END)

#Main program starts here

'''
importing tkinter 
if method not there install using pep install tkinter
'''

import tkinter as tk

prev=0
curr=0
operation=''

#Setting screen has per computer calculator
root_window=tk.Tk()
root_window.title("Simple Calculator")
root_window.geometry('320x370')
root_window.configure(
    background='orangered' #color is  orangered u can change as per ur wish 
)

#const for padding
x=1
y=1
wi=11

root_window.resizable(width='false', height='false')

entry_input=tk.Entry(
    master=root_window,
    text=0,
    font=('Arial',40,'normal'),
    width=11
)

entry_input.grid(
    row=0,
    columnspan=4,
    padx=x,
    pady=y
)

button_1=tk.Button(
    master=root_window,
    font=('Arial',20,'normal'),
    text='x^2',
    padx=x,
    pady=y,
    command=perform_square
)

button_2=tk.Button(
    master=root_window,
    font=('Arial',20,'normal'),
    text='C',
    padx=x,
    pady=y,
    command=aclear_click
)

button_3=tk.Button(
    master=root_window,
    font=('Arial',20,'normal'),
    text='%',
    padx=x,
    pady=y,
    command=perform_per
    
)

button_4=tk.Button(
    master=root_window,
    font=('Arial',20,'normal'),
    text='/',
    padx=x,
    pady=y,
    command=perform_div
)

button_5=tk.Button(
    master=root_window,
    font=('Arial',20,'normal'),
    text='7',
    padx=x,
    pady=y,
    command=lambda:button_click(7)
)

button_6=tk.Button(
    master=root_window,
    font=('Arial',20,'normal'),
    text='8',
    padx=x,
    pady=y,
    command=lambda:button_click(8)
)

button_7=tk.Button(
    master=root_window,
    font=('Arial',20,'normal'),
    text='9',
    padx=x,
    pady=y,
    command=lambda:button_click(9)
)

button_8=tk.Button(
    master=root_window,
    font=('Arial',20,'normal'),
    text='X',
    padx=x,
    pady=y,
    command=perform_multi
)

button_9=tk.Button(
    master=root_window,
    font=('Arial',20,'normal'),
    text='4',
    padx=x,
    pady=y,
    command=lambda:button_click(4)
)

button_10=tk.Button(
    master=root_window,
    font=('Arial',20,'normal'),
    text='5',
    padx=x,
    pady=y,
    command=lambda:button_click(5)
)

button_11=tk.Button(
    master=root_window,
    font=('Arial',20,'normal'),
    text='6',
    padx=x,
    pady=y,
    command=lambda:button_click(6)
)

button_12=tk.Button(
    master=root_window,
    font=('Arial',20,'normal'),
    text='-',
    padx=x,
    pady=y,
    command=perform_sub
)

button_13=tk.Button(
    master=root_window,
    font=('Arial',20,'normal'),
    text='1',
    padx=x,
    pady=y,
    command=lambda:button_click(1)
)

button_14=tk.Button(
    master=root_window,
    font=('Arial',20,'normal'),
    text='2',
    padx=x,
    pady=y,
    command=lambda:button_click(2)
)

button_15=tk.Button(
    master=root_window,
    font=('Arial',20,'normal'),
    text='3',
    padx=x,
    pady=y,
    command=lambda:button_click(3)
)

button_16=tk.Button(
    master=root_window,
    font=('Arial',20,'normal'),
    text='+',
    padx=x,
    pady=y,
    command=perform_addtion
)

button_17=tk.Button(
    master=root_window,
    font=('Arial',20,'normal'),
    text='0',
    padx=x,
    pady=y,
    command=lambda:button_click(0)
)

button_18=tk.Button(
    master=root_window,
    font=('Arial',20,'normal'),
    text='.',
    padx=x,
    pady=y,
    command=lambda:button_click('.')
)

button_19=tk.Button(
    master=root_window,
    font=('Arial',20,'normal'),
    text='=',
    padx=x,
    pady=y,
    command=equal_click
)

button_1.grid(row=1,column=0,padx=2,pady=2)
button_2.grid(row=1,column=1,padx=2,pady=2,ipadx=wi)
button_3.grid(row=1,column=2,padx=2,pady=2,ipadx=wi)
button_4.grid(row=1,column=3,padx=2,pady=2,ipadx=wi)

button_5.grid(row=2,column=0,padx=2,pady=2,ipadx=wi)
button_6.grid(row=2,column=1,padx=2,pady=2,ipadx=wi)
button_7.grid(row=2,column=2,padx=2,pady=2,ipadx=wi)
button_8.grid(row=2,column=3,padx=2,pady=2,ipadx=wi)

button_9.grid(row=3,column=0,padx=2,pady=2,ipadx=wi)
button_10.grid(row=3,column=1,padx=2,pady=2,ipadx=wi)
button_11.grid(row=3,column=2,padx=2,pady=2,ipadx=wi)
button_12.grid(row=3,column=3,padx=2,pady=2,ipadx=wi)

button_13.grid(row=4,column=0,padx=2,pady=2,ipadx=wi)
button_14.grid(row=4,column=1,padx=2,pady=2,ipadx=wi)
button_15.grid(row=4,column=2,padx=2,pady=2,ipadx=wi)
button_16.grid(row=4,column=3,padx=2,pady=2,ipadx=wi)

button_17.grid(row=5,columnspan=2,padx=2,pady=2,ipadx=50 )
button_18.grid(row=5,column=2,padx=2,pady=2,ipadx=wi)
button_19.grid(row=5,column=3,padx=2,pady=2,ipadx=wi)


tk.mainloop()
