import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkcalendar import DateEntry
from PIL import Image, ImageTk
import datetime
import re
import subprocess
from boxmessages import validate_fields, show_warning, validate_date

my_w = tk.Tk()
my_w.geometry("800x600") 
my_w.title('Proposta de Serviço Efatá Eventos')
client = tk.StringVar(value='JOVEM PAN')
date = tk.StringVar(value='')
service_value = tk.StringVar(value='350')
services = []
s_filename = ''

# Cliente
l1 = tk.Label(my_w, text='Cliente', font=22, width=8, fg='blue')
l1.grid(row=0, column=0, padx=10, pady=10, sticky='w')
e1 = tk.Entry(my_w, font=22, width=30, textvariable=client)
e1.grid(row=0, column=1, padx=10, pady=10, sticky='w')

# Data
l2 = tk.Label(my_w, text='Data', font=22, width=8, fg='blue')
l2.grid(row=1, column=0, padx=10, pady=10, sticky='w')

def on_validate_date(P):
    if not validate_date(P):
        messagebox.showerror("Data Inválida", "Por favor, insira uma data válida no formato DD/MM/AAAA.")
        return False
    return True

vcmd_date = (my_w.register(on_validate_date), '%P')
e2 = DateEntry(my_w, font=22, textvariable=date, width=12, date_pattern='dd/mm/yyyy', validate='focusout', validatecommand=vcmd_date)
e2.grid(row=1, column=1, padx=10, pady=10, sticky='w')

# Serviço
l3 = tk.Label(my_w, text='Serviço', font=22, width=8, fg='blue')
l3.grid(row=2, column=0, padx=10, pady=10, sticky='w')
e3 = tk.Text(my_w, font=22, width=75, height=1)
e3.grid(row=2, column=1, padx=10, pady=10, sticky='w')

def add_service():
    service_text = e3.get("1.0", tk.END).strip()
    if service_text:
        services.append(service_text)
        e3.delete("1.0", tk.END)
        messagebox.showinfo("Serviço Adicionado", "Serviço adicionado com sucesso!")

# Botão para adicionar serviço
b_add_service = tk.Button(my_w, text='Adicionar Serviço', font=22, command=add_service)
b_add_service.grid(row=2, column=2, padx=10, pady=10)

# Valor total
l4 = tk.Label(my_w, text='Valor total', font=22, width=8, fg='blue')
l4.grid(row=3, column=0, padx=10, pady=10, sticky='w')
e4 = tk.Entry(my_w, font=22, textvariable=service_value, width=12, validate='focusout')
e4.grid(row=3, column=1, padx=10, pady=10, sticky='w')

def upload_file():
    global img, s_filename
    f_types = [('Jpg Files', '*.jpg')]
    s_filename = filedialog.askopenfilename(filetypes=f_types)
    img = ImageTk.PhotoImage(file=s_filename)
    b4 = tk.Button(my_w, image=img) # using Button 
    b4.grid(row=2, column=2, columnspan=2)

def on_generate():
    if not validate_fields(client, date, service_value):
        if not show_warning("Campos Vazios", "Alguns campos estão vazios ou incorretos. Deseja prosseguir?"):
            return
    my_w.destroy()
    
# Botão Gerar
b2 = tk.Button(my_w, text='Gerar', font=22, command=on_generate)
b2.grid(row=6, column=0, columnspan=2, padx=10, pady=20)

def on_enter(event):
    event.widget.insert(tk.INSERT, "\n")

e3.bind("<Return>", on_enter)

my_w.mainloop()