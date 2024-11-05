import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkcalendar import DateEntry
from PIL import Image, ImageTk
import datetime
import re

def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def on_validate_date(P):
    if not validate_date(P):
        messagebox.showerror("Data Inválida", "Por favor, insira uma data válida no formato DD/MM/AAAA.")
        return False
    return True

def validate_money(value_if_allowed):
    if re.match(r"^R\$ \d{1,3}(?:\.\d{3})*,\d{2}$", value_if_allowed):
        return True
    return False

my_w = tk.Tk()
my_w.geometry("800x600") 
client = tk.StringVar(value='JOVEM PAN CURITIBA JOVEM PAN cURITIBA')
date = tk.StringVar(value='')
service = tk.StringVar(value='Pipoqueira, a opção pipoca salgada c/ bacon, durante 2 horas;')
service_value = tk.StringVar(value='R$ ')
s_filename = ''

l1 = tk.Label(my_w, text='Cliente', font=22, width=8, fg='blue')
l1.grid(row=0, column=0, padx=1, pady=10)
e1 = tk.Entry(my_w, font=22, width=8, textvariable=client)
e1.grid(row=0, column=1, padx=1, pady=10)

l2 = tk.Label(my_w, text='Data', font=22, width=8, fg='blue')
l2.grid(row=0, column=2, padx=1, pady=10, sticky='w')

vcmd_date = (my_w.register(on_validate_date), '%P')
e2 = DateEntry(my_w, font=22, textvariable=date, width=10, date_pattern='dd/mm/yyyy', validate='focusout', validatecommand=vcmd_date)
e2.grid(row=0, column=3, padx=1, pady=10, sticky='w')

l3 = tk.Label(my_w, text='Serviço', font=22, width=8, fg='blue')
l3.grid(row=1, column=0, padx=1, pady=10)
e3 = tk.Entry(my_w, font=22, textvariable=service, width=8)
e3.grid(row=1, column=1, padx=1, pady=10)

l4 = tk.Label(my_w, text='Valor total', font=22, width=8, fg='blue')
l4.grid(row=1, column=2, padx=1, pady=10, sticky='w')

vcmd_money = (my_w.register(validate_money), '%P')
e4 = tk.Entry(my_w, font=22, textvariable=service_value, width=12, validate='focusout', validatecommand=vcmd_money)
e4.grid(row=1, column=3, padx=1, pady=10, sticky='w')

def upload_file():
    global img, s_filename
    f_types = [('Jpg Files', '*.jpg')]
    s_filename = filedialog.askopenfilename(filetypes=f_types)
    img = ImageTk.PhotoImage(file=s_filename)
    b4 = tk.Button(my_w, image=img) # using Button 
    b4.grid(row=2, column=2, columnspan=2)
    #print(s_filename)

b2 = tk.Button(my_w, text='Gerar', font=22, command=lambda: my_w.destroy())
b2.grid(row=3, column=1, padx=10, pady=10)

my_w.mainloop()