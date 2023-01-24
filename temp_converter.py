# Import modules from standard library
import tkinter as tk
from tkinter import ttk


# Function. Clear input fields and set to a '0'
def set_text(ent, text):
    ent.delete(0, tk.END)
    ent.insert(0, text)
    return

# Function. Check if input is a valid float number, remove spaces and replace commas, clear message 
# alert and return, else inform user 
def check_float(potential_float):
    try:
        converted_string = float(potential_float.replace(',', '.').replace(' ', ""))
        lbl_result_msg["text"] = ""
        return converted_string
    except ValueError:
        lbl_result_msg["text"] = "Input a valid number."
        return False

# Function. Get value of input field, call check_float function to check valid input and save return value, 
# attempt num conversion of fahrenheit to celsius and display result to user, else break
def fahrenheit_to_celsius():
    try:
        fahrenheit = ent_temperature.get()
        result = check_float(fahrenheit)
        celsius = (5 / 9) * (float(result) - 32)
        lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
    except ValueError:
        return False

# Function. Get value of input field, call check_float function to check valid input and save return value, 
# attempt num conversion of celsius to fahrenheit and display result to user, else break
def celsius_to_fahrenheit():
    try:
        celsius = ent_temperature_cs.get()
        result = check_float(celsius)
        fahrenheit = (9 / 5) * (float(result)) + 32
        lbl_result_cs["text"] = f"{round(fahrenheit, 2)} \N{DEGREE FAHRENHEIT}"
    except ValueError:
        return False

# Instantiate the Tk module, set window title and window as non resizable
window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

# Style configuration of Tkk and custom Tkk styling classes
style = ttk.Style()
# style.configure("TFrame", foreground="black", background="white", padding="30")
style.configure("TButton", foreground="blue", background="white")
# style.configure("TLabel", foreground="red", background="white")
# style.configure("TEntry", foreground="black", background="white")
# style.configure("BW.TLabel", foreground="white", background="black")

# Configure size, scaling and padding of rows and cols in the grid
window.rowconfigure([0, 1, 2], weight=1, minsize=15, pad=15)
window.columnconfigure([0, 1, 2, 3], weight=1, minsize=0, pad=5)

# Create frames for main content and bind to window
frm_entry = ttk.Frame(master=window)
frm_entry_cs = ttk.Frame(master=window)

# Create required components for app
ent_temperature = ttk.Entry(master=frm_entry, width=10)
lbl_temp = ttk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")
btn_convert = ttk.Button(master=frm_entry, text="\N{RIGHTWARDS BLACK ARROW}", command=fahrenheit_to_celsius)
lbl_result = ttk.Label(master=frm_entry, text="\N{DEGREE CELSIUS}")

ent_temperature_cs = ttk.Entry(master=frm_entry_cs, width=10)
lbl_temp_cs = ttk.Label(master=frm_entry_cs, text="\N{DEGREE CELSIUS}")
btn_convert_cs = ttk.Button(master=frm_entry_cs, text="\N{RIGHTWARDS BLACK ARROW}", command=celsius_to_fahrenheit)
lbl_result_cs = ttk.Label(master=frm_entry_cs, text="\N{DEGREE FAHRENHEIT}")

lbl_result_msg = ttk.Label(master=window)

# Bind components to grid layout
frm_entry.grid(row=0, column=0, padx=15, sticky="w")
frm_entry_cs.grid(row=1, column=0, padx=15, sticky="w")

ent_temperature.grid(row=0, column=0)
lbl_temp.grid(row=0, column=1, padx=5)
btn_convert.grid(row=0, column=2)
lbl_result.grid(row=0, column=3, padx=(5, 0))

ent_temperature_cs.grid(row=1, column=0)
lbl_temp_cs.grid(row=1, column=1, padx=5)
btn_convert_cs.grid(row=1, column=2)
lbl_result_cs.grid(row=1, column=3, padx=(5, 0))

lbl_result_msg.grid(row=2, column=0)

# Function call to reset input fields
set_text(ent_temperature, 0)
set_text(ent_temperature_cs, 0)

# Bind a 'Return' keypress action to each input field and use a lambda function to invoke the 
# function call of the respective buttons
ent_temperature.bind("<Return>", lambda event=None: btn_convert.invoke())
ent_temperature_cs.bind("<Return>", lambda event=None: btn_convert_cs.invoke())

# Start the main loop
window.mainloop()
