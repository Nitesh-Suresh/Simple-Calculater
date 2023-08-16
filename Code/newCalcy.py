import tkinter as tk

calculation = ""
history_list=[]

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,result)
        history_list.append(f"{calculation} = {result}")
        calculation = "" 

    except Exception as e:
        clear_field()
        text_result.insert(1.0,"Error")
        calculation = ""

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0,"end")

def display_history():
    history_window = tk.Toplevel(root)
    history_window.title("Calculation History")
    history_window.geometry("300x200")

    history_text = tk.Text(
        history_window,
        height=10,
        width= 30,
        font=("Arial", 12)
    )

    for history_item in history_list:
        history_text.insert("end", history_item + "\n")
    history_text.pack()

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("310x360")
root.configure(bg="#f0f0f0")

#text field
text_result=tk.Text(
    root,
    height =2,
    width=16,
    font=("Arial", 24),
    bd=5,
    relief="ridge"
)

text_result.grid(columnspan=5, pady=10)

def set_button_style(button):
    button.config(
        bd=3,  # Add a border
        relief="raised",  # Set the border style
        bg="#e0e0e0",  # Set the background color for the buttons
        activebackground="#d0d0d0",  # Set the background color when the button is pressed
        font=("Arial", 14)
    )

buttons =[
    tk.Button(
        root,
        text = "1",
        command= lambda:add_to_calculation(1),
        width= 5,
    ),

    tk.Button(
        root,
        text = "2",
        command= lambda:add_to_calculation(2),
        width= 5,
    ),

    tk.Button(
        root,
        text = "3",
        command= lambda:add_to_calculation(3),
        width= 5,
    ),

    tk.Button(
        root,
        text = "+",
        command= lambda:add_to_calculation("+"),
        width= 5,
    ), 

    tk.Button(
        root,
        text = "4",
        command= lambda:add_to_calculation(4),
        width= 5,
    ),

    tk.Button(
        root,
        text = "5",
        command= lambda:add_to_calculation(5),
        width= 5,
    ),

    tk.Button(
        root,
        text = "6",
        command= lambda:add_to_calculation(6),
        width= 5,
    ),

    tk.Button(
        root,
        text = "-",
        command= lambda:add_to_calculation("-"),
        width= 5,
    ),

    tk.Button(
        root,
        text = "7",
        command= lambda:add_to_calculation(7),
        width= 5,
    ),

    tk.Button(
        root,
        text = "8",
        command= lambda:add_to_calculation(8),
        width= 5,
    ),

    tk.Button(
        root,
        text = "9",
        command= lambda:add_to_calculation(9),
        width= 5,
    ),

    tk.Button(
        root,
        text = "*",
        command= lambda:add_to_calculation("*"),
        width= 5,
    ),

    tk.Button(
        root,
        text = "(",
        command= lambda:add_to_calculation("("),
        width= 5,
    ),

    tk.Button(
        root,
        text = "0",
        command= lambda:add_to_calculation(0),
        width= 5,
    ),

    tk.Button(
        root,
        text = ")",
        command= lambda:add_to_calculation(")"),
        width= 5,
    ),

    tk.Button(
        root,
        text = "/",
        command= lambda:add_to_calculation("/"),
        width= 5,
    ),

    tk.Button(
        root,
        text = "C",
        command= clear_field,
        width= 5,
    ),

    tk.Button(
        root,
        text = "M",
        command= display_history,
        width= 5,
    ),

    tk.Button(
        root,
        text = "=",
        command= evaluate_calculation,
        width= 5,
    )
] 

# Grid positions for buttons
button_positions = [
    (2, 1), (2, 2), (2, 3), (2, 4),
    (3, 1), (3, 2), (3, 3), (3, 4),
    (4, 1), (4, 2), (4, 3), (4, 4),
    (5, 1), (5, 2), (5, 3), (5, 4),
    (6, 1), (6, 2), (6, 3)
]

for i, button in enumerate(buttons):
    set_button_style(button)
    button.grid(
        row=button_positions[i][0], 
        column=button_positions[i][1], 
        pady=5, 
        padx=5)

root.mainloop()